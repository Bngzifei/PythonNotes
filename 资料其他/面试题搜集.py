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