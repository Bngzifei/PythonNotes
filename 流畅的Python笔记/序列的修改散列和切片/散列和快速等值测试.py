"""
示例中的__hash__方法简单地计算hash(self.x) ^ hash(self.y).这一次,我们要使用^异或运算符依次计算各个分量的散列值,像这样:v[0]
^ v[1] ^ v[2]...这正是functools.reduce函数的作用.之前我说reduce没有以往那么常用但是计算向量所有分量的散列值非常适合使用这个函数.


归约函数(reduce,summ,any,all)把序列或有限的可迭代对象变成一个聚合结果.

我们已经知道functools.reduce()可以替换成sum().下面说说它的原理.它的关键思想是,把一系列值归约成单个值.reduce()函数的第一个参数是接受两个参数的函数,第二个函数是一个可迭代的镀锡.假如有个接受两个参数的fn函数和一个lst列表.调用reduce(fn,lst)时,fn会应用到第一对元素上,即fn(lst[0],lst[1]),生成第一个结果r1.然后,fn会应用到r1和下一个元素上,即fn(r1,lst[2]),生成第二个结果r2.接着,调用fn(r2,lst[3]),生成r3...直到最后一个元素,返回最后得到的结果rN.


使用reduce函数可以计算5!
import functools
functools.reduce(lambda a,b:a*b,range(1,6))
回到散列问题上.

计算整数0~5的累计异或的3种方式.

1.使用for循环和累加器变量计算聚合异或
n = 0
for i in range(1,6):
	n ^= i

2.使用functools.reduce函数,传入匿名函数
import functools
functools.reduce(lambda a,b:a^b,range(6))

3.使用functools.reduce函数,把lambda表达式换成operator.xor
import operator
functools.reduce(operator.xor,range(6))

以上3种方式里,我最喜欢最后一种,其次是for循环.


operator模块以函数的形式提供了Python的全部中缀运算符,从而减少使用lambda表达式.

添加__hash__方法:
"""
from array import array
import reprlib
import math
import functools
import operator

class Vector:
	typecode = "d"

	def __eq__(self,other):
		return tuple(self) == tuple(other)

	def __hash__(self):
		hashes = (hash(x) for x in self._compontents)
		return functools.reduce(operator.xor,hashes,0)

