# coding:utf-8
import requests

RED_URL = "https://access.redhat.com/downloads/content/rhel---7.4/x86_64/4118/kernel/3.10.0-1062.21.1.el7/src/fd431d51/package-changelog"
TOKEN = "1589773580731.q1ZSczcS16VIH4DCGlCWnw=="

# https://access.redhat.com/downloads/content/rhel---8.1/x86_64/4118/kernel/3.10.1-1062.18.1.el7/src/fd431d51/package-changelog

account_number = "rd.sangfor@gmail.com"
password = "@Sangfor123"
# {username: "rd.sangfor@gmail.com", token: "1589422996052.b6XZNS7NAwAwW/bcX7sgCA=="}
# token: "1589422996052.b6XZNS7NAwAwW/bcX7sgCA=="
# username: "rd.sangfor@gmail.com"
data = {
    "username": account_number,
    "token": TOKEN,
    "Content-Type": "application/json"
}


# REQUEST_URL = "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/pdf/8.2_release_notes/Red_Hat_Enterprise_Linux-8-8.2_Release_Notes-en-US.pdf"

# import pdb;pdb.set_trace()
response = requests.post(RED_URL, params=data)
print(response.text.encode("utf-8"))


# import requests

# url = "https://www.12306.cn/mormhweb/"
# response = requests.get(url)
# print(response.text.encode("utf-8"))


# 链接
# https://github.com/kerbalwzy

https://simpleui.88cto.com/docs/simpleui/QUICK.html#%E4%B8%BB%E9%A2%98%E5%88%97%E8%A1%A8

# github仓库
https://github.com/TheAlgorithms/Python?utm_source=gold_browser_extension


# 关于时间
https://www.cnblogs.com/shilxfly/p/9436981.html

# 关于django + xadmin + echart 实现图表绘制
https://www.bbsmax.com/A/GBJrrQK3J0/


# xadmin后台图标搜集:
https://v3.bootcss.com/components/

# 博客集:
https://www.cnblogs.com/feifeifeisir/category/1413044.html

# xadmin 实现二级联动
https://www.bbsmax.com/A/1O5EOwmWz7/

# 小程序开发
https://www.bbsmax.com/A/VGzlNgBV5b/


# gRPC相关介绍:
https://segmentfault.com/a/1190000020592330

得去学:Django 中 使用 gRPC 或者 Flask 使用 gRPC


# RPC 资料链接:
https://blog.csdn.net/kalulioo/article/details/89189914?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase


# python 微服务的简单使用
https://blog.csdn.net/eagleuniversityeye/article/details/102722741?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

# git 工作流(面试大概率会问)

# REST API 与 restful API
关于 REST API:
https://blog.csdn.net/D_R_L_T/article/details/82562902

# 搜集下这两个库的使用:
from oslo_config import cfg
from oslo_log import log as loggi
import uuid
from webob import Response
from enum import Enum
from oslo_concurrency import processutils

关于数据库表设计的知识:
https://www.cnblogs.com/CrazyJioJio/p/12591679.html



mysql 远程访问不行解决方法 Host is not allowed to connect to this MySQL server:
进入数据库,执行:
navicat 设置连接远程数据库问题解决:
注明:123456 是你授权root用户登录时的密码

grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;

flush privileges;

MySQL只有information_schema,test两个数据库
https://www.jianshu.com/p/db91ecb697bc

蓝色理想:
网站设计:http://www.blueidea.com/

小黑格子屋:http://vlambda.com/wz_wQnSVaj4tA.html

好的github:
https://github.com/kon9chunkit/GitHub-Chinese-Top-Charts?utm_source=gold_browser_extension

云计算概念:
https://blog.csdn.net/weixin_30387799/article/details/96954805?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase

https://blog.csdn.net/liujg79/article/details/84453736

关于saas企业介绍:
https://www.zhihu.com/question/19797440

开源软件:
https://docs.mattermost.com/help/settings/theme-colors.html#custom-theme-examples

mattermost:介绍
https://www.zybuluo.com/tata/note/274699
https://networm.me/2019/02/17/mattermost-install/

slack:懒散的
https://www.zhihu.com/question/22890036

meth:就是method的意思,方法的意思
md,太多简写,导致单词的意思都对不上了

多线程:
https://blog.csdn.net/dd864140130/article/details/57128782?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase

博客:
https://www.cnblogs.com/lovecindywang/category/225505.html

python下的单例模式:
https://www.cnblogs.com/huchong/p/8244279.html

