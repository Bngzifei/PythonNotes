大的方向:

布隆过滤器:
设计模式:
数据结构与算法:
数据库调优:
redis:
mongodb:
多线程多进程协程:
消息队列:
RPC
领域驱动设计
敏捷开发
GDB
websocket
SSE(Server Sent Events)
Redis的 ORM  redisco Walrus
发布/订阅模式
asyncio框架,未来web开发不可能离开websocket等实时技术
k8s-容器编排


redis命令介绍:
http://redisdoc.com/

谈谈装饰器，迭代器，yield，内存管理等

Python高并发解决方案

web安全相关，sql注入，xss

如何面试Python开发?
https://www.zhihu.com/question/33398583

面试经历:
https://segmentfault.com/a/1190000014540229

牛客网:
https://www.nowcoder.com/discuss/136491

核心: 扎实的基础和灵活的思维
公司 艾维邑动
http://avazuinc.com/home/

https://www.appannie.com/cn/
JD:工作描述 (job description)

剑指offer
牛客左神

Python之美专刊:
https://zhuanlan.zhihu.com/python-cn

sanic项目:
https://github.com/dongweiming/lyanna

python分支代码技巧:
https://zhuanlan.zhihu.com/p/35425907

详解Python元类:
https://zhuanlan.zhihu.com/p/30861351

算法题:
https://labuladong.gitbook.io/algo/

Python布隆过滤器:
https://www.cnblogs.com/yscl/p/12003359.html

https://my.oschina.net/u/4336234/blog/3441424

站酷:UI设计网站
https://www.zcool.com.cn/

debian教程:
https://www.debian.org/doc/manuals/debian-reference/ch01.zh-cn.html

网页转成PDF,搜集一下

一个完整的项目设计:
https://zhuanlan.zhihu.com/p/28672237

python web框架评测网站:
https://python-guide.readthedocs.io/en/latest/scenarios/web/

python web 应用性能调优:
https://tech.glowing.com/cn/python-web-performance-optimization/

用于替换requests的性能更好的库:
https://github.com/gwik/geventhttpclient

提的合并:
https://github.com/gwik/geventhttpclient/pull/85

opentracing, 完善分布式环境下的性能追踪

阅读开源项目代码:
https://zhuanlan.zhihu.com/p/22275595

新版的pypi站点:https://pypi.org/

开发中经常提及的Pr是什么意思？
PR是Pull Request缩写，Git/svn之类用的。比如GitHub上的项目，你pull下来，
修改了部分代码之后再提交PR，然后管理员觉得你改的代码没毛病，确认。这个项目某部分代码就改成你的了.

python web开发实战:
https://zhuanlan.zhihu.com/p/22371355

潘俊勇

https://python-modernize.readthedocs.io/en/latest/

PR模板指导:
https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository

BTW:顺便一提 (by the way)

代码质量保证:
https://zhuanlan.zhihu.com/p/22338225

Python 不能不知的模块:
https://zhuanlan.zhihu.com/p/22246193

golang erlang

terminus 打开本地终端: 快捷键  Ctrl + L

windows下python第三方的库集合:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

No module named '_curses'解决办法:
https://www.pianshen.com/article/9233675404/

windows下安装bpython:
https://www.cnblogs.com/zhaojiedi1992/p/zhaojiedi_python_006_bpython.html

按位取反运计算方法:
https://blog.csdn.net/xiexievv/article/details/8124108

学术科研互动平台:
http://muchong.com/t-11559382-1

golang公链学习资料:
https://blog.csdn.net/itcastcpp/article/details/86603408

Golang精编100题-搞定golang面试:
https://blog.csdn.net/itcastcpp/article/details/80462619?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.nonecase

截图神器:ShareX
https://github.com/ShareX/ShareX/releases/tag/v13.1.0

Python 文件操作常用函数:

1.> 等效于 rm * -rf 命令递归删除的:
import shutil
shutil.rmtree(路径)

2.> 等效于 mkdir -p 命令递归创建目录:

os.makedirs(dst)

3.> 等效于 cp -r src_path dst_path
import shutil
shutil.copytree(src, dst)

4. 注意: os.system(系统命令)
返回值为0 才是正常执行,否则就是执行失败

5. 这种就是程序退出,类似于 手动按下 ctrl + c 键:
import sys
sys.exit()

6.切换到指定目录:
os.chdir(指定路径)

7.获取当前所在路径:
os.getcwd()

仔细看下这个仓库:
https://github.com/jumper2014/PyCodeComplete

做成这个打包:
https://www.jianshu.com/p/692bab7f8e07

知乎专栏-Python实践之路:
https://zhuanlan.zhihu.com/python2018

知乎专栏-90 条写 Python 程序的建议:
https://zhuanlan.zhihu.com/p/144228839

这个网站需要挂代理才能访问:
https://itbook.download/

自定义编写的python脚本实现开机自启动。

增量爬虫，最主要的就是爬取的url的去重,所以需要持久化存储,那就使用mongodb存起来,
当再次爬取的时候,进行比对去重,实现增量爬取。

