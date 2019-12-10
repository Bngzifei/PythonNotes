"""
不要检查它是不是鸭子,它的叫声像不像鸭子,它的走路姿势像不像鸭子,等等.具体检查什么取决于你想使用语言的哪些行为.

基本的序列协议----__len__和__getitem__


正确表述拥有很多元素的实例


适当的切片支持,用于生成新的Vector实例


综合各个元素的值计算散列值


自定义的格式语言扩展


此外,我们还将通过__getattr__方法实现属性的动态获取,以此取代Vector2d使用的只读特性---不过,序列类型通常不会这么做.

在大量代码之间,我们将穿插讨论一个概念:把协议当作正式的接口.我们将说明协议和鸭子类型之间的关系,以及对自定义类型的实际影响.



三维以上向量的应用:


谁需要1000维向量呢?提示:不是3D艺术家.不过,信息检索领域经常使用n维向量(n是很大的数),查询的文档和文本使用向量表示,一个单词一个维度.这叫向量空间模型.在这个模型中,一个关键的相关指标是余弦相关性(即查询向量与文档向量夹角的余弦).夹角越小,余弦值越趋近于1,文档与查询的相关性就越大.


gensim使用NumPy和SciPy实现了用于处理自然语言和检索信息的向量空间模型.



vector_v1.py
"""
from array import array
import reprlib
import math

class Vector:

	typecode = "d"

	def __init__(self,compontents):
		# self._compontents是受保护的实例属性.
		self._compontents = array(self.typecode,compontents)

	def __iter__(self):
		"""构建一个迭代器"""
		return iter(self._compontents)

	def __repr__(self):
		"""使用reprlib.repr()函数获取self._compontents的有限长度表示形式."""
		compontents = reprlib.repr(self._compontents)
		compontents = compontents[compontents.find("["):-1]
		return "Vector({})".format(compontents)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(self._compontents))

	def __eq__(self,other):
		return tuple(self) == tuple(other)

	def __abs__(self):
		return math.sqrt(sum(x * x for x in self))

	def __bool__(self):
		return bool(abs(self))

	@classmethod 
	def frombytes(cls,octets):
		typecode = chr(octets)
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv)

"""
我使用reprlib.repr的方式需要做些说明.这个函数用于生成大型结构或递归结构的安全表示形式,它会限制输出字符串的长度,用"..."表示截断的部分.我希望Vector实例的表示形式是Vector([3.0,4.0,5.0])这样,而不是Vector(array("d",[3.0,4.0,5.0])),因为Vector实例中的数组是实现细节.因为这种两种构造方法的调用方式所构建的Vector对象是一样的,所以我选择使用更简单的句法,即传入列表参数.

编写__repr__方法时,本可以使用这个表达式生成简化的compontents显示形式.


调用repr()函数的目的是调试,因此绝对不能抛出异常.如果__repr__方法的实现由问题,那么必须处理.尽量输出有用内容,让用户能够识别目标对象.


注意,__str__,__eq__和__bool__方法与Vector2d类中的一样


顺便说一下,我们本可以让Vecttor继承Vector2d,但是我没这么做,原因有二.其一,两个构造方法不兼容,因此不建议继承.这一点可以通过适当处理__init__方法的参数解决.不过第二个原因更重要:我想把Vector类当作单独的示例,以此实现序列协议.


"""