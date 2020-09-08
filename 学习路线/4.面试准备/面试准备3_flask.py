# Flask 是一个类 ,flask 是一个模块
# from flask import Flask, abort, redirect
#
# # Flask 类接收一个参数__name__
# app = Flask(__name__)
#
#
# # 装饰器的作用是将路由映射到视图函数index
# @app.route('/')
# def index():
# 	return 'Hello Python!'
#
#
# if __name__ == '__main__':
# 	app.run()
# # -------------------------
#
# # 路由传递的参数默认当做string处理,这里指定int.尖括号中冒号
# # 后面的内容是动态的
# # @app.route('/user/<int:id>')
# @app.route('/')
# def index():
# 	# abort(404)  # abort  vt. 使流产；使中止
# 	# return 'Hello Python ', 999
# 	return redirect('http://www.baidu.com')
#
#
# @app.errorhandler(404)
# def error(e):
# 	return '您请求的页面不存在了,请确认后再次访问!%s' % e
#
#
# # Flask 应用程序实例的run方法启动web服务器
# if __name__ == '__main__':
# 	app.run()

"""
flask程序运行:  flask是酒瓶的意思  n. [分化] 烧瓶；长颈瓶，细颈瓶；酒瓶，携带瓶
	所有的flask程序必须有一个程序实例.
	flask调用视图函数之后,会将视图函数的返回值作为响应的内容,返回给客户端.
	一般情况下,响应内容主要是字符串和响应状态码.

	WSGI(web server gateway interface的简写)协议:是为python语言定义的web
	服务器和web 应用程序之间的一种简单而通用的接口.它封装了接受HTTP请求.解析HTTP
	请求,发送HTTP,响应等等的这些底层的代码和操作.目的是为了方便开发者高效的编写web应用.

"""
"""
使用abort函数立即终止视图函数的执行,通过abort函数,可以向前端返回一个http标准中存在的错误状态码.表示出现错误的信息.
使用abort抛出一个http标准中不存在的自定义的状态码,没有实际意义.
如果abort函数被触发,其后面的语句将不会被执行.类似于Python中的raise

在flask中通过装饰器来实现捕获异常.errorhandler()接收的参数为异常状态码.视图函数的参数,返回的是错误信息
"""
"""
正则URL是为了匹配指定的url,而匹配指定的url则可以达到限制访问,以及优化访问路径的目的.
"""

# from flask import Flask
# from werkzeug.routing import BaseConverter
#
#
# class Regex_url(BaseConverter):
# 	def __init__(self, url_map, *args):
# 		super(Regex_url, self).__init__(url_map)
# 		self.regex = args[0]
#
#
# app = Flask(__name__)
# app.url_map.converters['re'] = Regex_url
#
#
# @app.route('/user/<re("[a-z]{3}"):id>')
# def hello_itcast(id):
# 	return 'hello %s' % id

# from flask import Flask, make_response
#
# app = Flask(__name__)
#
#
# @app.route('/cookie')
# def set_cookie():
# 	resp = make_response('this is to set cookie')
# 	resp.set_cookie('username', 'itcast')
# 	return resp
#
#
# if __name__ == '__main__':
# 	app.run()

# from flask import Flask, request
#
# app = Flask(__name__)
#
#
# @app.route('/request/')
# def set_cookie():
# 	resp = request.cookies.get('username')
#
# 	return resp
#
#
# if __name__ == '__main__':
# 	app.run()