进击的巨人:
协程,多线程,多进程

好博客:
https://www.cnblogs.com/huchong/category/1061954.html

django 中关于timefield的字段介绍:
http://www.mamicode.com/info-detail-2243163.html

pyecharts绘制各种图表:
https://blog.csdn.net/update7/article/details/89086454

pyecharts更换加载echarts地址:
https://www.cnblogs.com/deliaries/p/12957771.html


django 中使用 pyecharts:本质上还是调用js中的echarts实现


xadmin使用介绍:
https://blog.csdn.net/qq_40083134/article/details/83343745?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

python翻译模块:pip install translate

知乎python总结精华:https://zhuanlan.zhihu.com/p/144644492

gitbook专栏:https://47.104.249.3/Django/mds/xadmin%E8%87%AA%E5%AE%9A%E4%B9%89.html

博客集:
http://code4fs.xyz/article/31/

redis教程:http://www.manongjc.com/redis/redis_benchmarks.html


python数据爬虫:https://www.cnblogs.com/kai-/p/12149742.html


django模板语法:https://www.cnblogs.com/machangwei-8/p/11044988.html

pycharm设置html模板中代码高亮和自动补全:
https://blog.csdn.net/liudinglong1989/article/details/81207108

##########
必须学会Pycharm编译环境在远程中的调试调用,同名方法或者函数的快速查找
##########

https://bigyoung.cn/
https://www.lizenghai.com/archives/69591.html

html空格标签介绍:
https://blog.csdn.net/weixin_30325971/article/details/95124748

echarts绘制折线图:
https://www.jb51.net/article/171512.htm

echarts属性设置:
https://www.cnblogs.com/benmumu/p/8316652.html

pyecharts:
http://pyecharts.herokuapp.com/

pycharm的远程调试配置:
https://blog.csdn.net/zhaihaifei/article/details/53691873

PyDev 是一个 Python 调试器 原本用 Eclipse 之类的东西写 Python 就会用这货或者 pdb 或者 ipdb 来调试

这名字可以
周微凡

echarts最全解释:
https://blog.csdn.net/qq_36330228/article/details/79945928

echarts双y轴显示数据:
https://blog.csdn.net/shu580231/article/details/77837279

django模板继承:https://blog.csdn.net/weixin_43860025/article/details/91450142

数据结构与算法:https://www.cnblogs.com/zknublx/category/883119.html

GraphQL:https://www.zhihu.com/question/264629587

django 模型表数据库设计:
https://www.cnblogs.com/chushujin/p/12533851.html

django ORM:
当queryset非常巨大时，cache会成为问题。此时可以queryset.iterator()
https://blog.csdn.net/dyunspace_csdn/article/details/70063296

odoo技术手册:
https://www.sunpop.cn/documentation/12.0/reference/views.html

关于django新旧版本路由的介绍:
https://blog.csdn.net/bbwangj/article/details/79935500

django admin中搜索框 搜外键相关字段:
https://www.cnblogs.com/Brin-guo/p/8963706.html

django ajax请求:
https://www.cnblogs.com/wanlei/p/10297083.html

django下载文件:
https://blog.csdn.net/weixin_30448603/article/details/95460528

jinja语法:
https://jinja.palletsprojects.com/en/2.11.x/

docxtpl:
https://docxtpl.readthedocs.io/en/stable/

python处理docx表格文件:
https://zhuanlan.zhihu.com/p/38413601

个人博客网站:
http://www.chenxm.cc/article/147.html

django中的import_export导入/导出库:
https://www.cnblogs.com/pcent/p/10809136.html
https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource
https://django-import-export.readthedocs.io/en/latest/getting_started.html

https://segmentfault.com/a/1190000004401099
dajngo 数据校验模型扩展包:
https://github.com/romain-li/django-validator

python iterator介绍:(专门为了生成器迭代器设计的内置包)
https://www.jb51.net/article/178330.htm
https://docs.python.org/zh-cn/3.7/library/itertools.html

python global关键字解释:
https://www.jb51.net/article/169395.htm

python tablib模块:
https://pypi.org/project/tablib/
https://cloud.tencent.com/developer/news/439849

django中import-export的改写:
https://www.jianshu.com/p/f82a465a41d8
如何将文件格式限制为仅限CSV,XLS和XLSX？
http://www.voidcn.com/article/p-mtaweymx-bwh.html

python 有序字典:
https://www.cnblogs.com/zhenwei66/p/6596248.html
# 有序字典取值:setdefault
task_uuid = row.setdefault("测试任务UUID")
server_uuid = row.setdefault("服务器UUID")

