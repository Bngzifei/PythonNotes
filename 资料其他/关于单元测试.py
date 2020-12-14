单元测试之mock:
	为单元测试的初始设置准备的其他代码资源.
	创建mock模拟这些代码资源.
	mock可以让我们模拟那些在单元测试中不可用/太笨重的资源

python中创建mock是通过Mock模块完成的.

测试准备:   1.测试对象(可以是一个方法,模块,或者类).可以返回一个结果,也可以不返回.但是可以根据数据/数据内部状态产生错误或者异常

		   2.测试用例(可以单独运行,也可以作为套件的一部分)为了测试对象准备的,也可以是测试对象所需要的任意数据或者资源.

好处:
有些时候测试资源不可用,或者不适合.(也许这个资源正在和测试对象并行开发中,或者并不完整/不稳定/不可靠)

mock提供给测试对象一套和测试资源相同的方法接口.但是更容易创建和管理.它可以向测试对象提供和真实的测试资源
相同的方法接口.可以提供确定的接口


Mock类有四套方法，分别为构造器方法、断言方法、管理方法、统计方法。


mock接口:
测试真实支付的场景下,如果不想去花自己的钱,那么需要自己写一个支付接口来模拟第三方支付，
反正支付接口就是你把金额传过来，然后扣你账户的钱，返回支付成功就可以了。
等到和第三方支付平台联调的时候再去用真实接口进行支付。

就是自己开发的时候需要进行测试,但是协同开发的情况下,别人的接口你需要进行调用,在别人还没写好的接口的时候,你先
自己写一个假的接口,用来测试自己的功能是否是正确的.这个就是mock的作用和意义


涉及到的内容:
1.unittest单元测试
2.pdb调试
3.mock测试
4.phoenix框架
5.底层的反射
6.restful API接口
7.fixtures 库 https://pypi.org/project/fixtures/
8.wsgi 协议的源码
9.断言的实际使用
10.oslo 库的使用
11.curl是个啥?
12.rpc 微服务的概念
13.装饰器工厂函数/类装饰器
11.__call__方法
12.set集合的交差并补.交差并补的方法使用.
13.mq现消息中间件:rabbit
14.flake8编码规范  python -m pip install flake8 安装. pep8和flake8之间的关系
15.python2和python3兼容的six模块
16.content_types = [v for h, v in headers if h == 'Content-Type']  列表推导式
17.oslo库
18.OpenStack 还是得看
19.shell 脚本语言
20.sanitize()  # 消毒/清除
21.句柄
22.rpdb
23.Paste
24.greenlet/eventlet/gevent  链接:https://zhu327.github.io/2016/06/16/python%E5%8D%8F%E7%A8%8B/
25.def iteritems(d: Mapping[_K, _V]) -> typing.Iterator[Tuple[_K, _V]]: ...  这是啥?
26.def add_metaclass(metaclass: type) -> Callable[[_T], _T]: ...  这又是啥?
27.paste deploy
28. BSON
29. real signature unknown; restored from __doc__   这句话的真正意思是啥?
30.C语言中的结构体,指针概念
31.allure
32.importlib.import_module
34.对文件的操作部分.
35.打桩函数
36.Hunter
是一个灵活的代码跟踪工具包，不是用于测量覆盖范围，而是用于调试，记录，检查和其他恶意目的。它有一个简单的Python API，一个方便的终端API和一个附加到进程的CLI工具。
37.异常的多层拦截机制


原来这里说的服务就是服务器的意思.服务就是之前的项目程序,就是一个web服务器

kill -s SIGUSR1 15972  向服务进程发送运行时调试信号

Debug mode is: True  服务进程开启调试模式

external libraries:外部库





RPC:(Remote Procedure Call) --意思是远程过程调用.
是一种通过网络从远程计算机程序程序上请求服务,而不需要了解底层网络技术的协议.
RPC协议假定某些传输协议的存在,比如TCP或UDP,为通信程序之间携带信息数据.在OSI网络通信
模型中,RPC跨越了传输层和应用层.RPC使得开发包括网络分布式多程序在内的应用程序更加容易.


RPC采用 客户机/服务器 模式.
请求程序就是一个客户机,而服务提供程序就是一个服务器.首先,客户机调用进程发送一个有进程参数的调用信息到服务进程,然后等待应答信息.在服务器端,进程保持睡眠状态直到调用信息到达为止.
当一个调用信息到达,服务器获得进程参数,计算结果,发送答复信息,然后等待下一个调用信息,最后,客户端调用进程接收答复信息,获得进程结果,然后调用执行继续进行.


