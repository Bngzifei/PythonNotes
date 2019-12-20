# coding:utf-8

博客地址:
https://www.cnblogs.com/jl-bai/p/7724772.html

python web application/framework:

application/framework 端必须定义一个callable object ,callable object
可以是下面三者之一:

1.>function,method
2.>class
3.>instance with a __call__ method

callable object 必须满足以下两个条件:
1.>接受两个参数:字典(environ),回调函数(start_response,返回HTTP status ,headers 给web server)
2.>返回一个可迭代的值


示例:
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['HELLO WORLD!']

class ApplicationClass(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK', [('Content-type', 'text/plain')])
        yield "Hello world!n"



1.environ 和 start_response 由 http server 提供并实现
2.environ 变量是包含了环境信息的字典
3.Application 内部在返回前调用 start_response
4.start_response也是一个 callable，接受两个必须的参数，status（HTTP状态）和 response_headers（响应消息的头）
5.可调用对象要返回一个值，这个值是可迭代的

服务器接口端:

服务器端主要专注HTTP层面的业务,重点是接收HTTP请求和提供并发.

每当收到HTTP请求,服务器接口端就必须调用callable object

接收HTTP请求,但是不关心HTTP url,HTTP method等

为environ提供必要的参数.实现一个回调函数 start response ,并传给callable object

调用callable object


middleware 中间件:

middleware 处于服务层和应用接口层之间,每个middleware实现不同的功能.我们通常根据需求选择相应的middleware并组合起来,实现所需的功能.

其作用有以下几点:

根据url把用户请求调度到不同的application中.

负载均衡,转发用户请求.

预处理XSL等相关数据.

限制请求速率,设置白名单.

大致了解WSGI框架后我们来看下Paste+Pastedeploy+route+webob开发，openstack开发使用的就是此开发框架，主要使用到的一些模块是:

eventlet:pytohn 的高并发网络库

paste.deploy:用于发现和配置WSGI application 和server的库

routes: 处理http url mapping 的库

webob:处理HTTP请求并提供了一个对象来方便的处理返回的response消息.


Eventlet: 是一个基于协程的python高并发网络库.有以下特点:
1.使用epoll,kqueue或libevent等I/O 复用机制,对于非阻塞I/O 具有良好的性能.
2.基于协程,和进程,线程相比,其切换开销更小,具有更高的性能.
3.简单易用,特别是支持采用同步的方式编写异步的代码.


paste.deploy:

paste deployment是用于查找和配置WSGI应用程序和服务器的系统.对于WSGI应用程序消费者,
它提供了从配置文件或python egg 加载 WSGI 应用程序的单一简单函数(loadapp) .对于WSGI应用程序提供商,它只需要一个简单的入口点到您的应用程序,以便应用程序用户不需要暴露于应用程序的实现细节.

paste.deploy 通常要求application实现一个factory的类方法,如下:

class TestApplication(object):
    def __init__(self):
        pass

    @webob.dec.wsgify
    def __call__(self, req):
        return self.router

    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls()

if '__main__' == __name__:
    application = loadapp('config:%s/config.ini' % (CONF))
    server = eventlet.spawn(wsgi.server,
                            eventlet.listen(('0.0.0.0', 8080)), application)
    server.wait()


paste.deploy 的.ini 配置文件配置讲解:

配置文件说明:一个配置文件有不同的分段,但pastedeploy关心的是前缀,比如app:main or filter:errors.
分隔部分之后是这个分段的name,前一部分是这个分段的type类型.前段给的类型,后段名字将被忽略.

一个简单的ini配置文件格式是 name = value .可以通过缩进后续行来扩展配置.
# 是对前面配置的评论标注

通常,您有一个或两个部分,称谓main,一个应用程序部分(app:main) 和一个服务器部分(server:main)

[composite:main]
use = egg:Paste#urlmap
/ = home
/blog = blog
/wiki = wiki
/cms = config:cms.ini

[app:home]
use = egg:Paste#static
document_root = %(here)s/htdocs

[filter-app:blog]
use = egg:Authentication#auth
next = blogapp
roles = admin
htpasswd = /home/me/users.htpasswd

[app:blogapp]
use = egg:BlogApp
database = sqlite:/home/me/blog.db

[app:wiki]
use = call:mywiki.main:application
database = sqlite:/home/me/wiki.db

urlmap相当于做了多路由的分发,
请求http://xxx/时候会请求分段名称为home的app,走到相对的处理函数或者controller,其他雷同.