xadmin自定义菜单栏显示顺序:
https://www.cnblogs.com/fiona-zhong/p/9647721.html
https://blog.csdn.net/weixin_41622043/article/details/96330570
# 注意:class GlobalSetting 去继承 CommAdminView 父类

xadmin app设置中文显示:
https://www.dazhuanlan.com/2019/12/07/5deb002378fd6/

django xadmin 隐藏菜单栏右侧的数字图标标签，或自定义标签:
https://blog.csdn.net/ch_improve/article/details/103023101

django xadmin隐藏顶部“增加”按钮:
https://blog.csdn.net/ch_improve/article/details/103023006

屏蔽Django admin界面添加按钮的操作:
https://www.zhangshengrong.com/p/Z9a23j9zNV/

隐藏指定app中的model菜单栏不显示:
https://www.cnblogs.com/roystime/p/6866964.html?utm_source=itdadao&utm_medium=referral
在adminx.py中的Admin类增加属性hidden_menu = True即可

django中日期时间的问题:
https://blog.51cto.com/xujpxm/2090382

Django ORM 模糊查询和查询操作:
https://www.cnblogs.com/ls1997/p/10955402.html

Python 获得最近一个月的每天的日期:
https://www.cnblogs.com/xuchunlin/p/10722623.html

程序中的递归:
https://www.cnblogs.com/schut/p/10625111.html

test_tasks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0]
test_tasks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 3, 3, 3]
上面的列表如何变成下面的列表?
如下简单的方法:

def sum_tasks(task_num):
    tasks = list()
    tmp_num = 0
    for item in task_num:
        tmp_num += item
        tasks.append(tmp_num)
    return tasks

下面这个的使用:
class Meta:

django查询集API:
https://www.cnblogs.com/xuchunlin/p/6676301.html

博客园:
https://www.cnblogs.com/renoyuan/p/11724616.html

FastAPI框架:
https://www.jianshu.com/p/7849c8be415b

django + uwsgi + nginx 部署:
https://www.jianshu.com/p/b91447672b35

https://prismjs.com/download.html

uwsgi测试报错:
uwsgi: unrecognized option '--http:8000'
getopt_long() error
解决办法:去掉 --http:8000 中间的 : 号即可
https://segmentfault.com/q/1010000007395155
uwsgi --http 8000 --wsgi-file tester.py

xshell打开多个窗口，没有标题显示的解决方法:
https://blog.csdn.net/huangbaokang/article/details/84939430
按ctrl +shift +t快捷键解决。

python 正则表达式总结:
https://www.cnblogs.com/misswangxing/p/10736310.html

python中用json存储列表字典等文件操作:
https://www.cnblogs.com/feng-hao/p/10822631.html
JSON字符串用json.dumps, json.loads JSON文件名用json.dump, json.load
https://www.jb51.net/article/110899.htm

python – 如何逐步写入json文件:
https://www.jb51.cc/python/186612.html
import json

def write_json(jlist):
    # 将bx列表写入json文件
    with open('data/bx_list.json', 'w') as f_obj:  
        json.dump(jlist, f_obj)


def read_json():
    # 读取存储于json文件中的列表
    with open('data/bx_list.json', 'r') as f_obj:
        jlist = json.load(f_obj)
    return jlist



爬虫第一步:模拟登录
https://zhuanlan.zhihu.com/p/59733826

个人邮箱手机号注册网站:
https://mp.weixin.qq.com/s?__biz=MzA5NDk4NDcwMw==&mid=2651386828&idx=1&sn=b33210dde8e0eea6d06932c0ab70b299&chksm=8bba135cbccd9a4acdd08a4af2536e6dc311ea2bd1845f8c8df9a6fd943aee7f4b7e7dabce4b&token=258555898&lang=zh_CN#rd

https://mp.weixin.qq.com/s?__biz=MzA5NDk4NDcwMw==&mid=2651386588&idx=1&sn=307829fbd6db0aaace975311284a9ecf&chksm=8bba124cbccd9b5a728338eff2343cf72ad6c6f88708c48750e8bdd4acfc07f3007463eb3c34&scene=21#wechat_redirect


模拟登录github:
https://github.com/Kr1s77/awesome-python-login-model

python精美小例子:
https://github.com/jackzhenguo/python-small-examples?utm_source=gold_browser_extension

Cpython:
https://github.com/cython/cython?utm_source=gold_browser_extension


