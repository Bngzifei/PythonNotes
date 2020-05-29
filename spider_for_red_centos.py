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
from oslo_log import log as logging
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