为什么要用RPC?
    1.>可以做到分布式,现代化的微服务
    2.>部署灵活
    3.>解耦服务
    4.>扩展性强


RPC 的目的是让你在本地调用远程服务器的一种方式.对你来说这个调用是透明的,你并不知道这个调用的方法是部署在哪里.通过RPC能够解耦服务,这才是使用RPC的真正目的.

RPC结构: client-server结构,调用方是client,远程被调用方是server. 其实双方的地位一样,看谁调用谁而已.

RPC工作原理:

1.>调用客户端句柄,执行传送参数   句柄(就是文件描述符)  客户端:就是本地主机上面的一个应用程序,类似mysql的shell终端
2.>调用本地系统内核发送网络消息  本地系统内核:就是一台具体的主机,操作系统是linux或unix或windows.操作系统内核中的发送网络消息的模块进行发送发送消息.
3.>消息传送到远程主机
4.>服务器句柄得到消息并取出参数
5.>执行远程调用过程
6.>执行的调用过程将结果返回给服务器句柄
7.>服务器句柄返回结果,调用远程系统内核发送网络消息
8.>消息传回本地主机
9.>客户端句柄由内核接收消息
10.>客户端接收句柄返回的数据


RPC框架有哪些?

一般主流框架都实现了跨平台跨语言的C/S RPC调用

dubbo,主流配合hessian协议使用,duboo/hessian.
DUBBO是一个分布式服务框架，致力于提供高性能和透明化的RPC远程服务调用方案，是阿里巴巴SOA服务化治理方案的核心框架，每天为2,000+个服务提供3,000,000,000+次访问量支持，
并被广泛应用于阿里巴巴集团的各成员站点。

thrift,Apache Thrift software framework.


hprose,High Performance Remote Object Service Engine

RPC-HTTP:

HTTP本质来讲是RPC调用的一种实现方式.换种方式说,RPC客户端可以通过HTTP连接到RPC服务端程序执行RPC(远程过程调用)

把RPC比作交通工具,那么HTTP就是相当于汽车


RPC 框架的优点:
    RPC框架一般使用长链接，不必每次通信都要3次握手，减少网络开销

    RPC框架一般都有注册中心，有丰富的监控管理

    发布、下线接口、动态扩展等，对调用方来说是无感知、统一化的操作

    协议私密，安全性较高

    rpc 协议更简单内容更小，效率更高

    服务化架构、服务化治理，RPC框架是一个强力的支撑.

RPC-REST
    REST 是定义http接口调用的一种方式，REST 也可以说是RPC调用的实现方式。




那RPC最大的优点，或者说它相比简单的HTTP接口，它的优势、更适合它的业务场景是怎样呢？简单的HTTP又哪里不足，哪些场景明显不太适合呢？

答:
    http接口是在接口不多、系统与系统交互较少的情况下，解决信息孤岛初期常使用的一种通信手段；优点就是简单、直接、开发方便。利用现成的http协议进行传输。
    但是如果是一个大型的网站，内部子系统较多、接口非常多的情况下，RPC框架的好处就显示出来了，首先就是长链接，不必每次通信都要像http一样去3次握手什么的，减少了网络开销；
    其次就是RPC框架一般都有注册中心，有丰富的监控管理、发布、下线接口、动态扩展等，对调用方来说是无感知、统一化的操作。
    第三个来说就是安全性。最后就是最近流行的服务化架构、服务化治理，RPC框架是一个强力的支撑。

    RPC:远程过程调用。RPC的核心并不在于使用什么协议。RPC的目的是让你在本地调用远程（就是其他机器上面）的方法，而对你来说这个调用是透明的，你并不知道这个调用的方法是部署哪里。
    通过RPC能解耦服务，这才是使用RPC的真正目的。RPC的原理主要用到了动态代理模式，至于http协议，只是传输协议而已。简单的实现可以参考spring remoting，复杂的实现可以参考dubbo。


所以,以后说写一个服务就是写一个服务端的应用app

WSGI服务器介绍:
https://www.cnblogs.com/jl-bai/p/7724772.html

i18n（其来源是英文单词 internationalization的首末字符i和n，18为中间的字符数）是“国际化”的简称。
通常与i18n相关的还有L10n（“本地化”的简称）。

从远端进行分支回退:
git reset --hard origin/远端的分支

图示当前分支历史:
git show-branch