python模拟登录:
https://blog.csdn.net/weixin_34357928/article/details/91426164?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase


分析:先手动登录,网页端拿到cookie之后,再get请求 添加 headers 参数,携带cookie请求 package-changelog 页面获取数据.

Fiddler抓取HTTPS配置:
https://www.cnblogs.com/liulinghua90/p/9109282.html

Fiddler官方文档翻译:
https://www.kancloud.cn/gaogui/l2/420405

[Android 原创] fiddler抓包工具详细配置方法
https://www.52pojie.cn/thread-1171662-1-1.html

吾爱破解工具包:
https://down.52pojie.cn/Tools/

Fiddler资料链接:
https://www.cnblogs.com/yyhh/p/5140852.html

OpenResty:
https://zhuanlan.zhihu.com/p/94623469

fiddler如何设置才能抓FireFox的包？
https://blog.csdn.net/zhoutaohenan/article/details/8477993
https://blog.csdn.net/qq_35182128/article/details/97612206?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

http状态码:
https://www.php.cn/web/web-http422.html

一个代码库的好网站:
https://www.ctolib.com/

Python爬虫汇总:
https://zhuanlan.zhihu.com/p/112526698

js2py库:
https://www.yiyult.com/201906037223.html

selenium + phantomJS资料:
https://www.cnblogs.com/miqi1992/p/8093958.html

人人网模拟登录:
https://www.cnblogs.com/LexMoon/p/pyspider04.html

注意:在git提交项目出现这个问题的时候:
warning: unable to access '.gitignore': Permission denied
需要把.gitignore 文件放在跟项目同级的目录内,  警告中的.gitignore是一个目录,删除掉即可

pycharm如果不显示annotate(版本控制的提示信息):
https://www.iteye.com/blog/shareisattitude-2389427
菜单栏-->VCS-->enable version control Intrgration

如何在局域网内开一家电影院:
https://www.cnblogs.com/LexMoon/p/mov.html

file:///D:/BaiduNetdiskDownload/PythonSpider%E8%AF%BE%E4%BB%B6(%E6%96%B0%E7%89%88%E8%AF%BE%E4%BB%B6alpha)/%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91/2.%E6%A1%86%E6%9E%B6%E9%9B%8F%E5%BD%A2%E5%AE%9E%E7%8E%B0/2.%E6%A1%86%E6%9E%B6%E9%9B%8F%E5%BD%A2--%E6%A0%B8%E5%BF%83%E6%A8%A1%E5%9D%97.html

urls:
//div[@class="option pull-left"][2]/select[@id="evr"]/option/@value
文本内容:
//div[@class="option pull-left"][2]/select[@id="evr"]/option/text()

https://access.redhat.com

chrome无头浏览器使用:
https://www.cnblogs.com/kaibindirver/p/11432850.html

chrome启动选项参数:
https://www.jianshu.com/p/04848a35fe0a
https://peter.sh/experiments/chromium-command-line-switches/

在线加密解密:
https://tool.oschina.net/encrypt?type=3

在线编码转换:
https://tool.oschina.net/encode?type=4

利用xpath获取text或者href内容:
https://blog.csdn.net/onesmile5137/article/details/90696785

第九节：JWT简介和以JS+WebApi为例基于JWT的安全校验
https://www.cnblogs.com/yaopengfei/p/10451189.html

处理txt文本数据:
https://github.com/JGPY/Python_The-wisdom-of-life/tree/master/autoTXT

未保存的:
3.10.0-957.38.2.el7
3.10.0-862.34.1.el7
3.10.0-514.55.4.el7
3.10.0-514.53.1.el7
3.10.0-327.28.2.el7



https://access.redhat.com/downloads/content/rhel---7.4/x86_64/4118/kernel/3.10.0-957.41.1.el7/src/fd431d51/package-changelog




3.10.0-1062.26.1.el7 [最新的]
3.10.0-1062.21.1.el7 
3.10.0-1062.18.1.el7 
3.10.0-1062.12.1.el7 
3.10.0-1062.9.1.el7 
3.10.0-1062.7.1.el7 
3.10.0-1062.4.3.el7 
3.10.0-1062.4.2.el7 
3.10.0-1062.4.1.el7 
3.10.0-1062.1.2.el7 
3.10.0-1062.1.1.el7 
3.10.0-1062.el7 
3.10.0-957.54.1.el7 
3.10.0-957.48.1.el7 
3.10.0-957.46.1.el7 
3.10.0-957.43.1.el7 
3.10.0-957.41.1.el7 
3.10.0-957.38.3.el7 
3.10.0-957.38.2.el7 
3.10.0-957.38.1.el7 
3.10.0-957.35.2.el7 
3.10.0-957.35.1.el7 
3.10.0-957.27.4.el7 
3.10.0-957.27.2.el7 
3.10.0-957.21.3.el7 
3.10.0-957.21.2.el7 
3.10.0-957.12.2.el7 
3.10.0-957.12.1.el7 
3.10.0-957.10.1.el7 
3.10.0-957.5.1.el7 
3.10.0-957.1.3.el7 
3.10.0-957.el7 
3.10.0-862.51.1.el7

