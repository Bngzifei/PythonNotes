"""
re:regex的简写    adj. 定期的；有规律的；合格的；整齐的     regular:有规律的
正则表达式概念:
用事先定义好的一些特定字符,及这些特定字符的组合,组成一个规则字符串.
这个规则字符串用来表达对字符串的一种过滤逻辑

匹配:意思就是从字符串中把符合条件的部分切出来,截取出来

"""

"""
re:模块,操作正则表达式

小结:re.match()方法根据正则表达式从头开始匹配字符串数据
"""
# import re

# match()方法进行匹配
# res = re.match(r'itcast','itcast.cn')
# # group()方法提取数据
# print(res.group())

"""
匹配单个字符:


.  匹配1个任意字符(除了\n)

[] 匹配[]里面列举的字符

\d 匹配数字,即0-9

\D 匹配非数字,即不是数字

\s 匹配空白,即空格,tab键(代表制表符)

\S 匹配非空白

\w 匹配非特殊字符,即a-z,A-Z,0-9,_,以及汉字

\W 匹配特殊字符,即非字母,非数字,非汉字


"""
import re

# 任何字符都可以\t 空格也可以,就是\n不可以
# ret = re.match(r'..................','-*`~!@$%^&*\t ()汉字中国0')
# print(ret.group())

#
# ret = re.match(r't.o','too')
# print(ret.group())
#
# ret = re.match(r't.o','two')
# print(ret.group())


# ret = re.match(r'h','hello python')
# print(ret.group())
#
#
# ret = re.match(r'H','Hello python')
# print(ret.group())

# ret = re.match(r'[hH]ello', 'Hhello python')
# print(ret.group())

# 匹配0-9的第一种写法
# ret = re.match(r'[0-9]', '9Hellop9')  # 记得位置要对应
# print(ret.group())

# 匹配0-9的第二种方法
# ret = re.match(r'[0123456789]','0dhfjf')
# print(ret.group())
# 没有匹配到就报错:AttributeError: 'NoneType' object has no attribute 'group'
# ret = re.match(r'[0-35-9]','4dhfjf')  # 第一位字符只能在0-3或者5-9之间
# print(ret.group())

# ret = re.match(r'[0-35-9]','5dhfjf')  # 第一位字符只能在0-3或者5-9之间
# print(ret.group())

"""\d匹配数字0-9"""

import re

# ret = re.match(r'肠儿1号','肠儿1号发射')
# print(ret.group())

# ret = re.match(r'肠儿\d号','肠儿2号发射')
# print(ret.group())

"""\D匹配非数字"""

# obj = re.match(r'\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D', '~.!@o汉字%$*&^|/ \n\t')
# 只要不是数字,随便,空格也可以,\n表示的换行符(Enter键)也可以,\t表示的tab键也可以
# print(obj.group())  # ~.!@o汉字%$*&^|/

"""\s匹配空白"""

# obj = re.match(r'\s\s\s',' \t\n')
# 匹配空格键,\t表示的tab键(制表符,缩进4个空格键),\n表示的Enter键(换行)
# print(obj.group())

"""\S匹配非空白"""
# 只要不是空格,\t,\n就可以
# obj = re.match(r'\S\S\S\S','a_!9+.-vidfivjvdfvdfvkdfjk')
# print(obj.group())

"""\w匹配非特殊字符a-z,A-Z,0-9,_,以及汉字/其他语言,比如日语,韩语法语等等"""

# obj = re.match(r'\w\w\w\w\w','a_べ9W孙aaddd')
# 字母(不区分大小写),数字,下划线,汉字
# print(obj.group())  # a_べ9W

"""\W匹配特殊字符即非字母,非数字,非汉字"""

# obj = re.match(r'\W\W\W\W\W\W\W\W','~`!@#$%^&*-|/?><,.')
# print(obj.group())


