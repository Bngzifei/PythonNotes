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