3.10.0-862.48.1.el7 
3.10.0-862.46.1.el7 
3.10.0-862.44.2.el7 
3.10.0-862.43.3.el7 
3.10.0-862.43.2.el7 
3.10.0-862.43.1.el7 
3.10.0-862.41.2.el7 
3.10.0-862.41.1.el7 
3.10.0-862.37.1.el7 
3.10.0-862.34.2.el7 
3.10.0-862.34.1.el7 
3.10.0-862.32.2.el7 
3.10.0-862.32.1.el7 
3.10.0-862.29.1.el7 
3.10.0-862.27.1.el7 
3.10.0-862.25.3.el7 
3.10.0-862.20.2.el7 
3.10.0-862.14.4.el7 
3.10.0-862.11.6.el7 
3.10.0-862.9.1.el7 
3.10.0-862.6.3.el7 
3.10.0-862.3.3.el7 
3.10.0-862.3.2.el7 
3.10.0-862.2.3.el7 
3.10.0-862.el7 
3.10.0-693.58.1.el7 
3.10.0-693.55.1.el7 
3.10.0-693.50.3.el7 
3.10.0-693.47.2.el7 
3.10.0-693.46.1.el7 
3.10.0-693.44.1.el7 
3.10.0-693.43.1.el7 
3.10.0-693.39.1.el7 
3.10.0-693.37.4.el7 
3.10.0-693.35.1.el7 
3.10.0-693.33.1.el7 
3.10.0-693.25.7.el7 
3.10.0-693.25.4.el7 
3.10.0-693.25.2.el7 
3.10.0-693.21.1.el7 
3.10.0-693.17.1.el7 
3.10.0-693.11.6.el7 
3.10.0-693.11.1.el7 
3.10.0-693.5.2.el7 
3.10.0-693.2.2.el7 
3.10.0-693.2.1.el7 
3.10.0-693.1.1.el7 
3.10.0-693.el7 
3.10.0-514.61.1.el7 
3.10.0-514.58.1.el7 
3.10.0-514.55.4.el7 
3.10.0-514.53.1.el7 
3.10.0-514.51.1.el7 
3.10.0-514.48.5.el7 
3.10.0-514.48.3.el7 
3.10.0-514.48.1.el7 
3.10.0-514.44.1.el7 
3.10.0-514.41.1.el7 
3.10.0-514.36.5.el7 
3.10.0-514.36.1.el7 
3.10.0-514.35.1.el7 
3.10.0-514.32.3.el7 
3.10.0-514.32.2.el7 
3.10.0-514.28.2.el7 
3.10.0-514.28.1.el7 
3.10.0-514.26.2.el7 
3.10.0-514.26.1.el7 
3.10.0-514.21.2.el7 
3.10.0-514.21.1.el7 
3.10.0-514.16.1.el7 
3.10.0-514.10.2.el7 
3.10.0-514.6.2.el7 
3.10.0-514.6.1.el7 
3.10.0-514.2.2.el7 
3.10.0-514.el7 
3.10.0-327.62.1.el7 
3.10.0-327.61.3.el7 
3.10.0-327.59.3.el7 
3.10.0-327.59.2.el7 
3.10.0-327.59.1.el7 
3.10.0-327.58.1.el7 
3.10.0-327.55.3.el7 
3.10.0-327.55.2.el7 
3.10.0-327.55.1.el7 
3.10.0-327.53.1.el7 
3.10.0-327.49.2.el7 
3.10.0-327.46.1.el7 
3.10.0-327.44.2.el7 
3.10.0-327.41.4.el7 
3.10.0-327.41.3.el7 
3.10.0-327.36.3.el7 
3.10.0-327.36.2.el7 
3.10.0-327.36.1.el7 
3.10.0-327.28.3.el7 
3.10.0-327.28.2.el7 
3.10.0-327.22.2.el7 
3.10.0-327.18.2.el7 
3.10.0-327.13.1.el7 
3.10.0-327.10.1.el7 
3.10.0-327.4.5.el7 
3.10.0-327.4.4.el7 
3.10.0-327.3.1.el7 
3.10.0-327.el7 
3.10.0-229.49.1.el7 
3.10.0-229.48.1.el7 
3.10.0-229.46.1.el7 
3.10.0-229.44.1.el7 
3.10.0-229.42.2.el7 
3.10.0-229.42.1.el7 
3.10.0-229.40.1.el7 
3.10.0-229.38.1.el7 
3.10.0-229.34.1.el7 
3.10.0-229.30.1.el7 
3.10.0-229.28.1.el7 
3.10.0-229.26.2.el7 
3.10.0-229.24.2.el7 
3.10.0-229.20.1.el7 
3.10.0-229.14.1.el7 
3.10.0-229.11.1.el7 
3.10.0-229.7.2.el7 
3.10.0-229.4.2.el7 
3.10.0-229.1.2.el7 
3.10.0-229.el7 
3.10.0-123.20.1.el7 
3.10.0-123.13.2.el7 
3.10.0-123.13.1.el7 
3.10.0-123.9.3.el7 
3.10.0-123.9.2.el7 
3.10.0-123.8.1.el7 
3.10.0-123.6.3.el7 
3.10.0-123.4.4.el7 
3.10.0-123.4.2.el7 
3.10.0-123.1.2.el7 
3.10.0-123.el7