"""
交互过程:
一切从客户端发起请求开始:
	1.所有flask都必须创建一个程序实例
	2.当客户端想要获取资源时,一般会通过浏览器发起http请求
	3.此时,web服务器使用一种名为web服务器网关接口的wsgi协议,把来自客户端的请求都交给flask程序实例
	4.flak使用werkzeug来做路由分发(url和视图函数之间的对应关系),根据每个url请求,找到具体的视图函数.
	5.在flask程序中,路由一般是通过程序实例的装饰器实现.通过调用视图函数,获取到数据后,把数据传到html模板文件中,模板引擎负责渲染http响应数据,然后由flask返回响应数据给浏览器,最后浏览器显示返回的结果.
	
为啥使用框架?
	避免重复造轮子.
	框架作用:基础操作,例如网络操作,数据库访问,会话管理,等基本操作都交给框架处理
	开发人员主要精力都在具体的业务逻辑上面.

flask框架:
	诞生于2010年,是Armin ronacher 使用 Python语言基于werkzeug工具箱编写的轻量级开发框架.主要是面向需求简单的小应用.
	本身相当于一个内核,其他功能需要扩展.模板引擎使用Jinja2
	框架核心就是Werkzeug和Jinja2。
	

"""
"""
上下文:相当于一个容器,保存flask程序运行过程中的一些信息.flask中有两种上下文,请求上下文和应用上下文.

request和session都属于请求上下文对象.

request封装了http请求的内容.针对的是http请求
session用来记录请求会话中的信息.针对的是用户信息.

"""
# from flask import Flask
# from flask_script import Manager
#
# app = Flask(__name__)
#
# manager = Manager(app)
#
#
# @app.route('/')
# def index():
# 	return '窗前名月光'
#
#
# if __name__ == '__main__':
# 	manager.run()
"""
模板:在之前的示例中,视图函数的主要作用是生成请求响应,这是最简单的请求.
实际上:视图函数有两个作用:处理业务逻辑和返回响应内容.在大型应用中,把业务逻辑和表现内容放在一起.会增加代码的复杂度和维护成本.
模板的作用就是承担视图函数的另一个作用:返回响应内容.
模板其实是一个包含响应文本的文件.其中用占位符(变量)表示动态部分.
告诉模板引擎其具体值需要从使用的数据中获取.使用真实值替代变量.再返回最终得到的字符串,这个过程称之为:渲染

flask使用jinja2这个模板引擎来渲染模板,jinja2可以识别所有类型的变量,包括{}.
jinja2引擎,flask提供的render_template函数封装了该模板引擎.
render_template函数的第一个参数是模板的文件名.后面的参数都是键值对,表示模板中变量对应的真实值.
"""
from flask import Flask, make_response, session
from flask import jsonify
from flask import request
from flask import redirect
from werkzeug.routing import BaseConverter

# 路由传递的参数默认当做string处理,也可以指定参数的类型
# 这里指定int,尖括号中的内容是动态的,在此暂时可以理解为接受int类型的值,实际上int代表使用IntegerConverter去处理url传入的参数
# @app.route('/demo2/<int:user_id>')
# @app.route('/demo2/', methods=['GET', 'POST'])
# def user_info():
# 	# return 'hello %d' % user_id
# 	# 直接从请求中取到请求方式并返回
# 	return request.method
#
# 自定义正则转换器
# class RegexConverter(BaseConverter):
# 	def __init__(self, url_map, *args):
# 		super(RegexConverter, self).__init__(url_map)
# 		# 将接受的第一个参数当做匹配规则进行保存
# 		self.regex = args[0]
#
#
app = Flask(__name__)
#
#
# # # 将自定义转换器添加到转换器字典中,并指定转换器使用时名字为:re
# # app.url_map.converters['re'] = RegexConverter
# #
# #
# # # 使用转换器去实现自定义匹配规则
# # # 当前此处定义的规则是:3位数字
# # @app.route('/user/<re("[0-9]{3}"):user_id>')
# # def user_info(user_id):
# # 	return "user_id是%s" % user_id
# # 获取cookie
@app.route('/set_session')
def set_session():
	session['username'] = 'itcast'
	secret_key:app.secret_key = 'itheima'
	return 'set_session ok!'


@app.route('/get_session')
def get_session():
	return session.get('username')


if __name__ == '__main__':
	app.run()

