# -*- coding: utf-8 -*-
# ! /usr/bin/python
import copy
import hashlib
import time

import requests
import os
import logging
import threading
import configparser
import json
import base64
from flask import Flask, render_template, send_from_directory, request, \
    redirect, url_for, jsonify
from flask import make_response, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
lock = threading.Lock()

APP_DIR = '/usr/local/adeploy-server'
UPLOAD_FOLDER = os.path.join(APP_DIR, 'upload')
SCAN_UPLOAD_FOLDER = os.path.join(APP_DIR, 'scan_upload')
SDSUPLOAD_FOLDER = os.path.join(APP_DIR, 'sdsupload')
SERVER_LOG = os.path.join(APP_DIR, 'log', 'server.log')
DOWNLOAD_LOG = os.path.join(APP_DIR, 'log', 'downloads.log')
DOWNLOAD_FILE = os.path.join(APP_DIR, 'downloads')
ALLOWED_EXTENSIONS = set(['zip'])  # 允许上传的文件后缀


# 自增下载量和记录下载日志的装饰器
def downloads_wrap(func):
    def cal_downloads(filename):
        try:
            res = func(filename)
        except Exception as e:
            raise

        # 仅统计下载安装包的下载请求
        if filename.endswith(
                "aDeploy-server-install.zip") or filename.endswith(
            "aDeploy-server-upgrade.zip"):
            undate_downloads(filename=filename)
        return res

    return cal_downloads


# 设置下载日志器
def set_download_log():
    # 设置下载日志器
    download_logger = logging.getLogger(DOWNLOAD_LOG)
    download_logger.setLevel(logging.INFO)

    # 设置下载日志器的处理器和等级和格式和时间格式
    if not os.path.exists(os.path.dirname(DOWNLOAD_LOG)):
        os.mkdir(os.path.dirname(DOWNLOAD_LOG))

    # 设置下载日志器的处理器
    download_handler = logging.FileHandler(filename=DOWNLOAD_LOG)
    # 设置日志和时间格式
    download_formatter = logging.Formatter(fmt="%(asctime)s : %(message)s",
                                           datefmt="%Y-%m-%d %H:%M:%S")
    download_handler.setFormatter(download_formatter)
    download_handler.setLevel(logging.INFO)

    # 添加日志处理器到下载日志器
    download_logger.addHandler(download_handler)


# 设置服务器日志器
def set_server_log():
    # 服务器日志器
    server_logger = logging.getLogger(SERVER_LOG)
    server_logger.setLevel(logging.ERROR)

    # 设置服务器日志器的处理器和等级和格式和时间格式
    if not os.path.exists(os.path.dirname(SERVER_LOG)):
        os.mkdir(os.path.dirname(SERVER_LOG))

    # 设置服务器日志器的处理器
    server_handler = logging.FileHandler(filename=SERVER_LOG)
    # 设置日志和时间格式
    server_formatter = logging.Formatter(fmt="%(asctime)s : %(message)s",
                                         datefmt="%Y-%m-%d %H:%M:%S")
    server_handler.setFormatter(server_formatter)
    server_handler.setLevel(logging.ERROR)

    # 添加日志处理器到下载日志器
    server_logger.addHandler(server_handler)


# 更新下载量记录
def undate_downloads(**kwargs):
    download_logger = logging.getLogger(DOWNLOAD_LOG)
    download_section = "download_log"
    downloads = configparser.ConfigParser()
    filename = kwargs.pop("filename")
    lock.acquire()
    try:
        # 找不到记录则创建文件
        try:
            downloads.read(DOWNLOAD_FILE)
        except Exception as e:
            with open(file=DOWNLOAD_FILE, mode="w", encoding="utf8") as fd:
                downloads.read(DOWNLOAD_FILE)
        # 找不到记录则创建section
        if not downloads.has_section(download_section):
            downloads.add_section(download_section)

        # 下载量加1
        downloads_num = downloads.getint(download_section, filename,
                                         fallback=0) + 1
        downloads.set(download_section, filename, str(downloads_num))
        with open(file=DOWNLOAD_FILE, mode="w", encoding="utf8") as fd:
            downloads.write(fd)

        # 打日志
        download_logger.info(
            "%s download file: %s success ! total downloads: %s" % (
                request.remote_addr, filename, downloads_num))
    except Exception as e:
        download_logger.error("%s cal download file: %s failed: %s ! " % (
            request.remote_addr, filename, e))
    finally:
        lock.release()