优质的博客:
https://www.nmirage.com/sort/secure
https://www.oschina.net/blog/3217082
企业网管:
https://www.cnblogs.com/medik/p/10989759.html

centos7安装svn客户端和使用:
https://blog.csdn.net/weixin_30408309/article/details/95457257
步骤:
rpm -qa subversion # 检查是否已经安装svn
yum remove -y subversion  # 移除svn
yum install -y subversion  # 安装svn
svnserve --version  # 查看版本信息
svn checkout http://xxx.xx.xx/xx  # 下载svn远端服务器上指定项目的代码 地址是http的形式
svn checkout svn://500.900.23.140/PATH/custom/HCIPLATFORM  # 下载svn远端服务器上指定项目的代码  地址是svn的形式

bdb.py


python dir()与__dict__的区别:
https://www.cnblogs.com/zjchao/p/7894477.html
https://www.cnblogs.com/xxpythonxx/p/11831384.html


python 执行终端命令的库:
https://blog.csdn.net/hpwzjz/article/details/82992176
subprocess

python用字典实现switch-case功能:
https://www.cnblogs.com/Ralph-Wang/p/3395322.html

如何检查字符串在Python中是大小写还是混合大小写？
https://cloud.tencent.com/developer/ask/64073
字符串中有许多“方法”。islower()并且isupper()应该满足您的需求:
例如:
sp_name = "custom-aSec-bandwidth"
执行  sp_name.islower()
返回  False
执行:
sp_name.isupper()
返回  False

说明既不是小写也不是大写,是大小写混用:
因为: sp_name = "custom-asec-bandwidth"
执行  sp_name.islower()
返回  True
说明  islower/isupper 只是针对26个字母进行判别,非字母符号不影响.


# 删除test这个目录及其里面的子目录和文件
import shutil
shutil.rmtree(path=top)
就是相当于 rm xxx -rf 的命令

git add 操作时候警告: warning:The file will have its original line endings in your working directory
https://www.cnblogs.com/shijieli/p/10535051.html

解决办法:
执行下面的命令: 
# git config --global core.autocrlf false

python操作svn的扩展包:
https://pypi.org/project/svn/
看下如何获取author等信息

python实现定时任务:
https://blog.csdn.net/chen801090/article/details/93335733

python使用logging实现简易的日志系统:
https://www.cnblogs.com/goodhacker/p/3355660.html

python爬取qq音乐:
https://www.cnblogs.com/taotaoblogs/p/6872508.html

djang多对多时添加数据:
出现报错:TypeError: Direct assignment to the forward side of a many-to-many set is prohibited.
https://blog.csdn.net/ckk727/article/details/104031911
解决办法:多对多字段 先 add() ,
不能 还就是不能 Tice(**pkg_attrs) 这么写,否则下面的
多对多 version字段无法设置
tice_obj = Tice.objects.create(**pkg_attrs)
tice_obj.version.add(version_obj)

