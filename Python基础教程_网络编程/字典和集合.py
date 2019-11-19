"""

正是因为字典至关重要,Python对它的实现做了高度优化,而散列表则是字典类型性能出众的根本原因.

集合的实现其实也依赖于散列表.想要进一步理解集合和字典,就得先理解散列表的原理.

然而,非抽象映射类型一般不会直接继承这些抽象基类,它们会直接对dict或是collections.User.Dict
进行扩展.这些抽象基类的主要作用是作为形式化的文档,它们定义了构建一个映射类型所需要的最基本的
接口.然后它们还可以跟isinstance一起被用来判定某个数据是不是广义上的映射类型.


>>>from collections import abc

>>>my_dict = {}

>>>isinstance(my_dict,abc.Mapping)
True


这里用isinstance而不是type来检查某个参数是否为dict类型,因为这个参数有可能不是dict,而是一个比较
另类的映射类型.


标准库里的所有映射都是利用dict来实现的,因此它们有个共同的限制,即只有可散列的数据类型才能用作这些映射
里的键(只有键有这个要求,值并不需要是可散列的数据类型).


	问:什么是可散列的数据类型?
		
		官方解释:
		一个目的是可哈希如果它有一个哈希值其寿命（它需要一个在这期间从不改变__hash__()方法），
		并且可相对于其他对象（它需要一个__eq__()方法）。
		比较相等的可哈希对象必须具有相同的哈希值。

		散列性使对象可用作字典键和set成员，因为这些数据结构在内部使用散列值。

		Python的大多数不可变内置对象都是可哈希的；可变容器（例如列表或字典）不是；
		不可变容器（例如元组和Frozensets）仅在其元素可哈希化时才可哈希化。默认情况下，作为用户定义类实例的对象是可哈希的。
		它们都比较不相等（除了它们本身），并且它们的哈希值从中得出id()。

		原子不可变数据类型(str,bytes和数值类型)都是可散列类型,frozenset也是可散列的,因为根据其定义,frozenset里只能容纳
		可散列类型.元组的话,只有当一个元组包含的所有元素都是可散列类型的情况下,它才是可散列的.
	

错误的说法:Python里所有的不可变类型都是可散列的.
	原因:比如虽然元组本身是不可变序列,它里面的元素可能是其他可变类型的引用.一般来讲用户自定义的类型的对象都是可散列的,散列
	值就是它们的id()函数的返回值,所以所有这些对象在比较的时候都是不相等的.如果一个对象实现了__eq__方法,并且在方法中用到了
	这个对象的内部状态的话,那么只有当所有这些内部状态都是不可变的情况下,这个对象才是可散列的


字典推导式：
"""
DIAL_CODES = [
		(86,"China"),
		(91,"India"),
		(1,"United States"),
		(62,"Indonesia"),

]


country_code = {country:code for code,country in DIAL_CODES}
print(country_code)  # {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62}

ss = {code:country.upper() for country,code in country_code.items() if code < 66}
print(ss)  # {1: 'UNITED STATES', 62: 'INDONESIA'}


"""

常见的映射方法:

	*default_factory并不是一个方法,屙屎一个可调用对象(callable),它的值在defaultdict初始化的时候由用户设定.

	OrderedDict.popitem()会移除字典里最先插入的元素(先进先出):同时这个方法还有一个可选的last参数,若为真,则会
	移除最后插入的元素(后进先出).


字典更新方法说明:
d.update(m,[**kargs]):m可以是映射或者键值对迭代器,用来更新d里对应的条目.

update方法处理参数m的方式,是典型的"鸭子类型".函数首先检查m是否有keys方法,如果有,那么update函数就把它当做映射对象来处理.
否则.函数会退一步,转而把m当做包含了键值对元素的迭代器.Python里多数映射类型的构造方法都采用了类似的逻辑,因此你既可以用一个
映射对象来新建一个映射对象,也可以用包含(key,value)元素的可迭代对象来初始化一个映射对象.


在映射对象的方法里,setdefault可能是比较微妙的一个.我们虽然并不会每次都用它,但是一旦它发挥作用,就可以节省不少次键查询,
从而让程序更高效.

用setdefault处理找不到的键:
	
	当字典d[k]不能找到正确的键的时候,Python会抛出异常,这个行为符合Python所信奉的"快速失败的哲学".也学每个Python程序员都知道
	可以使用d.get(k,default)来代替d[k],给找不到的键一个默认的返回值(这比处理KeyError要方便不少).但是要更新某个键对应的值的
	时候,不管使用__getitem__还是get都会不自然.而且效率低.

	dict.get并不是处理找不到的键的最好方法.




"""

print("***************>>>")


import sys
import re


WORD_RE = re.compile(r"\w+")

index = {}


with open(sys.argv[1], encoding="utf-8") as fp:
	for line_no,line in enumerate(fp,1):
		for match in WORD_RE.finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no,column_no)
			# 这其实是一种很不好的实现,这样写只是为了证明论点
			occurrences = index.get(word,[])
			occurrences.append(location)
			index[word] = occurrences

for word in sorted(index,key=str.upper):
	print(word,index[word])

"""

my_dict.setdefault(key,[]).append(new_value)
这么写和:

if key not in my_dict:
	my_dict[key] = []
my_dict[key].append(new_value)

二者的效果是一样的,只不过后者至少需要进行两次键查询----如果键不存在的话,
就是三次,用setdefault只需要一次就可以完成整个操作.

那么,在单纯地查找取值(而不是通过查找来插入新值)的时候,该怎么处理找不到的键呢?


"""