"""匹配多个字符:<其实就是匹配前一个字符出现的次数>

* 匹配前一个字符出现0次或者无限次,即可有可无

+ 匹配前一个字符出现1次或者无限次,即至少一次

? 匹配前一个字符出现1次或者0次,即要么有1次,要么没有

{m} 匹配前一个字符出现m次,即匹配指定的次数

{m,n} 匹配前一个字符出现从m到n次


"""

"""示例:* 0个或多个  """

"""

需求：匹配出一个字符串第一个字母为大写或者小写字符，
后面都是小写字母并且这些小写字母可有可无
"""
# import re

# obj = re.match(r'[A-Za-z][a-z]*','Asdhssklddffdh')
# print(obj.group())

"""示例: + 一个或多个 """
import re

"""
需求：匹配一个字符串，第一个字符是t,最后一个字符串是o,中间至少有一个字符
"""
# .占位的作用,.+ 表示这个位置上面可以有至少一个字符,反正有就行结尾是o,开头是t就行
# obj = re.match(r't.+o','tfvhgfdgdovdfvdvp6556596')
# print(obj.group())

"""示例:? 一个或0 个"""
"""需求：匹配出这样的数据，但是https中 这个s可能有，也可能这个s没有"""
# import re
# obj1 = re.match(r'https?','httpdffvldfjkdjvo')
# obj2 = re.match(r'https?','httpsssdffvldfjkdjvo')
# print(obj1.group())
# print(obj2.group())

"""示例:{m},{m,n}  m次,从m到n次  """
"""
需求：匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
"""
# import re
# obj = re.match(r'[a-zA-Z0-9_]{8,20}', 'passwejefivfdbksfkvjk')
# print(obj.group())


"""匹配开头和结尾:

^ 匹配字符串开头
$ 匹配字符串结尾

"""
"""需求：匹配以数字开头的数据"""

# import re
#
# obj = re.match(r'^\d.*', '233vdkvkvdfvkjnbksv')
# print(obj.group())
"""需求：匹配以数字结尾的数据"""

# import re
# obj = re.match(r'.*\d$', '233vdkvkvdfvkjnbksv9')
# print(obj.group())

"""需求: 匹配以数字开头中间内容不管,以数字结尾"""
# import re
# #  9fgfggffhh-!@#$%^&*()_0
# obj = re.match(r'^\d.*\d$','9fgfggffhh-!@#$%^&*()_0')
# print(obj.group())

"""除了指定字符以外,都匹配"""

"""
[^指定字符]: 对应位置除了指定字符以外,都匹配
"""
# import re
# # 第一个字符不是5-9之间的数字,就匹配出来
# obj = re.match(r'[^5-9].*','_66fidijb')
# print(obj.group())

"""匹配分组:

|  匹配左右任意一个表达式

(ab) 将括号中字符作为一个分组

\num 引用第num个分组匹配到的字符串

(?P<name>) 分组起别名

(?P=name)  引用别名为name分组匹配到的字符串


"""

"""示例:|  匹配左右任意一个表达式, 表示或者关系"""

"""
需求：在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
"""
# import re

# 水果列表
# fruit_list = ['apple','banana','pear','orange']
#
# # 遍历数据
# for value in fruit_list:
# 	obj = re.match(r'apple|pear',value)
# 	if not obj:
# 		continue
# 		# print('不是我想要的')
# 	else:
# 		print('是我想要的', obj.group())


"""示例:() 将括号中字符作为一个分组,表示分类别了 """

"""需求：匹配出163、126、qq等邮箱"""

import re

# obj = re.match(r'[a-zA-Z0-9_]{4,20}@(126|163|qq|sina|yahoo|gmail)\.(com|cn)', 'bngzifei@gmail.com')
# print(obj.group())

"""需求: 匹配 qq:10567这样的数据，提取出来qq文字和qq号码"""
# 备注 qq号是5-11位的,所以下面的^[1-9]占了一位,\d{4,10},
# 意思是从第二位开始是数字(0-9均可),并且这个数字可以最少出现4次(包括第二位出现的次数在内),
# 最多出现10次.这样就是4位到10位,加上第一位就是5-11位的qq号码位数要求了.
# obj = re.match(r'(^[1-9]\d{4,10})','26045')