django使用celery实现定时任务:
https://www.cnblogs.com/huang-yc/p/10110754.html
https://www.cnblogs.com/crb912/p/8976937.html

在做一个django项目的时候，我遇到了一个定时任务的需求，我这里是需要定时扫描数据库并发送邮件，在查阅相关资料后，总结出如下几个方法

1.使用while创建一个死循环，判断时间，从而执行一些函数
2.使用APScheduler库实现定时任务 （详情可以见http://blog.csdn.net/hui3909/article/details/46652623）
3.django-crontab实现定时任务
4.django-celery实现定时任务

使用APScheduler库实现定时任务:
https://blog.csdn.net/hui3909/article/details/46652623

<<<<<<< HEAD
paramiko执行命令实时输出的问题:
https://zhangge.net/5122.html

python 3.6之后引入的新的字符串格式化:f-strings格式化:
https://blog.csdn.net/qq_29027865/article/details/84850683

python中os.path.isdir()和os.path.isfile()的正确用法:
https://www.jianshu.com/p/582910d13501


with self.client:
    self.exec_remote_cmd(compile_cmd)
    self.exec_remote_cmd(mv_dev_pkg_cmd)
    self.exec_remote_cmd(generate_md5_cmd)

只要 self.client 对象中有__enter__和__exit__内置方法,就可以使用with语法进行自动开闭资源的操作,
省去最后的close的写法
使用dir(self.client)查看其所有的属性和方法:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__',......]

django 中间件的五种自定义使用方法:
https://www.cnblogs.com/buyisan/p/8557252.html

Django（Python）前后端交互:
https://www.cnblogs.com/zhuchenglin/p/10763795.html

前端站长素材:
http://sc.chinaz.com/tag_jiaoben/danchukuang.html

termius:更好的终端工具
https://www.termius.com/

Django使用message框架向模板中推送消息内容:
https://www.cnblogs.com/jl-bai/p/6209653.html
https://www.cnblogs.com/zihao1037/p/11037801.html
https://www.jianshu.com/p/5344c120eca6

xadmin中的提示消息也是使用这个包实现的

Django 开启CSRF保护:
https://www.qttc.net/211-python-django-post-csrf.html

django面试基础题:
https://blog.csdn.net/weixin_42186490/article/details/90638399?utm_medium=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

Github上 10 个开源免费且优秀的后台控制面板:
https://blog.csdn.net/qq_29055201/article/details/84781865?utm_medium=distribute.down_relevant_right.none-task-blog-BlogCommendFromBaidu-7.nonecase&depth_1-utm_source=distribute.down_relevant_right.none-task-blog-BlogCommendFromBaidu-7.nonecase

后台UI集合:
https://github.com/chenxingxing6/AdminUi

源码编译安装redis:
https://blog.csdn.net/huangyuhuangyu/article/details/80263525

vim 编辑文件时遇到:   E325: 注意
					 发现交换文件 ".nginx.conf.swp"
https://blog.csdn.net/oxinliang12/article/details/73613879/


Django+Celery+redis kombu.exceptions.EncodeError:Object of type is not JSON serializable报错:
注意是celery版本的问题:
https://www.cnblogs.com/hszstudypy/p/12153416.html

celery优质博客:
https://www.itread01.com/content/1538621943.html

记个问题:
消息队列,多线程,多进程,协程等异步任务中如何实现pdb的断点调试???
https://blog.csdn.net/DeathlessDogface/article/details/84074461

Python协程爬虫实现断点续爬与分布式爬虫原理举例:
https://www.52pojie.cn/thread-1210439-1-1.html

django中csrf中间件的说明:
https://www.cnblogs.com/h2zZhou/p/9776270.html

Django常用的QuerySet操作:
https://www.cnblogs.com/zihao1037/p/11050397.html

python3异步编程详解:
https://blog.csdn.net/lu8000/article/details/45025987?utm_medium=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase


https://pyrasite.readthedocs.io/en/latest/Payloads.html
python内存泄露诊断过程:
https://www.51dev.com/python/17998

Python 进程内存增长解决方案:
https://zhuanlan.zhihu.com/p/28031057

pudb调试多进程Python代码:
https://zhuanlan.zhihu.com/p/107044373

FastAPI框架:
https://zhuanlan.zhihu.com/p/136887785

Python如何高效的调试:
https://www.zhihu.com/question/21572891

2020年最新的golang教程直接看：
https://www.bilibili.com/video/BV1Vi4y1t71d?p=1

rust程序设计语言:
https://kaisery.gitbooks.io/rust-book-chinese/content/