"""
为了使用reduce函数,导入functools模块

为了使用xor函数,导入operator模块

__eq__方法没变,我把它列出来是为了把它和__hash__方法放在一起,因为它们要结合在一起使用.

创建一个生成器表达式,惰性计算各个分量的散列值

把hashes提供给reduce函数,使用xor函数计算聚合的散列值;第三个参数0是初始值.

警告:

使用reduce函数时最好提供第三个参数,reduce(function,iterable,inintializer),这样能避免这个异常:TypeError:reduce() of empty sequence with no initial value.  说明,如果序列为空,inintilizer是返回的结果:否则,在归约中使用它作为第一个参数,因此应该使用恒等值.比如,对+|和^来说,initializer应该是0;而对*和&来说,应该是1.

示例中实现的__hash__方法是一种映射归约计算.

映射归约:把函数应用到各个元素上,生成一个新序列(映射,map),然后计算聚合值(归约,reduce).

映射过程计算各个分量的散列值,归约过程则使用xor运算符聚合所有散列值.把生成器表达式替换成map方法,映射过程更明显:


def __hash__(self):
	hashes = map(hash,self._components)
	return functools.reduce(operator.xor,hashes)


在Python2中使用map函数效率低些,因为map函数要使用结果构建一个列表.但是在Python3中,map函数式惰性的,它会创建一个生成器,按需产出结果,因此能节省内存---这与示例中使用生成器表达式定义__hash__方法的原理一样.



为了提高比较的效率,Vector.__eq__方法在for循环中使用zip函数.

def __eq__(self,other):
	if len(self) != len(other):
		return False
	for a,b in zip(self,other):
		if a != b:
			return False

	return True


如果两个对象的长度不一样,那么它们不相等.

zip函数生成一个由元组构成的生成器,元组中的元素来自参数传入的各个可迭代对象.前面比较长度的测试是有必要的,因为一旦有一个输入耗尽,zip函数会立即停止生成值,而且不发出警告.

只要有两个分量不同,返回False,退出.

否则,对象是相等的.

示例10-13的效率很好,不过用于计算聚合值的整个for循环可以替换成一行all函数调用:如果所有 分量对 的比较结果都是True,那么结果就是True.只要有一次比较的结果是False,all函数就返回False.使用all函数实现__eq__方法的方式如示例10-14.

使用zip和all函数实现Vector.__eq__方法:

def __eq__(self,other):
	rerurn len(self) == len(other) and all(a == b for a,b in zip(self,other))

注意:首先要检查两个操作数的长度是否相同,因为zip函数会在最短的那个操作数耗尽时停止.


出色的zip函数

使用for循环迭代元素不用处理索引变量,还能避免很多缺陷,但是需要一些特殊的使用函数协助.其中一个是内置的zip函数.使用zip函数能轻松地并行迭代两个或更多可迭代对象,它返回的元组可以拆包成变量,分别对应各个并行输入中的一个元素
.


zip函数返回一个生成器,按需生成元组.

为了输出,构建一个列表;通常,我们会迭代生成器.

zip有个奇怪的特性:当一个可迭代对象耗尽后,它不发出警告就停止.

itertool.zip_longest函数的行为有所不同:使用可选的fillvalue(默认值为None)填充缺失的值,因此可以继续产出,直到最长的可迭代对象耗尽.


为了避免在for循环中手动处理索引变量,还经常使用内置的enumerate生成器函数.

BIF内置函数的链接:
https://docs.python.org/3/library/functions.html#enumerate


至少对我来说,这是奇怪的.我认为,当组合不同长度的可迭代对象时,zip应该抛出ValueError




格式化:

Vector类的__format__方法与Vector2d类的相似,但是不使用极坐标,而使用球面坐标(也叫超球面坐标),因为Vector类支持n个维度,而超过四维后,球体变成了"超球体".因此,我们会把自定义的格式后缀由"p"变成"h"

扩展格式规范微语言时,最好避免重用内置类型支持的格式代码.这里对象微语言的扩展还会用到浮点数的格式代码"eEfFgGn%",而且保持原意,因此绝对要避免重用代码.整数使用的格式代码有"bcdoxXn",字符串使用的是"s".在Vector2d类中,我选择使用"p"表示极坐标.使用"h"表示超球面坐标是个不错的选择.


例如,对四维空间(len(v) == 4)中的Vector对象来说,"h"代码得到的结果是这样:<r,xxxx>

在小幅改动__format__方法之前,我们要定义两个辅助方法:一个是angle(n),
用于计算某个角坐标,另一个是angles(),返回由所有角坐标构成的可迭代对象.我们不会讲解其中涉及的数学原理,如果你好奇的话,可以查看维基百科中的n维球体词条.


"""
from array import array
import reprlib
import math
import numbers
import operator
import itertools

class Vector:
	typecode = "d"

	def __init__(self,_components):
		self._components = array(self.typecode,components)

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components = reprlib.repr(self._components)
		components = components[components.find("["):-1]
		return "Vector({})".format(components)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(self._components))

	def __eq__(self,other):
		return (len(self) == len(other) and all(a== b for a,b in zip(self,other)))

	def __hash__(self):
		hashes = (hash(x) for x in self)
		return functools.reduce(operator.xor,hashes,0)

	def __abs__(self):
		return math.sqrt(sum(x * x for x in self))

	def __bool__(self):
		return bool(abs(self))

	def __len__(self):
		return len(self._components)

	def __getitem__(self,index):
		cls = type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg = "{.__name__} indices must be integers"
			raise TypeError(msg.format(cls))

	shortcut_name = "xyzt"

	def __getattr__(self,name):
		cls = type(self)

		if len(name) == 1:
			pos = cls.shortcut_name.find(name)
			if 0 <= pos < len(self._components):
				return self._components[pos]
		msg = "{.__name__!r} object has no attribute {!r}" 
		raise AttributeError(msg.format(cls,name))

	def angle(self,n):
		r = math.sqrt(sum(x*x for x in self[n:]))
		a = math.atan2(r,self[n-1])
		if (n == len(self) -1) and (self[-1] < 0):
			return math.pi * 2
		else:
			return a

	def angeles(self):
		return (self.angele(n) for n in range(1,len(self)))

	def __format__(self,fmt_spec=""):
		if fmt_spec.endswith("h"):  # 超球面坐标
			fmt_spec = [:-1]
			coords = itertools.chain([abs(self)],self.angeles())
			outer_fmt = "<{}>"
		else:
			coords = self
			outer_fmt = "({})"

		components = (format(c,fmt_spec) for c in coords)
		return outer_fmt.format(", ".join(components))

	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv)

