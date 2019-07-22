"""
异常:Bug,出现问题了.
提前干预,提前预防.

网络请求的地方使用的最多.应急处理,预防这种问题.

如果真的产生了,不是让程序停掉,而是让程序给用户一个错误提示,跳过异常继续运行.而不是程序闪退.

预判处理:

如果某些代码很可能出错,就把这些代码放在try里面尝试性的去执行.

当try里面的代码出现异常,会直接执行对应的except的代码.except就是来拦截try里面的异常.

之前都是Python解释器来处理异常,直接报错.先在try就是有人提前帮你处理这些错误了.

except:就是一个拦截异常的作用.

就好比用户输入密码出错了,不能让程序闪退,而是应该给用户提示并继续程序的执行.实际上使用if进行预判处理也可以,但是try是专门来处理代码异常的,所以还是使用专业的处理异常的语法模块.

着重在网络请求的时候使用.
有可能正常执执行,也有可能出现异常.
except去拦截异常


基类:就是父类的意思.
异常类的基类是Exception.真正的最基类是BaseException.

代码不稳定就去try里面执行.

try后面可以跟多个except,但是只会执行某一个.

在使用try的时候,一般后面必须要跟一个except或者finally. else可以写也可以不写.
"""

try:
	f = open('113.txt', 'r')  # 代码出现异常了,立刻就停止运行了,不会继续往下运行.
	# content = f.read()
	# print(content)
	f.close()
	# print(b)

except FileNotFoundError as error:  # 拦截指定类型的异常 as 前面必须指定异常类型
	print(error)
except NameError as error1:  # 拦截指定类型的异常 as 前面必须指定异常类型
	print(error1)


# except Exception as error:  # bug终结者.并且可以拿到错误信息
# 	print(error)

# except:  # bug终结者.只有当try里面的代码出错了才会执行.
# 	print('代码出错了')


# NameError  命名错误
# FileNotFoundError  文件找不到错误
else:  # 如果try里面的代码没有出错,就执行else里面代码,只能1个,位置只能放到try和finally中间.
	print('如果try里面的代码没有出错,就执行else里面代码')

finally:  # 后面不能接东西.无论try里面有没有异常,都会执行finally里面的代码,只能1个.放到最后
	print('无论try里面有没有异常,都会执行finally里面的代码')

# print('这里还会执行吗?')


"""NameError: name 'a' is not defined"""