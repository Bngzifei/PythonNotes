"""
有时候为了方便起见,就算某个键在映射里不存在,我们也希望在通过这个键读取值的时候能
得到一个默认值.有两个途径能帮我们达到这个目的,一个是通过defaultdict这个类型而不
是普通的dict,另一个是自己定义一个dict的子类,然后在子类中实现__missing__方法.


	1.>defaultdict:处理找不到的键的一个选择:

		具体而言,在实例化一个defaultdict的时候,需要给构造方法提供一个可调用对象,
		这个可调用对象会在__getitem__碰到找不到的键的时候被调用,让__getitem__返回
		某种默认值.

		比如,我们新建了这样一个字典:dd = defaultdict(list),如果键new-key在dd中还不存
		在的话,表达式dd["new-key"]会按照以下的步骤来行事:
		(1)调用list()来建立一个新列表
		(2)把这个新列表作为值,"new-key"作为它的键,放到dd中
		(3)返回这个列表的引用

		而这个用来生成默认值的可调用对象放在名为default_factory的实例属性里.

如果在创建defaultdict的时候没有指定default_factory,查询不存在的键会触发KeyError.

defaultdict里的default_factory只会在__getitem__里被调用,在其他的方法里完全不会发挥作用.
比如:dd是个defaultdict,k是个找不到的键,dd[k]这个表达式会调用default_factory创造某个默认值,
而dd.get(k)则会返回None


所有这一切背后的功臣其实是特殊方法__missing__.它会在defaultdict遇到找不到的键的时候调用default_factory,
而实际上这个特性是所有映射类型都可以选择去支持的.



特殊方法__missing__:
	
	所有的映射类型在处理找不到的键的时候,都会牵扯到__missing__方法.这也是这个方法称作"missing"的原因.
	虽然基类dict并没有定义这个方法,但是dict是知道有这么个东西存在的.也就是说,如果有一个类继承了dict,然后这个
	继承类提供了__missing__方法,那么在__getitem__碰到找不到的键的时候,Python就会自动调用它,而不是抛出一个KeyError
	异常.

__missing__方法只会被__getitem__调用(比如在表达式d[k]中).提供__missing__方法对get或者__contains__(in 运算符会用到
这个方法)这些方法的使用没有影响.这也是defaultdict中的default_factory只对__getitem__起作用的原因.



"""		


# StrKeyDict0在查询的时候把非字符串的键转换为字符串:

class StrKeyDict0(dict):

	def __missing__(self,key):
		if isinstance(key,str):
			raise KeyError(key)
		return self[str(key)]

	def get(self,key,default=None):
		try:
			# get 方法把查找工作用self[key]的形式委托给__getitem__,
			# 这样在宣布查找失败之前,还能通过__missing__再给某个键一个机会.
			return self[key]
		except KeyError:
			return default

	def __contains__(self,key):
		return key in self.keys() or str(key) in self.keys()

"""

像k in my_dict.keys()这种操作在Python3中是很快的,而且即便映射类型对象很庞大也没关系.
这是因为dict.keys()的返回值是一个视图.视图就像一个集合,而且跟字典类似的是,在视图里查找
一个元素的速度很快.Python2的dict.keys()返回的是个列表,因此虽然上面的方法仍然是正确的,
它在处理体积大的对象的时候效率不会太高,因为k in my_list操作需要扫描整个列表.


字典的变种:

我们已经见识过 dict 和 defaultdict 了。但是标准库里面还
有很多其他的映射类型.

1.collectionsOrderedDict:
	
	这个类型在添加键的时候会保持顺序,因此键的迭代次序总是一致的.OrderedDict的popitem方法默认
	删除并返回的是字典里的最后一个元素,但是如果像my_odict.popitem(last=False)这样调用它,那么
	它删除并返回第一个被添加进去的元素.

2.collections.ChainMap:
	
	该类型可以容纳数个不同的映射对象,然后在进行键查找操作的时候,这些对象会被当做一个整体被逐个
	查找.直到键被找到为止.这个功能在给有嵌套作用域的语言做解释器的时候很有用,可以用一个映射对象
	来代表一个作用域的上下文.

3.collections.Counter:

	这个映射类型会给键准备一个整数计数器.每次更新一个键的时候都会增加这个计数器.所以这个类型可以
	用来给可散列表对象计数,或者是当成多重集来用----多重集合就是集合里的元素可以出现不止一次.Counter
	实现了+和-运算符用来合并记录,还有像most_common([n])这类很有用的方法.most_common([n])会按照
	次序返回映射里最常见的n个键和它们的计数.

4.collections.UserDict:
	
	这个类其实就是把标准dict用纯Python又实现了一遍.
	而更倾向于从UserDict而不是从dict继承的主要原因是,后者有时会在某些方法的实现上走一些捷径,导致我们
	不得不在它的子类中重写这些方法,但是UserDict就不会带来这些问题.

	另外一个值得注意的地方是:UserDict并不是dict的子类,但是UserDict有一个叫做data的属性,是dict的实例,
	这个属性实际上是UserDict最终存储数据的地方.这样做的好处是,UserDict的子类就能在实现__setitem__的时候
	避免不必要的递归,也可以让__contains__里的代码更简洁.

	




"""