# 注意:如果加了分组符号()之后,就不能在  不是开头的位置使用^
# obj = re.match(r'^((qq)|(QQ)|(qQ)|(Qq)):([1-9]\d{4,10})','qQ:26042441698222222')
#
#
# if obj:
# 	print(obj.group())
# 	print(obj.group(1))
# 	print(obj.group(2))
# else:
# 	print('匹配失败')
# obj = re.match(r'^[1-9]\d..','111111112604244167')
# print(type(obj))
# print(obj.group())

"""示例:\num 引用第num个分组匹配到的字符串   """
"""需求：需求：匹配出<html>hh</html> """
import re

# obj = re.match("<[a-zA-Z]+>.*</[a-zA-Z]+>", "<html>hh</div>")
#
# if obj:
#     print(obj.group())
# else:
#     print("匹配失败")
# \1:表示 直接引用第1个分组匹配到的字符串,这里的第一个分组就是([a-zA-Z]+)匹配到了  html
# obj = re.match(r"<([a-zA-Z]+)>.*</\1>", "<html>hh</html>")
# 对比得出,r的作用就是转义,在\1中,我们需要\,如果没有r的转义就需要使用\\来表示\1中的\.
# obj1 = re.match("<([a-zA-Z]+)>.*</\\1>", "<html>hh</html>")
# if obj1:
#     print(obj1.group())
# else:
#     print("匹配失败")

"""示例:需求：匹配出<html><h1>www.itcast.cn</h1></html>"""
# import re
# obj = re.match(r"<([a-zA-Z]+)><([a-zA-Z1-6]+)>.*</\2></\1>", "<html><h1>www.itcast.cn</h1></html>")
#
# if obj:
#     print(obj.group())
# else:
#     print("匹配失败")

"""
示例:(?P<name>) --> 给分组起别名,(?P=name) --> 引用别名为name分组匹配到的字符串 

"""

"""需求：匹配出<html><h1>www.itcast.cn</h1></html>"""
# import re

# obj = re.match('<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>','<html><h1>www.itcast.cn</h1></html>')

# print(obj.group())

"""小结:(分组数据):分组数是从左到右的方式进行分配的"""

"""re模块的高级用法"""

"""1.serach """

"""需求：匹配出水果的个数"""
# import re
#
# # pattern:正则表达式 string:需要进行匹配操作的字符串
# obj = re.search(r'\d+','水果有20个,其中苹果8个')
# if obj:
# 	print(obj.group())
# else:
# 	print('匹配失败')


"""2.findall"""

"""需求：匹配出多种水果的个数"""

# import re
#
# # pattern:正则表达式 string:需要进行匹配操作的字符串,返回值是一个列表类型,不需要使用group()方法进行匹配输出
# obj = re.findall(r'\d+','水果有20个,其中苹果8个,鸭梨5个')
# if obj:
# 	print(obj)  # ['20', '8', '5']
# else:
# 	print('匹配失败')
#

"""3.sub 将匹配到的数据进行替换(sub是子,替换的意思),不需要使用group()方法进行匹配输出"""

"""需求：将匹配到的评论数改成22"""

# import re

# pattern:正则表达式 repl:替换后的字符串 string:需要匹配的字符 count:替换次数,count = 1 根据指定次数替换,默认全部替换
# 注意:按照从左到右的顺序进行匹配操作,指定替换次数是1,所以这里才将第一次匹配到的评论数:10替换成了22
# res = re.sub(r'\d+','22','评论数:10,赞数:20',count=1)
# print(res)


"""需求：将匹配到的阅读数加1"""

# import re