"""

flask中,定义一个路由,默认的请求方式为:
GET,OPTIONS,HEAD,

cookie指某些网站为了辨别用户身份,进行会话跟踪而存储在用户本地的数据,通常是加密的数据
cookie由服务器生成,发送给客户端浏览器,浏览器会将cookie的key/value保存,下次请求同一网站时就发送该cookie给服务器,前提是浏览器设置为启用cookie.cookie的key/value
可以由服务器端自己定义

应用:最典型的应用是判断注册用户是否已经等录网站:用户可能会得到提示,是否在下一次进入此网站时候保留用户信息以便简化登录手续,这些都是cookie的功劳.

网站的广告推送,经常遇到访问某个网站时,会弹出小窗口,展示我们曾经在购物网站上看过的商品信息

购物车,用户可能会在一段时间内在同一家网站的不同页面中选择不同的商品,这些信息都会写入cookie,以便在最后付款时候提取信息.

提示:cookie是存储在浏览器中的一段纯文本信息,建议不要存储敏感信息如密码,因为电脑上的浏览器可能被其他人使用.
cookie是基于域名安全,不同域名的cookie死不能互相访问的,如访问itcast.cn时候想浏览器中写了cookie信息,使用同一浏览器访问baidu.com时,无法访问到itcast.cn写的cookie信息.
浏览器的同源策略

当浏览器请求某网站的时候,会将本网站下所有的cookie信息提交给服务器,所以在request中可以读取cookie信息

session:会话,对于敏感,重要的信息,建议要存储在服务器.不能存储在浏览器中,如用户名,余额 ,等级,验证码等信息.
在服务器端进行状态保持的方案就是session
session依赖于cookie

session请求上下文对象,用于处理http请求中的一些数据内容


在客户端和服务器交互的过程中,有些准备工作或扫尾工作需要处理.比如:在请求开始时,建立数据库;连接.在请求开始时,根据请求进行权限校验.在请求结束时,指定数据的交互格式

为了让每个视图函数避免编写重复功能的代码,flask提供了通用设施的功能,即请求钩子.

请求钩子是通过装饰器的形式实现,flask支持如下四种请求钩子:
before_first_request在处理第一个请求前执行,
before_request在每次请求前执行
如果在某修饰的函数中返回了一个响应,视图函数将不再被调用
after_request 如果没有抛出错误,在每次请求后执行
接受一个参数:视图函数作出的响应
在此函数中可以对响应值在返回之前做最后一步修改处理
需要将参数中的响应在此参数中进行返回

abort方法:
抛出一个给定状态代码的HTTPException或者指定响应.例如想要用一个页面为找到异常来终止请求,你可以调用abort(404)
参数:code-HTTP的错误状态码

"""
# from flask import Flask
# from flask import abort
#
# app = Flask(__name__)
#
# # 在第一次请求之前调用,可以在此方法内部做一些初始化操作
# @app.before_first_request
# def before_first_request():
# 	print('before_first_request')
#
# # 在每一次请求之前调用,这时候已经有请求 了,可能在这个方法里面做请求的校验
# # 如果请求的校验不成功,可以直接在此方法中进行响应,直接return之后那么就不会执行视图函数
# @app.before_request
# def before_request():
# 	print('before_request')
#
# # 在执行完视图函数之后会调用,并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
# @app.after_request
# def after_request(response):
# 	print('after_request')
# 	response.headers['COntent-Type'] = "application/json"
# 	return response
# # 在每一次请求之后都会调用,会接受一个参数,参数是服务器出现的错误信息
# @app.teardown_request
# def teardown_request(e):
# 	print('teardown_request')
#
#
# @app.route('/')
# def index():
# 	return 'index'
#
#
# if __name__ == '__main__':
# 	app.run(debug=True)
"""
上下文:即语境,语意.
在程序中可以理解为在代码执行到某一时刻时,根据之前代码所做的操作以及下文即将要执行
的逻辑,可以决定在当前时刻下可以使用到的变量,或者可以完成的事情.

flask中有两种上下文,请求上下文和应用上下文

flask中上下文对象:相当于一个容器,保存了flask程序运行过程中的一些信息.

请求上下文:request context

在flask中,可以直接在视图函数中使用request这个对象进行获取相关数据,而request就是请求上下文的对象,保存了当前本次请求的相关数据,请求上下文对象有:request,session

request:封装了HTTP请求的内容,针对的是http请求,
session用来记录请求会话中的信息,针对的是用户信息.

应用上下文:名字是应用上下文,但是它不是一直存在的.它只是request context 中的一个对app的代理,所谓local proxy.它的作用主要是帮助request获取当前的应用,它是伴request而生,随request而灭的.

应用上下文有:current_app g


"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 把Manager类和应用程序实例进行关联
manager = Manager(app)

@app.route('/index')
def index():
	return '窗前明月光'


if __name__ == '__main__':
	manager.run()
