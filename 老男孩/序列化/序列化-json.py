"""
以前我们是使用eval()内置方法将一个字符串转成Python对象
(字符串形式的Python数据类型转换成相应的Python数据类型),
不过eval方法是有局限性的,对于普通的数据类型json.load和eval都可以使用,但是,当
遇到特殊类型的时候,eval就不管用了,所以eval的重点还是通常用来执行一个字符串表达式,
并返回表达式的值.

序列化:
  我们把对象(变量)从内存中变成可存储或者可传输的过程称之为序列化.在Python中叫  Pickling
在其他语言中也被称之为serialization,marshalling,flattening.
序列化之后,就可以把序列化之后的内容写入磁盘,或者通过网络传输到别的机器.

"""
"""
JSON:

如果我们要在不同的编程语言之间传递对象,就必须把对象序列化成标准格式,比如XML,但是,更好的方法是
序列化为JSON,因为JSON表示出来就是一个字符串,可以被所有语言读取,也可以方便的存储到磁盘或者通过
网络传输.JSON不仅是标准格式,并且比XML更快,而且可以直接在Web页面中读取,非常方便.

JSON表示的对象就是标准的JavaScript语言的对象,JSON和Python内置的数据类型对应如下:

	JSON类型                      Python

	{}							  dict

	[]							  list

	"string"					  str

	1234.56						  int/float

	true/false					  True/False

	null						  None


备注: dumps() 是序列化  loads()是反序列化

dumps可以理解为放进去
loads可以理解为取出来<加载实际上就是这个意思,比如平时所说的加载一个图片,其实就是把这个图片取出来显示给用户>
"""
# 将一个字典写入到文本
# 写入
# dic = {'name':'alex'}
# f = open('dic.txt','w')
# f.write(dic)  # dic是一个字典类型,这样肯定是写不进去的,因为文本写入要求写入的对象是字符串 str 格式
# f.write(str(dic))
# 读取
# f_read = open('dic.txt','r')
# data = f_read.read()
# print(type(data))  # <class 'str'>
# # print(data['name'])  # TypeError: string indices must be integers:意思是str字符串的索引必须是整数类型,说明读取出来的不是字典类型的数据,是一个字符串
# data = eval(data)  # 将字符串类型转为字典类型
# print(data['name'])  # alex

# 但是:eval()存不了函数,类,JSON可以存储函数,但是不能存储类,pickle什么类型的都可以,类,函数,只要你想到的均可以.

# import json

# dic = {'name':'alex'}  JSON 会把所有的''单引号变成""双引号
# dic = {"name": "alex"}  # JSON 也会把所有的""双引号变成""双引号
# i = 8
# s = 'hello'
# l = [11, 22]
# data1 = json.dumps(dic)
# data2 = json.dumps(i)
# data3 = json.dumps(s)
# data4 = json.dumps(l)
# print(data1)  # {"name": "alex"}
# print(type(data1))  # <class 'str'>  JSON 字符串  什么语言都可以使用了
# print(data2)  # 8
# print(type(data2))  # <class 'str'>
# print(data3)  # "hello"
# print(type(data3))  # <class 'str'>
# print(data4)  # [11, 22]
# print(type(data4))  # <class 'str'>
"""
结论:json.dumps()之后的数据都是str的类型,即可以将Python里面的任何(类除外)数据类型均可以转换成
字符串形式,这样就可以写入保存到文本文件中了.
注意:JSON 里面没有单引号''  只有双引号""

转换:传输/存储到磁盘
前端传输给后端,后端传输给前端,也得使用json封装进行传输
"""
# 存进去  dumps:倾泻,倾倒.
# dic = {"name": "alex"}
# dic_str = json.dumps(dic)  # 就是将其他数据类型转成字符串类型
# f = open('new_hello.txt','w')
# f.write(dic_str)

# 取出来
# f_read = open('new_hello.txt','r')
# print(type(f_read.read()))  # <class 'str'> 因为读出来还是字符串类型,程序中不方便转换成原来的数据类型,不如json.load()方法好用
# print(f_read.read())  # {"name": "alex"} 也可以读出来,但是建议不要这么用
# data = json.loads(f_read.read())  # 加载:作用就是将字符串转成对应的数据类型
# print(type(data))  # <class 'dict'>
# print(data)  # {'name': 'alex'}
# print(data['name'])  # alex


# json就是一个桥梁,进行多种语言之间的数据转换,连接作用
# x = '[null,true,false,1]'
# print(eval(x))  # 直接报错  NameError: name 'null' is not defined
# print(json.loads(x))  # [None, True, False, 1]

# dict1 = {'name': 'alex', 'age': 15, 'sex': 'male'}
# print(type(dict1))  # <class 'dict'>
#
# j = json.dumps(dict1)
# print(type(j))  # <class 'str'>

"""
json.dump(参数1,参数2)和json.dumps(参数3)的区别:
参数2:指的是打开文件的句柄
dumps() 加上write() 等价于 dump()
即下面例子中:
dic_str = json.dumps(dic)
f.write(dic_str)
这两句等价于  dic_str1 = json.dump(dic, f) 这一句
"""
# 示例:
# f = open('new_hello1.txt', 'w')
# dic = {"name": "alex"}
# dic_str = json.dumps(dic)
# f.write(dic_str)
# dic_str1 = json.dump(dic, f)
"""
json.load(参数1,参数2) 和 json.dumps(参数3) 的区别:
参数1是打开文件的句柄.就是 f_read = open('new_hello1.txt', 'r')
load()等价于 loads() 加上 read() 即下面示例中的

json.load(f_read) 等价于下面这两句 read() 和loads()
# data = f_read.read()
# print(json.loads(data))

"""
# 示例:
# f_read = open('new_hello1.txt', 'r')
# data = f_read.read()
# print(json.loads(data))
# print(json.load(f_read))  # {'name': 'alex'}


# 新建一个json的文本<ps:里面新建后的数据类型是str字符串类型>
import json

with open('json_test', 'r') as f:

	# print(json.load(f)['name'])  # libin

	data = f.read()
	data1 = json.loads(data)
	print(data1['name'])  # libin