git开发中文手册:
https://www.php.cn/manual/view/34956.html

优雅的git message:
https://juejin.im/post/5f0818c15188252e906f8bac?utm_source=gold_browser_extension

检出:就是找到,找出的意思

爬虫管理平台:crawlab:
https://juejin.im/post/5efac4ab6fb9a07e5d76b86a

MySQL面试集锦:
https://juejin.im/post/5f09c24be51d4534a81aa11d?utm_source=gold_browser_extension

微信排版工具:
https://mdnice.com/?from=juejin

掘金大厂面试集锦:
https://juejin.im/post/5e7d4e8b6fb9a03c6422f112?utm_source=gold_browser_extension
https://github.com/sanyuan0704/my_blog

Cpythonyuanm源码:
https://github.com/python/cpython/blob/master/Modules/socketmodule.c

设计模式:
https://www.cnblogs.com/taosiyu/p/11293949.html

C语言教学视频:
http://c.biancheng.net/video/c/

内网时间同步:
执行:
yum install -y ntpdate
然后执行:
注意: ntp.sjtu.edu.cn 这个是你内网的时间服务器域名
ntpdate ntp.sjtu.edu.cn

一张图总结操作系统核心知识:
https://juejin.im/post/5f0d04ae5188252e7a1c717a?utm_source=gold_browser_extension#heading-10

ELK日志搜集介绍:
https://blog.csdn.net/qiushisoftware/article/details/100298046

快速搭建ELK教程:
https://www.cnblogs.com/yuhuLin/p/7018858.html

https://segmentfault.com/a/1190000003689999
https://www.cnblogs.com/along21/p/8613115.html

linux中的 diff 命令详解:
https://www.cnblogs.com/wf-linux/p/9488257.html

通过Python模块filecmp 对文件比较的实现方法:
https://www.jb51.net/article/142813.htm
https://www.cnblogs.com/franknihao/p/7649746.html

优秀的博客:
https://www.cnblogs.com/wangbin2188/tag/python/

Linux专题:
https://www.linuxprobe.com/python-exit-exit.html

Python递归return退出的问题:
https://blog.csdn.net/qq878594585/article/details/82193249

Python运算符:
https://www.runoob.com/python/python-operators.html

数据结构-位图原理及实现
https://blog.csdn.net/lucky52529/article/details/90172264

python实现文件夹文件遍历及比对:
https://blog.csdn.net/xiaxuesong666/article/details/78470035?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-4-78470035.nonecase

董伟明博客:
https://old.dongwm.com/

Python 标准库 shutil用法介绍:
https://m.jb51.net/article/145522.htm?ivk_sa=1023345p

# 遇到多层循环的场景, 注意: 先从内层小循环开始,然后再逐层向外扩展.

python字符串格式化好图:
https://www.cnblogs.com/lvcm/p/8859225.html

如何自定义导包?
# 添加自定义导包路径                      
CURRENT_DIR = os.path.dirname(os.
# 就是把当前文件所在路径的上一级路径添加到系统环境变量中,以便c
sys.path.insert(0, os.path.dirnam
# 下面这样是不行的,需要再来上一级路径             
# sys.path.insert(0, CURRENT_DIR)

下面的这个是正确操作:
centos7磁盘(新增磁盘后,原有磁盘也是这么扩容的,没区别)扩容之后进行分区,格式化,挂载的操作:
https://blog.csdn.net/sinat_34104446/article/details/84637590?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase

注意原有磁盘上面扩容后执行 fdisk /dev/vda  命令后,先按n 新建分区,再按p新建主分区,然后就和上面的教程步骤一致了.

ubuntu磁盘扩容:
https://blog.51cto.com/12348890/2092339

Centos7原有磁盘扩容:
https://cloud.tencent.com/developer/article/1634538

查看磁盘空间大小:
https://www.cnblogs.com/liaojie970/p/9026457.html

windows安装mongodb:
# 下面这个教程中的log日志路径设置和自己的有出入,不能照搬.
https://www.cnblogs.com/TM0831/p/10606624.html
https://www.jb51.net/article/164138.htm

windows下面启动MongoDB,然后在windows的服务列表中就可以看到MongoDB的服务了:
net start MongoDB

robo3t连接时报错:network error while attemping to run command 'getnonce' on host 'localhost:27017'
https://blog.csdn.net/xuxiaoyu122/article/details/104546339

ubuntu系统下非root用户使用filezilla软件传输文件时,需要先给目的目录进行授权操作.