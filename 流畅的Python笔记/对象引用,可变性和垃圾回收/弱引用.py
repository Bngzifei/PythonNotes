"""
正是因为有引用,对象才会在内存中存在.当对象的引用数量归零后,垃圾回收程序会把对象销毁.但是,有时需要引用对象,而不让对象存在的时间超过所需时间.这经常用在缓存中.

弱引用不会增加对象的引用数量.引用的目标对象称为所指对象(refrent).因此我们说,弱引用不会妨碍所指对象呗当作垃圾回收.


弱引用在缓存应用中很有用,因为我们不想仅因为被缓存引用着而始终保存缓存对象.


示例展示了如何使用weakref.ref实例获取所指对象.如果对象存在,调用弱引用可以获取对象;否则返回None


示例8-17是一个控制台会话.Python控制台会自动把_变量绑定到结果不为None的表达式结果上.这对我想演示的行为有影响,不过却凸显了一个实际问题:微观管理内存时,往往会得到意外的结果,因为不明显的隐式赋值会为对象创建新引用.控制台中的_变量是一例.调用跟踪对象也常导致意料之外的引用.


弱引用是可调用对象,返回的是被引用的对象;如果所指对象不存在了,返回None

weakref类其实是低层接口,供高级用途使用.多数程序最好使用weakref集合和finalize.也就是说,应该使用WeakKeyDictionary,WeakValueDictionary,WeakSet和
finalize(在内部使用弱引用),不要自己动手创建并处理weakref.ref实例.


WeakValueDictionary简介:

	WeakValueDictionary类实现的是一种可变映射.里面的值是对象的弱引用.被引用的对象在程序中的其他地方被当作垃圾回收后,对应的键会自动从WeakValueDictionary中删除.因此,WeakValueDictionary经常用于缓存.


Cheese有个kind属性和标准的字符串表示形式

"""

class Cheese:

	def __init__(self,kind):
		self.kind = kind

	def __repr__(self):
		return "Cheese(%r)" % self.kind


import weakref
stock = weakref.WeakValueDictionary()  # stock是WeakValueDictionary实例
catalog = [Cheese("Red Leicester"),Cheese("Tilsit"),Cheese("Brie"),Cheese("Parmesan")]
for cheese in catalog:
	stock[cheese.kind] = cheese  # stock把奶酪的名称映射到catalog中Cheese实例的弱引用上.

print(sorted(stock.keys()))  # ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']  stock是完整的

del catalog

print(sorted(stock.keys()))  # ['Parmesan']  删除catalog之后,stock中的大多数奶酪都不见了,这是WeakValueDictionary的预期行为.为什么不是全部呢?

del cheese
print(sorted(stock.keys()))  # []


"""
临时变量引用了对象,这可能会导致该变量存在时间比预期长.通常,这对局部变量来说不是问题,因为它们在函数返回时会被销毁.但在示例中,for循环中的变量cheese是全局变量,除非显式删除,否则不会消失.


与WeakValueDictionary对应的是WeakKeyDictionary,后者的键是弱引用.weakref.WeakKeyDictionary的文档.

WeakKeyDictionary实例可以为应用中的其他部分拥有的对象附加数据,这样就无需为对象添加属性.这对覆盖属性访问权限的对象尤其有用.

weakref模块还提供了WeakSet类.按照文档的说明,这个类的作用很简单:保存元素弱引用的集合类.元素没有强引用时,集合会把它删除.如果一个类需要知道所有实例,一种好的方案是创建一个WeakSet类型的类属性,保存实例的引用.如果使用常规的set,实例永远不会被垃圾回收.因为类中有实例的强引用,而类存在的时间与Python进程一样长,除非显式删除类.



弱引用的局限:
	
	不是每个Python对象都可以作为弱引用的目标(或所指对象).基本的list和dict实例不能作为所指对象,但是它们的子类可以轻松地解决这个问题:
	
"""

class Mylist(list):
	"""list的子类,实例可以作为弱引用的目标"""

a_list = Mylist(range(10))

# a_list可以作为弱引用的目标
wref_to_a_list = weakref.ref(a_list)

"""
set实例可以作为对象,因此示例才使用set实例.用户定义的类型也没问题,这就解释了示例为什么使用那个简单的Cheese类.但是,int和tuple实例不能作为弱引用的目标,甚至它们的子类也不行.

这些局限基本上是CPython的实现细节,在其他Python解释器中情况可能不一样.这些局限是内部优化导致的结果.



"""