解决报错:[944:9704:0723/151739.208:ERROR:browser_switcher_service.cc(238)
https://blog.cnrainbird.com/index.php/2020/04/21/python_windows_xia_yun_xing_selenium_ti_shi_devtools_listening_on_ws_127_0_0_1/


Python中文网教程:
https://www.cnpython.com/tags/262753

mongodb基础操作:
https://blog.csdn.net/fengbingchun/article/details/89069165

mongodbmanager可视化连接器:还有一个robo3T
https://www.mongodbmanager.com/download-mongodb-manager-free


mongodb基础操作命令:
1、查询指定集合的所有记录：
	db.centos8_table.find() 或者 db.centos8_table.find({})
	查询关键字指定的记录:
	db.centos8_table.find({"kw":kw})
2、删除指定集合的所有记录：
如果你想删除所有数据，可以使用以下方式（类似常规 SQL 的 truncate 命令）：
	db.col.remove({})   注意:remove方法需要一个query参数,删除所有给{}即可
	删除关键字指定的记录:
	db.col.remove({"kw":kw})

https://www.runoob.com/mongodb/mongodb-remove.html

mongodb常用查询命令:
https://blog.csdn.net/liqi_q/article/details/79086238

github加载慢解决办法:
https://github.com/521xueweihan/GitHub520?utm_source=gold_browser_extension

脚本之家电子书:
https://www.jb51.net/do/book.html

git reset三种模式
https://www.jianshu.com/p/c2ec5f06cf1a

免费终端连接软件MobaXterm:
https://mobaxterm.mobatek.net/download-home-edition.html

在民企使用vdi办公的同事使用下面的登录方式：
IE浏览器或safari浏览器访问下面地址：
地址一：webagent.sangfor.net.cn/ssl/mqkjyvdc.php
地址二：webagent.sangfor.net/ssl/mqkjyvdc.php
账号密码为办公VDI（200.200.8.80）的账号密码（账号默认为工号，忘记密码的同事可以联系its重置）
收起

智齿客服开发文档:
http://www.sobot.com/developer/%E5%BC%80%E6%94%BE%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%8D%95%E7%B3%BB%E7%BB%9F/

app后端设计:
https://blog.csdn.net/newjueqi/article/details/19003775

iteye网站:
https://www.iteye.com/magazines/130

前端设计资源网站:
https://zhuanlan.zhihu.com/p/115949816

https://www.freesion.com/article/4140230558/

俄罗斯搜索引擎:
yandex浏览器

解决github访问慢的问题:
https://zhuanlan.zhihu.com/p/93436925
140.82.113.3	github.com
199.232.69.194	github.global.ssl.fastly.net

github无法加载图片:
https://blog.csdn.net/qq_38232598/article/details/91346392

go依赖包代理:
https://www.goproxy.io/zh/

golang 安装一个项目下的所有依赖:
https://blog.csdn.net/weixin_34319640/article/details/94330725

go依赖工具:
https://github.com/gpmgo/gopm

windows10搭建go语言开发环境:
https://www.cnblogs.com/jiangson/p/12022288.html

https://golang.google.cn/doc/install?download=go1.14.6.windows-amd64.msi

goland配置:
http://www.coder55.com/article/1233

go钱包项目:
https://github.com/mining-pool/not-only-mining-pool

https://www.cnblogs.com/zlslch/p/6860229.html

ubuntu中root账户的密码:911611

数据库导入导出操作:
https://www.cnblogs.com/withfeel/p/10796633.html

关于Python异常的最好的讲解:
https://blog.csdn.net/zong596568821xp/article/details/78180229?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-1-78180229.nonecase

redis服务设置为开机自启动:
https://www.cnblogs.com/songjilong/p/12580755.html

vim /etc/init.d/redis
就是创建一个redis的脚本,授权可执行,类似于windows中的.exe文件,开机自动执行.

设置后,重启命令:
/etc/init.d/redis restart 或者
service redis restart

mongodb设置开机自启动:
https://www.cnblogs.com/jifeng/p/7844201.html

celery设置开机自启动:
https://www.cnblogs.com/Ting-light/p/9948201.html
注意看报错::::自己进行授权操作.

【敌后武功团纪念文章】20140716 你不能不知道的iOS开发75种秘密武器:
https://zhuanlan.zhihu.com/p/19802486

SHA256:O4XUlL2xtLJN28j6yv2OjXikSDhhuC1IPBLd0EvA+ns

celery开机自启动配置及如何编写celery部分的app:
https://www.xz577.com/j/39845.html

https://pythonheidong.com/blog/article/182147/

区块链革命 PDF 高清版下载:
https://www.xz577.com/e/25265.html

硬链接与软链接:
https://blog.csdn.net/qq_28897525/article/details/80657465

git分支合并:
本地的分支合并的时候,一定是主分支去合并子分支, 比如 是 git checkout master,
切换到master分支,然后在master分支上面执行 git merge 1.0.0/feature/lb-fix-no-upload-bug,
就是master把 1.0.0/feature/lb-fix-no-upload-bug 分支合并了.


celery守护进程启动模式:
https://docs.celeryproject.org/en/latest/userguide/daemonizing.html
https://github.com/celery/celery/blob/master/extra/generic-init.d/celeryd

Django中支持restful风格的框架:
tastypie和DRF
http://tastypieapi.org/
https://django-tastypie.readthedocs.io/en/latest/
odoogithub地址:
https://github.com/odoo/odoo
关于odoo的话题:
https://www.zhihu.com/topic/19718907/newest
国内企业:华炎魔方
https://www.steedos.com/company/about-us/
苏州欧度:
http://oudu.me/
java web学习网站:
https://how2j.cn/
sanic框架介绍:	
https://github.com/howie6879/Sanic-For-Pythoneer

优秀的项目:gitter
https://gitter.im/?utm_source=left-menu-logo
https://irc.gitter.im/
https://gitter.im/login

机器学习算法:
https://github.com/guofei9987/scikit-opt?utm_source=gold_browser_extension
Python实现的算法:
git@github.com:TheAlgorithms/Python.git

myBase Desktop 是一款用于分类存储管理任意格式资料的小型个人数据库软件:
http://www.wjjsoft.com/mybase_cn.html
破解教程:
http://www.32r.com/soft/39166.html
个人知识库搭建教程:
https://www.cnblogs.com/d2zs/p/12095889.html
http://www.eryajf.net/1040.html


Python 常见文件格式 .py .pyc .pyw .pyo .pyd 之间的主要区别:
http://forum.digitser.cn/thread-1758-1-1.html

Sublime Text3 添加右键快捷方式:
https://www.jb51.net/article/130391.htm
django + apache 项目部署:
https://www.cnblogs.com/guishenyouhuo/p/10140907.html

前端资料集合网站:
https://jijian.link/

爬虫链接:
https://catalog.redhat.com/hardware/servers/search

pycharm-monokai主题配色:
https://github.com/simoncos/pycharm-monokai

XPath Helper使用:
快捷键CTRL+SHIFT+X开启XPath Helper插件；
长按CTRL+SHIFT，鼠标指向需提取的段落，按X开启或关闭提取，提取到的段落会变为黄色。

爬虫库:ghost
https://blog.51cto.com/rfyiamcool/1287810

阿里云镜像站:
https://developer.aliyun.com/mirror/

windows更换pypi源:
https://blog.csdn.net/Adam309050449/article/details/106742678

ghost说明文档:
https://ghost-py.readthedocs.io/en/latest/#

有意思的博客:
http://zengwu.com.cn/
https://www.jb51.net/article/179782.htm

https://wiki.qt.io/Qt_for_Python#PySide.QtWebKit.PySide.QtWebKit.QWebView.url

Python模拟浏览器加载资源:
https://www.cnblogs.com/maseng/p/3578553.html

http://jeanphix.me/Ghost.py/#quick-start
http://www.aichengxu.com/article/Python/10774_15.html

去爬取这个网站的视频试试:
https://itvideo.download/

B站UP主:
https://blog.csdn.net/sinat_33921105/article/details/105401654?utm_medium=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-5.channel_param_right&depth_1-utm_source=distribute.pc_relevant_right.none-task-blog-BlogCommendFromMachineLearnPai2-5.channel_param_right

https://www.itsvse.com/

https://www.cnblogs.com/yoyoketang/p/6719717.html

jsonpath:
https://www.cnblogs.com/yoyoketang/p/13216829.html

脚本之家python设计模式:
https://www.jb51.net/article/87081.htm

chrome插件下载:
https://www.chromefor.com/down/?wp_file=bkhaagjahfmjljalopjnoealnfndnagc/octotree_v2.4.6.crx&tdd=1597735052

python异步编程:
https://blog.csdn.net/lu8000/article/details/45025987?utm_medium=distribute.pc_relevant_download.none-task-blog-blogcommendfrombaidu-1.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-blogcommendfrombaidu-1.nonecas

http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html

推荐系统框架:
https://blog.csdn.net/shenziheng1/article/details/89434138?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

https://blog.csdn.net/LIHUINIHAO/article/details/40614179?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param


吾爱破解网:
账户:huangzifei
密码:Libin9116118*
注册邮箱:bngzifei@163.com

推荐算法视频:
https://blog.csdn.net/weixin_33922670/article/details/92457203

人工智能教程:
https://www.captainbed.net/u013421629/

优秀的博客:
https://v3u.cn/a_id_102

多去知乎看看有意思的python库:
https://www.zhihu.com/question/24590883
做一个搜集

DevOps:
https://zhuanlan.zhihu.com/p/95309012

对比工具:
https://www.beyondcompare.cc/jiqiao/bc-ghtd.html

得研究一下 Python的数据分析的三个库的使用方法,尤其是涉及到表格的操作.

数据分析-Pyecharts库:
https://pyecharts.org/#/
完整介绍:
https://pyecharts.org/#/zh-cn/intro
BI文档:
https://help.finebi.com/doc-view-203.html

chrome安装jsonview插件:
https://www.cnblogs.com/songyanan/p/9224347.html

chrome安装SwitchyOmega插件:
https://github.com/FelisCatus/SwitchyOmega/releases

常用网站收集:
https://www.cnblogs.com/unleashed/p/13587790.html

pypi账户:zifei
用户名:zifeiyushui8
bngzifei@gmail.com
密码:huangxiba8*

上传至pypi
twine upload dist/*

打包上传pypi步骤:
https://www.cnblogs.com/felixwang2/p/9815030.html
https://zhuanlan.zhihu.com/p/37987613
https://www.cnblogs.com/langqi250/p/12206143.html
https://blog.konghy.cn/2018/04/29/setup-dot-py/
https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi

Python项目打包成wheel笔记:
https://blog.csdn.net/T_NULL/article/details/89967641

优质博客:
https://thief.one/2017/11/08/1/

相对路径通常在表示图片、网页等位置时需要用到，相比使用绝对路径更不容易出错。
如果图片与.md文件在同一目录下，那么采用相对路径方式表示

![avatar](buildWebsites.jpg)
其中avatar表示图片未正常加载时所显示的内容，buildWebsites.jpg为文件名

Typora 设置图片保存相对路径
https://blog.csdn.net/fantasic_van/article/details/90762627?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

IT屋视频下载:
https://www.it1352.com/VideoTutorial/Index

'gbk' codec can‘t decode byte 0x80 in position 27: illegal multibyte sequenc  解决办法:
https://blog.csdn.net/qq_43802454/article/details/108113076


打包步骤:
1、python setup.py check
2、python setup.py sdist    wheel 格式的: python setup.py bdist_wheel
3、twine upload dist/*
4、输入账户: zifeiyushui8
5、输入密码

python 列表中查询指定元素:
list.count(指定元素),如果返回值0,说明没有查找到,如果返回值不为零,就是列表中该元素出现的次数

django orm 中的update_or_create方法使用:
https://blog.csdn.net/weixin_34395205/article/details/93589599

django事务原子操作:
https://www.cnblogs.com/thomson-fred/p/10198528.html

json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) —— 读取文件的坑:
https://blog.csdn.net/longzhinuhou/article/details/86634949

shell脚本遇到问题"$'\r': command not found":
shell脚本写得一切正常，但是一执行就报错:
line: XXX "$'\r': command not found"

先 yum install dos2unix 安装 dos2unix工具,
问题原因：文件格式问题(虽然在window和linux上选择的都是UTF-8，然而并没有用)，因为我是直接复制了一个别的文件，然后在那个基础上改的。
解决方法：dos2unix XXX.sh

然后执行脚本，问题解决。

python3中zipfile模块的常用方法:
https://www.cnblogs.com/ManyQian/p/9193199.html

os.system与os.popen区别:
https://www.cnblogs.com/jefree/p/4461979.html

输出内容需要有返回的:
output = os.popen('cat /proc/cpuinfo')
output.read()

只是返回一个状态码:
ret = os.system('cat /proc/cpuinfo')
ret为0,命令执行成功,否则非零执行失败

如果既要状态码,又要输出内容,则使用commands模块:
(status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
status 为0,说明执行成功,output为输出内容.

os.path.dirname(path)	返回文件路径
os.path.basename(path)	返回文件名

字符串首字母大写: STR.title()

Python有用的模块简介:
https://www.jb51.net/article/178716.htm

CMS内容管理系统

python将py编译成so方法
https://blog.csdn.net/qq_20154743/article/details/77891572

RESTful:
https://www.cnblogs.com/alex3714/articles/6808013.html

Fabric是一个python的远程执行shell的库，同时它也是一个命令行工具:
https://www.cnblogs.com/welisit/p/10995357.html

https://www.vmware.com/support/services/skyline.html?src=so_5703fb3d92c20&cid=70134000001M5td

一个神奇的网站:
https://github.com/TwoWater/Python/blob/master/Res/%E8%87%AA%E5%B7%B1%E6%90%AD%E5%BB%BAss:ssr%E6%9C%8D%E5%8A%A1%E5%99%A8.md

supervisor进程监控进程，发现进程没了重新拉起。
kill -TERM命令杀进程模拟.

DRF详细文档:
https://www.django-rest-framework.org/

修改要点:
自动创建目录,使用相对路径
同步的变成异步的

Python中文数据结构
https://github.com/PegasusWang/python_data_structures_and_algorithms
Python网络编程:
https://www.zhihu.com/question/42390552
算法设计:
https://www.zhihu.com/question/21628833/answer/370073009

164.50976610183716
179.6142578125

1093.7744140625 同步
641.87109375 协程异步  773.107421875

异步爬虫Pyppeteer:
http://blog.itpub.net/69923331/viewspace-2648397/
https://zhuanlan.zhihu.com/p/76237595
https://miyakogi.github.io/pyppeteer/
https://www.cnblogs.com/Summer-skr--blog/p/12020207.html

NB爬虫项目:
https://github.com/xxNB/crawl

aiomultiprocess:协程与多进程结合:
https://www.youtube.com/watch?v=0kXaLh8Fz3k
https://cuiqingcai.com/6160.html

pyecharts丨页面布局工具——Page 和 Grid
https://www.it610.com/article/1296632175210340352.htm

数据结构和算法 Python和C++语言描述
数据结构和算法 Python和C++语言描述作者：(美) 戴维·M.瑞德(David M. Reed) 约翰·策勒(John Ze)

curl用法:
http://www.ruanyifeng.com/blog/2019/09/curl-reference.html

牛人的博客-迅速提升英文阅读水平:
https://www.cnblogs.com/best/p/6589908.html

Python部署:
https://www.deploypython.com/

Python高级用法之消息队列zmq:
https://blog.csdn.net/biheyu828/article/details/88932826

Pycharm历史版本下载:
https://www.jetbrains.com/pycharm/download/other.html

sublime插件报错Anaconda.xxx错误:
https://blog.csdn.net/qq_27755877/article/details/104833771

http://c.biancheng.net/view/6376.html

https://pan.baidu.com/s/1ItKPWGygd4gKVC5iHnlT7A
密码:cagb

sanic文档:
https://howie6879.gitbooks.io/sanic/content/
sanic扩展:
https://sanic.readthedocs.io/en/latest/sanic/examples.html

nginx+uwsgi或nginx+python中manage部署多个网站:
https://blog.csdn.net/qq_33196814/article/details/86307939

复习指南:
廖雪峰教程:
https://www.liaoxuefeng.com/wiki/1016959663602400/1017631469467456

码农之家电子书下载:
https://www.xz577.com/
Python编程导论 PDF 中文第2版

杀掉所有进程:
sudo pkill -f uwsgi -9

撤销当前提交至缓存区的所有文件:
git restore --staged ./

java 资料下载:
https://www.seotest.cn/jishu/31878.html

百度云搜索:
http://lqkweb.com/
https://www.torrent.org.cn/t-44199

Python 数据结构与算法-中文教程:
https://github.com/PegasusWang/python_data_structures_and_algorithms
https://zhuanlan.zhihu.com/p/36038003

ipdb 调试:
https://zhuanlan.zhihu.com/p/36810978

南华大学:
http://www.nhu.edu.tw/main.htm

疯狂Python讲义
https://www.xz577.com/e/786.html

google编程规范:
http://google.github.io/styleguide/pyguide.html

骆昊:一百天Python大师
https://www.jb51.net/books/671456.html

Git同步更新操作GitHub和码云仓库上面的代码:
https://www.cnblogs.com/zhengqing/p/11218529.html
https://gitee.com
bngzifei@gmail.com
huangxiba888*

容器云运维实战：Docker与Kubernetes集群 PDF 影印版 下载:
https://www.xz577.com/e/21473.html

找一找这种项目
Python玩转物联网--《物联网Python开发实战》

物联网项目:
https://edu.csdn.net/course/detail/22983?utm_medium=distribute.pc_relevant.none-task-course-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-course-BlogCommendFromMachineLearnPai2-1.channel_param

Python twisted 异步网络框架

Python个人笔记:
https://github.com/daacheng/PythonBasic

USERNAME = "rd.sangfor@gmail.com"
PASSWORD = "@Sangfor123"

下载:
https://www.xz577.com/e/21486.html
https://www.xz577.com/e/21453.html
https://www.xz577.com/e/21487.html
https://www.xz577.com/e/24993.html


centos7 开启telnet远程连接配置:
https://www.cnblogs.com/nmap/p/10779658.html
https://www.cnblogs.com/Ankh-L/p/10120355.html
https://www.cnblogs.com/missinglihua/articles/7234667.html

重新安装openssh和openssl(直接从解压步骤开始)
https://www.cnblogs.com/v-fan/p/11026895.html

和这个链接(从里面找到下载openssh和openssl的下载链接即可):
https://www.cnblogs.com/nmap/p/10779658.html

注意是这个命令,不是其他的
telnet 127.0.0.1 22


查看端口开放:
https://www.cnblogs.com/heqiuyong/p/10460150.html


关注这几个问题:
迭代器生成器
深浅拷贝
GIL锁
垃圾回收
三次握手四次挥手
访问www.baidu.com的步骤
装饰器
单例

码农之家Python书籍推荐:
https://www.xz577.com/e/301.html

Erlang 语言:
https://www.xz577.com/e/40233.html

面试经历:
https://juejin.im/post/6875244112317317128?utm_source=gold_browser_extension

Python 内置数据类型的底层实现原理?比如set list 字典

自己设计实现一个set

最近学了啥新技术,说说

后端最拿手的技术点:

RPC

IO多路复用

RabbitMQ

Es Redis MongoDB存储的

DNS 服务公司如何盈利:
https://www.zhihu.com/question/22753490

Python 内存溢出的检测方式？

自行设计一个异步任务的消息队列

3个方向：
爬虫
数据分析 
学个新的语言

抓基础，重视基础
高度自我驱动


厘米脚印

简聊，瀑布，纷云还有那什么BearyChat等等

工单系统的设计

还有：字要写好，命名要规范

数据分析 R语言  Julia语言 MatLab
https://zhuanlan.zhihu.com/p/45079863

竟然还有机器学习和人工智能啥的

也不知道是啥:
https://quantecon.org/

元类

红黑树
B+数
快速查找

可以这样,在家里新建一个文件去存家里搜索的资料,在这里就在本文件下进行存储

apache服务器和nginx服务器的区别

就从爬虫入手吧

学习一点前端

Python 实现的设计模式:
https://github.com/wklken/py-patterns

Redis是如何持久化存储的?

开发部署应用之类的不需要去找,需要去搜集 涉及到原理之类的问答题

go资源:
https://zhuanlan.zhihu.com/p/25493806

https://github.com/wonderfo/wonderfogo/wiki

https://www.lylinux.net/archives.html


国庆期间就整理这些问题就行.

数据结构与算法
痛定思痛:shell编程

perl:
https://www.xz577.com/e/40765.html

sambda服务器的搭建

linux中的grep awk sed 三剑客的使用？


https://www.xz577.com/e/325.html
物理学高效计算:
https://www.xz577.com/e/359.html

得打开思维,不能局限在这一小块上面了

直播项目:
https://github.com/parzulpan/real-live

es 数据库: 本质上是一个分布式数据库
http://www.ruanyifeng.com/blog/2017/08/elasticsearch.html

CSS布局教程:
http://www.ruanyifeng.com/blog/2020/08/five-css-layouts-in-one-line.html

git-cherry-pick教程:
http://www.ruanyifeng.com/blog/2020/04/git-cherry-pick.html

ElasticSearch PDF 电子书下载:
https://www.xz577.com/e/40476.html
https://www.xz577.com/e/224.html

电子书网站下载:
https://www.52doc.com/

git 命令在线学习:
https://oschina.gitee.io/learn-git-branching/

Python数据结构与算法:
https://www.zhihu.com/question/19889750

一个神奇的电子书下载网站:
https://474b.com/file/18113597-321523035

北大地空教学课程:
http://gis4g.pku.edu.cn/course/pythonds/

gitbooks书籍:
http://ddrv.cn/docs/pythonalgorithm/

纸质笔记:
http://ddrv.cn/docs/pythonnotes/

十大经典排序算法:
http://ddrv.cn/docs/SortingAlgorithm/

招财猫咪网:
PDF电子书下载

存储、调度、微服务

关于计算机网络:
https://www.zhihu.com/question/30230102

刘欣老师的《码农翻身》


学个东西需要有个层次、递进的过程，不能一蹴而就。


计算机网络的学习:
https://www.xz577.com/e/60140.html
https://www.zhihu.com/question/30230102
https://www.zhihu.com/question/22354846


文档：黄小斜精选电子书.note
百度云链接全部都失效了:
链接：http://note.youdao.com/noteshare?id=48ae33f0d07442e753c1280854efd8ea&sub=B112279B61274291A552C6BAC3282F8A

国立清华大学的课程:
http://ocw.nthu.edu.tw/ocw/index.php?page=course&cid=13&

一个在线学习网站:
https://www.academiccourses.cn/peixunban-zhuanyepeixun/Ji-Suan-Ji-Wang-Luo-Ke-Xue/

软考资料书籍:
http://club.topsage.com/thread-174979-1-1.html

数学方面:
http://club.topsage.com/forum-931-1.html

大家论坛注册:
账户:BNGFRpq
密码:Sweepaway92*

TCP/IP 下载:
http://club.topsage.com/thread-2273478-1-1.html

VScode搭建C和C++环境的图文教程
https://juejin.im/post/6879387384669503501?utm_source=gold_browser_extension

掘金浏览器插件
https://juejin.im/extension/?utm_source=juejin.im&utm_medium=Pop-ups2&utm_campaign=extension_promotion

程序员论坛:
http://www.cx1314.cn/

如何加速GitHub访问速度
https://juejin.im/post/6876715404455051272?utm_source=gold_browser_extension

聊聊 Python 数据处理全家桶(各种格式的配置文件)
https://juejin.im/post/6880821708396183566

Python 设计和历史的 27 个问题
https://mp.weixin.qq.com/s/zabIvt4dfu_rf7SmGZXqXg

Python 为什么不支持 switch 语句？
https://juejin.im/post/6881085243009433607

公众号文章:
https://mp.weixin.qq.com/s?__biz=MzUyOTk2MTcwNg==&mid=2247483899&idx=1&sn=698a0a95ad3ce3496f960a5fe181df7f&chksm=fa58467ecd2fcf6875be2289accdb33db332c13855b17ae25d7f7456925beac4eb4f7afc30c3&scene=21#wechat_redirect

面试问题集合
https://github.com/jackfrued/Python-100-Days/blob/master/%E7%95%AA%E5%A4%96%E7%AF%87/Python%E9%9D%A2%E8%AF%95%E9%A2%98%E6%B1%87%E6%80%BB.md

动态规划问题
https://blog.csdn.net/mrlevo520/article/details/75676160
https://www.zhihu.com/question/23995189
https://mp.weixin.qq.com/s/pg-IJ8rA1duIzt5hW1Cycw

markdown 中 按下 > 键即可出现书签式的那种格式

是不限语言,不限技术栈的进行开发

程序员客栈: 搜集一下有意思的项目
https://www.proginn.com/w/1290589
程序员的那些事:
https://www.pythonheidong.com/blog/article/498183/

机器学习:go语言实现
https://www.xz577.com/e/21453.html

如何学好Python
https://github.com/Yixiaohan/codeparkshare
知乎:你是如何学习Python的
https://www.zhihu.com/question/20702054
医疗区块链项目
https://gitee.com/medical-alliance/medical-blockchain
SDN技术网站
https://www.sdnlab.com/tag/SDN/
马哥教育资料
http://www.magedu.com/73198.html?Python_wenda_zhihu_xiujiang_ruhejieshipythonzhaungshiqi_/question/26930016
常用正则表达式
https://mp.weixin.qq.com/s?__biz=MzI1MTE2ODg4MA==&mid=2650069706&idx=1&sn=cd5e3c6d8f3c9fed398d8679d3e02c61&chksm=f1f76bd5c680e2c374ac4f84a6a3f8e6aaf558d0e546dfd8232d6cfebafa0c0ecafd01bddeb4&scene=21#wechat_redirect

微信公众号文章
https://mp.weixin.qq.com/s?__biz=MzI1MTE2ODg4MA==&mid=2650068864&idx=1&sn=cf066098901df92203f4ae074a5d4fee&chksm=f1f7669fc680ef8984e523aa09ed5547da653a54a5e95b19694981bea7eda12a08cc3a336e32&scene=21#wechat_redirect

grequests库
https://mp.weixin.qq.com/s?__biz=MzI1MTE2ODg4MA==&mid=2650068929&idx=1&sn=bb8126172c8c439641d117ecbeb25674&chksm=f1f766dec680efc8f56c668facec58b43c79d941d05a8d9df5bb9f459cb501c38f385867bd45&scene=21#wechat_redirect

面试心得
https://www.xz577.com/e/384.html

Axure RP8实战手册:网站和APP原型制作案例精粹 PDF 彩色影印版:
https://www.xz577.com/e/399.html

HTML 中常见的水平居中设置方式
https://www.cnblogs.com/lxlw/p/11771001.html

SDN网络指南(SDN Handbook) PDF 完整版
https://www.xz577.com/e/103096.html

OpenStack从零开始学 PDF 高清版
https://www.xz577.com/e/25266.html

OpenStack运维指南 PDF 中文版
https://www.xz577.com/e/61124.html

OpenStack高可用集群（下册） PDF 影印高清版
https://www.xz577.com/e/65851.html

微服务设计原理与架构 PDF 全书高清版
https://www.xz577.com/e/66691.html

MySQL技术精粹：架构、高级特性、性能优化与集群实战 PDF 超清版
https://www.xz577.com/e/60347.html

Python编程之美：最佳实践指南 PDF 超清完整版
https://www.xz577.com/e/47378.html

Python高手之路 PDF 第3版 链接无效了
https://www.xz577.com/e/40314.html

C语言相关书籍
https://www.xz577.com/e/103101.html
C语言核心技术
https://www.xz577.com/e/396.html

从Excel到Python:数据分析进阶指南 PDF 高清版
https://www.xz577.com/e/25090.html
Python相关电子书
https://www.xz577.com/j/25980.html

ELKstack 中文指南 5.0(三斗大著) PDF 完整版
https://www.xz577.com/e/103237.html

DRF 二手书项目
https://github.com/mtianyan/VueDjangoAntdProBookShop
同类型的在线教育网站
https://github.com/mtianyan/OnlineMooc
资产管理系统CMDB
https://github.com/open-cmdb/cmdb
运维自动化系统
https://github.com/xufqing/rest_xops
台北议员选票系统
https://github.com/FroggyTaipei/froggy-service
微博用户情感分析
https://github.com/Superbsco/weibo-analysis-system
DB monitor数据库监控平台
https://github.com/gumengkai/db_monitor
问卷调查项目
https://github.com/shanghaobo/wjcat-release
工单系统
https://github.com/itimor/one-workflow
更nb的工单
https://github.com/blackholll/loonflow
工单-工作流思路
http://loonapp.com/blog/27/

仓储管理系统
https://github.com/lihao6666/vue-django-storeManage

Python讲义资料
https://github.com/HaoZhang95/Python24
https://github.com/coco369/knowledge

Flask实现的淘票票
https://github.com/yuansuixin/Vue_Flask_taopiaopiao

golang 实验室论文
https://github.com/yangsoon/LabAC

日文奇怪的
https://github.com/kitakou0313/Otamesi
多抓鱼二手书
https://www.duozhuayu.com/books/127663015842549686?utm_medium=web&utm_source=douban

利用Python进行数据分析
https://github.com/BrambleXu/pydata-notebook

Python采坑计
https://github.com/zhanghe06/python

先学学Vue,再学学shell,再学学go
只限于会用的水平
这要求不算高

关于go的讨论:
https://www.zhihu.com/question/360929863

Gin 都比它好用

量化交易开发

怎么学习 Golang？
https://www.zhihu.com/question/23486344/answer/1204644361
https://zhuanlan.zhihu.com/p/25493806

java与c#

java转行大数据:
https://www.zhihu.com/question/297875175/answer/855717147

go开发路线图
https://github.com/Quorafind/golang-developer-roadmap-cn/blob/master/ReadMe.md

过分夸大学习难度了

最好的go学习网站:
http://www.topgoer.com/

gitbook 转成 pdf:
https://www.mapull.com/gitbook/comscore/basic/markdown.html
https://www.zhihu.com/question/24428806

自定义Github首页:
https://juejin.im/post/6884819225266323463?utm_source=gold_browser_extension

Python算法:
https://github.com/TheAlgorithms/Python?utm_source=gold_browser_extension

Git工作流介绍:
https://juejin.im/post/6885504750758920200?utm_source=gold_browser_extension

C程序设计新思维 PDF 超清第2版
https://www.xz577.com/e/427.html
python算法教程 PDF 全书影印版
https://www.xz577.com/e/55396.html
Python金融实战(严玉星) PDF 中文原版扫描版
https://www.xz577.com/e/292.html
Python编程快速上手：让繁琐工作自动化 PDF 影印完整版 未下载:
https://www.xz577.com/e/40595.html

具体下载链接:
https://www.xz577.com/j/25980.html

Python 可以这样学 未下载:
https://www.xz577.com/e/201.html

Python全栈数据工程师养成攻略 PDF 超清视频版:
https://www.xz577.com/e/325.html

golang 数据结构:
https://github.com/hunterhug/goa.c
https://goa.lenggirl.com/

c/c++学习:
https://github.com/hunterhug/cmake_example

gitbook转成pdf项目:
https://github.com/fuergaosi233/gitbook2pdf
k8s 文档:
https://kubernetes.feisky.xyz/

打造自己的出版平台:
http://self-publishing.ebookchain.org/index.html

OSError: no library called "cairo" was found 怎么解决:
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

查个问题:
操作系统提供的数据结构

weasyprint库介绍:
https://weasyprint.readthedocs.io/en/stable/install.html#windows

知乎: golang 数据结构
https://zhuanlan.zhihu.com/p/113038466

计算机电子书下载:
https://www.cnblogs.com/apachecn/p/12129061.html


问: 多线程中 thread.start() 与 thread.run() 的区别?
Python中  dict list set 三种数据结构的底层实现

漏洞:Python中获取列表中每个元素所在的位置:
https://www.jb51.net/article/164287.htm
注意不能使用list.index(), 是错误的使用场景,因为  list.index(obj) 是从列表中找出某个值第一个匹配项的索引位置
应该使用enumerate()函数

golang教程-异常处理
http://www.topgoer.com/%E5%87%BD%E6%95%B0/%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86.html

相关链接:
https://www.xz577.com/e/188.html

java系列:
https://www.xz577.com/e/293.html

Python subprocess模块功能与常见用法实例详解:
https://www.jb51.net/article/142787.htm

使用示例:
process = subprocess.Popen(cmd, 
							shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
stdout = process.stdout.read()
stderr = process.stderr.read()
code = process.poll()

京东平台数字化运营
https://www.xz577.com/e/1026.html

linux 系列未下载:
https://www.xz577.com/e/103366.html
https://www.xz577.com/e/25088.html
https://www.xz577.com/e/40783.html
未下载:
https://www.xz577.com/e/333.html
下载链接:
https://www.xz577.com/e/513.html
代码管理:
https://www.xz577.com/e/338.html
redis cookbook:
https://www.xz577.com/e/419.html

在线协调工作:
https://docs.mattermost.com/help/settings/theme-colors.html#standard-themes

golang 设计模式
https://github.com/senghoo/golang-design-pattern
golang 开源项目
https://github.com/hackstoic/golang-open-source-projects
golang教程链接
https://github.com/yangwenmai/learning-golang
千峰golang100天大师
https://github.com/rubyhan1314/Golang-100-Days

渗透测试方向博客链接
https://www.xmanblog.net/web-security-interview/
json 文件:也是配置文件的一种格式 对应关系的那种和ini格式的是一样的.

优质博客
https://blog.zxysilent.com/

解决国内go get 超时问题:
https://www.sunzhongwei.com/problem-of-domestic-go-get-unable-to-download?from=sidebar_new
十分钟了解golang:
https://learnxinyminutes.com/docs/zh-cn/go-cn/

谷歌翻译使用:无需翻墙
https://translate.google.cn/#view=home&op=translate&sl=zh-CN&tl=en&text=%E5%A4%87%E4%BB%BDmultipath%E9%85%8D%E7%BD%AE%E6%A3%80%E6%B5%8B

地鼠文档:
http://wen.topgoer.com/

<<UNIX网络编程卷1：套接字联网API>>

优质博客:
https://www.cnblogs.com/zsy/p/5370052.html

Go 语言中如何开源自己写的包给别人用?
https://www.jianshu.com/p/56c11a02b84b

个人博客 go编程时光:
http://golang.iswbm.com/


.gitkeep 作用
大家可能在很多的开源项目中都看到过.gitkeep这个文件，文件内没有任何内容，一个空空的文件。
那么，它的作用到底是什么呢？
这要从git不允许追踪(track)或者说提交一个空的文件夹说起，git本身是不允许提交一个空文件夹的，
所有就有了.gitkeep的存在，可以把它看作是一个占位符，当然了，你也可以使用 .nofile或者其他的占位符，自行决定。

http://wen.topgoer.com/docs/gomianshiti/mian15

shell脚本项目
https://github.com/chen-shang/baseshell

学基本数据类型,就是学语言设计者设计这些数据结构的思想.

golang中iota的使用:
https://studygolang.com/articles/2192

项目选择:日志搜集系统

https://github.com/fqyshelly/interesting-python

https://tonybai.com/2015/01/13/a-hole-about-variable-scope-in-golang/
可视化在线算法:
https://www.cs.usfca.edu/~galles/visualization/Algorithms.html 

【】
Python List remove()方法
Python 列表 Python 列表

描述
remove() 函数用于移除列表中某个值的第一个匹配项。  注意是第一个,不是每一个,所以要注意判断条件

注意下面 这种 check_items  动态的用法,是错误的,
            for index, item in enumerate(check_items):
                if item["module"] == "vs_cold_upgrade_check":
                    check_items.pop(index)