# 处理请求异常并记录日志
def handle_res_exception(func):
    def fn(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            server_logger = logging.getLogger(SERVER_LOG)
            server_logger.error("IP: %s URL: %s ERROR: %s" % (
                request.remote_addr, request.url, e))
            raise
        return res

    return fn


# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 解析base64编码
def safe_b64decode(decode_str):
    """
    base64编码以=号结尾，在url传输中被截取,这里补上足够#，以可以正常解码base64
    :param decode_str: base64格式的字符串
    :return: 解码后的字符串
    """
    if len(decode_str) % 4 != 0:
        decode_str += "=" * (4 - len(decode_str) % 4)
    return base64.urlsafe_b64decode(
        (decode_str.encode(encoding="utf-8"))).decode(encoding="utf-8")


# 具有上传功能的页面
@app.route('/upload', methods=['POST'])
@handle_res_exception
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return "ok"


@app.route("/")
def hello():
    return "hello!"


def add_patch(infos_dict, headers, key_id, time_, prd_line):
    """增加pkg"""
    prd_line_info = {
        "HCI": {"app_id": "10000", "app_key": "RTGDA1DDF6AE45459650FTG6116RF5C4"},
        "SCP": {"app_id": "10004", "app_key": "AF8BE843F81B11EAA1F2FEFCFE0BA1C6"},
        "SDS": {"app_id": "10005", "app_key": "B6EF5A0DF81B11EAA1F2FEFCFE0BA1C6"},
    }
    if prd_line in prd_line_info:
        version = infos_dict.get("version", "null-").split("-")[0]
        signature_params = {
            "appId": prd_line_info.get(prd_line).get("app_id"),
            "deviceType": headers.get("deviceType", "IOS"),
            "deviceId": headers.get("deviceId", "181d4eb9882146e8bf82467eb3049acd"),
            "timestamp": headers.get("timestamp", time_),
            "nonce": headers.get("nonce", str(333274)),
            "version": version or None,
        }

        key_values = list()
        for k, v in sorted(signature_params.items(),
                           key=lambda kv: (kv[0], kv[1])):
            if not v:
                continue
            kv_params = "{k}{v}".format(k=k, v=v)
            key_values.append(kv_params)

        headers = {
            "appKey": prd_line_info.get(prd_line).get("app_key"),
            "Content-Type": "application/json",
        }

        stringA = "".join(key_values)
        stringB = headers["appKey"] + stringA
        signature = hashlib.sha256(stringB.encode("utf-8")).hexdigest()
        headers["signature"] = signature
        headers.update(signature_params)
        # 在生成json文件之间先去发请求
        priId = "-".join([key_id, time_])
        infos_dict_cp = copy.deepcopy(infos_dict)
        requestBody = {}
        for k in infos_dict.keys():
            if k == "patches":
                requestBody["patchs"] = infos_dict.get("patches")
                infos_dict_cp.pop("patches")
            if k == "key_id":
                requestBody["dev_id"] = infos_dict.get("key_id")
                infos_dict_cp.pop("key_id")
            if k == "inspect_time":
                requestBody["createdAt"] = infos_dict.get("inspect_time")
                infos_dict_cp.pop("inspect_time")

        requestBody["priId"] = priId
        requestBody.update(infos_dict_cp)
        body_params = json.dumps(requestBody)
        try:
            with requests.Session() as session:
                ret = session.post(ITGW_URL, data=body_params, headers=headers)
                result = json.loads(ret.text)
                if ret.status_code == 200 and result.get("code") == 0:
                    print("post request success!!!")
                # 不管是否成功,都打印结果看下
                print(result.get("message"))
        except Exception as e:
            print(e)


@app.route('/jgupload', methods=['GET'])
def jgupload():
    infos = request.args.get('infos', {})
    infos = safe_b64decode(infos)
    infos_dict = json.loads(infos)
    prd_line = infos_dict.get("prd_line")
    key_id = infos_dict.get("key_id", "")
    current_time = int(round(time.time() * 1000))
    time_ = str(infos_dict.get("inspect_time", current_time))
    file_name = ''.join([key_id, '_', time_, '.json'])
    headers = request.headers
    save_path = os.path.join(SCAN_UPLOAD_FOLDER, file_name)
    add_patch_thread = threading.Thread(target=add_patch,
                                        args=(infos_dict, headers,
                                              key_id, time_, prd_line))
    add_patch_thread.start()
    with open(save_path, 'w') as fp:
        fp.write(infos)
    # 返回一个html页面:
    current_version = infos_dict.get("version")
    patches = infos_dict.get("patches")
    data = {
        "current_version": current_version,
        "patch_info": ",".join(patches),
    }
    return render_template("pkg_info.html", data=data)


@app.route("/download/<path:filename>")
@downloads_wrap
def downloader(filename):
    dirpath = os.path.join(app.root_path,
                           'download')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename,
                               as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


if __name__ == '__main__':
    set_download_log()
    set_server_log()
    app.run(host='0.0.0.0', port=8080, threaded=True)