撤销提交dfb02e6e4f2f7b573337763e5c0013802e392818:
git revert dfb02e6e4f2f7b573337763e5c0013802e392818

合并分支:
git merge 合并的目标分支名

比如:git merge master 就是把当前分支合并到master主分支上面
git merge 最简洁用法:
https://blog.csdn.net/zl1zl2zl3/article/details/94019526

修改分支名:

1.git branch -m 旧的分支名 新的分支名(新建新分支并切换到新分支)
2.git push -u origin 新分支(将新分支推送到远程)
3.git push -u origin :旧分支(删除远程的旧分支)

合并多次提交:

git rebase -i 起始点(注意不是自己开始的那个,是其他人开始的那个节点,合并的时候并不包括这个节点)
接着按s合并多次提交commit
接着按#注释掉提交记录说明
最后 git push origin 你远端对应的分支 -f
这样就可以了.

推送到远端:
git push origin 分支名 -f

基于主分支进行拉取代码:
git pull --rebase origin 5.8.7R2/issue/add-xxxx  

本地合并的就是 git merge 被合并的分支,然后就git push origin 当前所在的分支.

pytest自动化测试库插件说明文档:
https://docs.pytest.org/en/latest/reference.html#hook-reference

sublime 上下移动一行的快捷键: ctrl + shift + 上箭头/下箭头

杀掉pytest进程的命令:
ps aux | grep 'python -m pytest' | awk '{print $2}' | xargs kill -9

sublime 全部选中一起修改: alt + ctrl + 下箭头 选中,然后按ctrl + d

有时候会想把github上的文件删除，但是本地仓库里的文件想保留下来该怎么办，只要用三条命令就能完成了

git rm --cached filename/-r directory
git commit "xxxx"
git push

git 使用在一个分支写完之后,可以先在这个分支的基础上新建一个分支,然后再推送,然后再去远端提合并请求

9..gz
解压1：gunzip FileName.gz
解压2：gzip -d FileName.gz
压缩：gzip FileName
.tar.gz
解压：tar zxvf FileName.tar.gz
压缩：tar zcvf FileName.tar.gz DirName
解压至指定目录:  tar zxvf FileName.tar.gz -C ./DirName

10. 打一个发行包,直接上传至pypi,可以使用 pip install 安装包名字 这个命令安装的
python setup.py sdist

11. python assert断言是声明布尔值必须为真的判定，如果发生异常就说明表达式为假。
可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常

12. 删除远程分支:
git push origin --delete dev

反射:
https://www.cnblogs.com/cenyu/p/5713686.html

cron 表达式链接 : https://www.cnblogs.com/javahr/p/8318728.html

.pyi是个啥?

去看下这个链接
https://www.cnblogs.com/lwp-king666/p/8331508.html

git stash 操作

git stash list部分

然后你就可以 执行 git stash clear  :注意这是清空你所有的内容

$ git stash drop stash@{0}  这是删除第一个队列

git reset --hard 和 git reset --soft区别
https://blog.csdn.net/yangfengjueqi/article/details/61668381

删除远程分支:
使用命令 git push origin --delete Chapater6   可以删除远程分支Chapater6

判断一个对象是不是一个函数: https://blog.csdn.net/yiifaa/article/details/78046331

批量杀掉进程:
ps -aux|grep "pytest"|awk '{print "kill -9 "$2}'|sh

这里是批量杀死进程名包含xxx的进程，记录做个备忘:
ps aux|grep pytest|awk '{print $2}'|xargs kill -9

绝对路径:
[\u@\h \w]\$

相对路径:
[\u@\h \w]\$


配置git多远端:
git remote add acloud xxx(url)
git pull acloud
git push acloud xxx(branch)


删除远端分支:
git branch -r -d origin/branch-name
git push origin :branch-name

git stash pop  冲突解决
git stash show -p | git apply && git stash drop


解决在Git 命令输出中的中文文件名显示问题。
git config --global core.quotepath false


提交代码时，rebase了两次，本地代码丢失了，吓得我差点跳起来。解决方法如下：
1、执行命令：

git reflog

2、用reset (Suppose the old commit was HEAD@{5} in the ref log)

git reset --hard HEAD@{7}
亲测有效！解决了～解决了～

scp命令:
scp username@servername:/path/filename /local/path

通过PYTHON-DOCX给WORD文档中的指定位置添加表格:
https://www.yinyubo.cn/?p=352

golang中切片去重

lsof -i 8090 查看端口占用