# def add(obj):
# 	value = obj.group()
# 	res = int(value) + 1
# 	return str(res)
#
#
# ret = re.sub(r'\d+', add, '阅读数:10')
# print(ret)

"""4.split 根据匹配进行切割字符串，并返回一个列表"""

"""需求：切割字符串"貂蝉,杨玉环:西施,王昭君"""

# pattern:正则表达式 string:需要匹配的字符串 maxsplit=0:分割次数,默认全部分割
# res = re.split(r',|:','貂蝉,杨玉环:西施,王昭君',maxsplit=1)
# ['貂蝉', '杨玉环:西施,王昭君']

# 默认全部分割
# res = re.split(r',|:','貂蝉,杨玉环:西施,王昭君')
# ['貂蝉', '杨玉环', '西施', '王昭君']
# print(res)

"""练习:

使用正则表达式把职位描述信息提取出来,不要html标签数据,只能使用sub替换方法.

<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

</div>



"""

import re

my_str = '''<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

</div>'''

# /?  就表示/ 出现0次或者1次均可
# res = re.sub(r'</?[a-zA-Z1-6]+>|\Wnbsp;','',my_str)
# res = re.sub(r'</?[a-zA-Z1-6]+>|&nbsp;','',my_str)
# 去除左右两边的空格
# print(res.strip())


"""Python 贪婪和非贪婪:

Python 里面数量词默认是贪婪的,总是尝试匹配尽可能多的字符

非贪婪:总是匹配尽可能少的字符

"""

"""在 '*','?','+','{m,n}' 后面加上?,贪婪就变成非贪婪 """
import re

s = 'This is a number 234-235-22-423'
obj = re.match(r'.+(\d+-\d+-\d+-\d+)', s)
# 4-235-22-423
print(obj.group(1))

obj1 = re.match(r'.+?(\d+-\d+-\d+-\d+)', s)
# 234-235-22-423
print(obj1.group(1))

"""

总结:正则表达式模式中使用到通配符,那么它在从左到右的顺序进行取值匹配的时候,
会尽量抓取满足匹配最长字符串. 示例中 .+ 会从字符串开始位置匹配,一直匹配到
23的位置(因为后面分组的正则表达式里面必须有一个数字来匹配\d+),\d+是匹配数字有1位
和超过1位的情况.只要有1位数字就行,所以它匹配了234中的4,而 .+ 则匹配了从字符串开始 位置到4之前的所有字符

解决方式:非贪婪操作符 ?   这个操作符可以跟在 + * ? 的后面,这样?前面的正则表达式不能匹配?后面正则表达式的数据.

+   1次或者多次

*   0次或者多次

?   0次或者1次


"""
"""示例:斗鱼字符串"""

import re

my_str1 = '''
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
'''

# 非贪婪的样式: *?或者+?或者??
# 非贪婪的含义: ? 后面的数据不要让前面的正则匹配,让?后面的正则去匹配
# https? 表示 https或者http的情况
# obj = re.search(r'https?://.*?.jpg',my_str1)
# if obj:
# 	print(obj.group())
# else:
# 	print('未匹配')


"""r的作用:

说明:Python中字符串前面加上r表示原生字符串,数据里面的\不需要进行转义,只是针对\起作用.所以以后全部都加r

Python 里的原生字符串很好的解决了这个问题,有了原生字符 串,你再也不用担心是不是漏写了\,写出来的表达式也更直观

建议:如果使用正则表达式匹配数据可以都加上r,要注意r针对的只是\起作用,不需要手动对其进行转义.


"""

"""示例:"""
import re

mm = "c:\\a\\b\\c"
# c:\a\b\c
print(mm)
print(re.match('c:\\\\', mm).group())
print(re.match('c:\\\\a', mm).group())
print(re.match(r'c:\\a', mm).group())
print(re.match(r'c:\\a\\b\\c', mm).group())
# AttributeError: 'NoneType' object has no attribute 'group'  没有匹配到
print(re.match(r'c:\a\\b\\c', mm).group())