"""
我们在__format,angle和angles中大量使用了生成器表达式,不过我们的目的是让Vector类的__format__方法与Vector2d类处在同一水平上.

...,不过二者的构造方法签名不同,Vector类的构造方法接受一个可迭代对象,这与内置的序列类型一样.Vector的行为之所以像序列,是因为它实现了__getitem__方法和__len__方法,借此,我们讨论了协议,这是鸭子类型语言使用的非正式接口.

然后,我们说明了my_seq[a:b:c]句法背后工作的工作原理:创建slice(a,b,c)对象,交给__getitem__方法处理.了解这一点之后,我们让Vector正确处理切片,像符合Python风格的序列那样返回新的Vector实例.


接下来,我们为Vector实例的头几个分量提供了只读访问功能,使用my_vec.x这样的表示法.这一点通过__getattr__方法实现.实现这一功能之后,用户会想通过my_vec.x = 7 这样的写法为头几个分量赋值-----这是一个潜在的缺陷.为了解决这个问题,我们又实现了__setattr__方法,通过它禁止为单字母属性赋值.大多数时候,如果定义了__getattr__方法,那么也要定义__setattr__方法,这样才能避免行为不一致.

实现__hash__方法特别适合使用functools.reduce函数,因为我们要把异或运算符^依次应用到各个分量的散列值上,生成整个向量的聚合散列值.在__hash__方法中使用reduce函数之后,我们又使用内置的归约函数all实现了效率更高的__eq__方法.


Vector类的最后一项改进是在Vector2d的基础上重新实现__format__方法,这一次,除了支持笛卡尔坐标,我们还支持了球面坐标.为了定义__format__方法及其辅助方法,我们用到了很多数学知识和几个生成器,但这些是实现细节.


与第9章一样,我们经常分析Python标准对象的行为,然后进行模仿,让Vector的行为符合Python风格.


第13章使用的数学知识比angle()方法用到的简单多了,但是通过了解Python中缀运算符的工作方式,我们对面向对象的设计的认识将更近一步.讨论运算符重载之前,我们将先定义一个类,说明如何使用接口和继承组织多个类---这是第11章和第12章的话题.

强大的高阶函数reduce也叫合拢,累计,聚合,压缩和注入.

具有递归数据结构的函数式语言.


把协议当作非正式的接口.

协议不是Python发明的.Smalltalk团队,也就是面向对象的发明者,使用协议这个词表示现在我们称之为接口的特性.某些Smalltalk编程环境允许程序员把一组方法标记为协议,但这只不过是一种文档,用于辅助导航,语言不对其施加特定措施.因此,向熟悉正式(而且编译器会施加措施)接口的人解释"协议"时,我会简单地说它是非正式的接口.

动态类型语言中的既定协议会自然进化.所谓动态类型是指在运行时检查类型,因为方法签名和变量没有静态类型信息.Ruby是一门重要的面向对象动态类型语言,它也使用协议.


在Python文档中,如果看到 "文件类对象" 这样的表述,通常说的就是协议.这是一种简短的说法,意思是:行为基本与文件一致,实现了部分文件接口,满足上下文相关需求的东西.

你可能觉得只实现协议的一部分不够严谨,但是这样做的优点是简单.

模仿内置类型实现类时,记住一点:模仿的程度对建模的对象来说合理即可.例如,有些序列可能只需要获取单个元素,而不必提取切片.

不要为了满足过度设计的接口契约和让编译器开心,而去实现不需要的方法,我们要遵守KISS原则.

鸭子类型的起源

	我相信Ruby社区在鸭子类型这个术语的推广过程中起了主要作用,因为他们向大量Java使用者宣扬了这个说法.但是,在Ruby或Python流行起来之前,Python就使用这个术语了.根据维基百科,在面向对象编程中较早使用鸭子作比喻的是Alex Martelli.


安全地__format__方法,增强可用性

实现__format__方法时,我们没有采取措施防范Vector实例拥有大量分量,不过在__repr__方法中我们使用reprlib做了预防.这是因为repr()函数用于调试和记录日志,所以必须生成可用的输出;而__format__方法用于向最终用户显示输出,它们大概想看到整个Vector.如果你觉得这样做危险,可以再为格式规范微语言实现一个扩展.


寻找符合Python风格的求和方式


就像什么是美没有确切的答案一样,什么是Python风格也没有标准答案.如果回答地道的Python,不能让人100%满意,因为对你来说是地道的,在我看来却可能不是.但我可以肯定的是,地道并不是指使用最鲜为人知的语言特性.

如果你想计算列表中各个元素的和,写出的代码应该看起来像是在"计算元素之和",而不是迭代元素,维护一个变量t,在执行一系列求和操作.

如果不能站在一定高度上表明意图,让语言去关注底层操作,那么要高级语言干嘛?




"""