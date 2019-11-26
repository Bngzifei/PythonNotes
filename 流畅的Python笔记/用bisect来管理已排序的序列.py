"""
bisect模块包含两个主要函数,bisect和insort,两个函数都利用二分查找算法来在
有序序列中查找或插入元素.

1.>用bisect来搜索
	bisect(haystack,needle) 在haystack(干草垛:比喻如大海捞针般难找)里搜索needle(针)
	的位置,该位置满足的条件是:把needle插入这个位置之后,haystack还能保持升序.也就是
	在说这个函数返回的位置前面的值,都小于或等于needle的值.其中haystack必须是一个有序的序列.
	你可以先用bisect(haystack,needle)查找位置index,再用haystack.insert(index,needle)
	来插入新值.但你也可用insort来一步到位,并且后者的速度更快一些.



"""

# 在有序序列中用bisect查找某个元素的插入位置
import bisect
import sys


HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

ROW_FMT = "{0:2d} @ {1:2d}  {2}{0:<2d}"

def demo(bisect_fn):
	for needle in reversed(NEEDLES):
		position = bisect_fn(HAYSTACK,needle)
		offset = position * "     |"
		print(ROW_FMT.format(needle,position,offset))



if __name__ == '__main__':
	
	if sys.argv[-1] == "left":
		bisect_fn = bisect.bisect_left
	else:
		bisect_fn = bisect.bisect_right


	print("DEMO:",bisect_fn.__name__)
	print("haystack ->","    ".join("%2d" % n for n in HAYSTACK))
	demo(bisect_fn)

"""
bisect可以用来建立一个用数字作为索引的查询表格,比如说把分数和成绩对应起来.
成绩指的是在美国大学中普遍使用的A~F字母成绩,A表示优秀,F表示不及格.


它们可以在很长的有序序列中作为index的替代,用来更快地查找一个元素的位置.

"""

print("==================>")

def grade(score,breakpoints=[60,70,80,90],grades="FDCBA"):
	i = bisect.bisect(breakpoints,score)
	return grades[i]


print([grade(score) for score in [33,99,77,70,80,90,100]])


"""
	用bisect.insort插入新元素

	排序很耗时,因此在得到一个有序序列之后,我们最好能够保持它的有序.
	bisect.insort就是为了这个而存在的.

	insort(seq,item)把变量item插入到序列seq中,并能保持seq的升序顺序.


	insort和bisect意义,有lo和hi两个可选参数来控制查找的范围.它也有个
	变体叫insort_left,这个变体在背后用的是bisect_left


	目前所提到的内容都不仅仅是对列表或者元组有效,还可以应用于几乎所有
	的序列类型上.有时候因为列表实在是太方便了,所以Python程序可能都会
	过度使用它.反正我知道我犯过这个毛病.而如果你只需要处理数字列表的话,
	数组可能是个更好的选择.
"""

print("=====================================>")


import bisect
import random

SIZE  =7

random.seed(1729)

my_list = []

for i in range(SIZE):
	new_item = random.randrange(SIZE*2)
	bisect.insort(my_list,new_item)
	print("%2d ->"%new_item,my_list)



"""
当列表不是首选时:

虽然列表既灵活又简单,但面对各类需求时,我们可能会有更好的选择.比如,
要存放1000万个浮点数的话,数组(array)的效率要高得多,因为数组在背后
存的并不是float对象,而是数字的机器翻译,也就是字节表述.这一点就跟C
语言中的数组一样.再比如说,如果需要频繁对序列做先进先出的操作,deque
(双端队列)的速度应该会更快.
	
	如果在你的代码里,包含操作(比如检查一个元素是否出现在一个集合中)的
	频率很高,用set(集合)会更合适.set专为检查元素是否存在做过优化.但是它
	并不是序列,因为set是无序的.



数组:

	如果我们需要一个只包含数字的列表,那么array.array比list更高效.数组支持
	所有跟可变序列有关的操作,包括 .pop, .insert和 .extend. 另外,数组还
	提供从文件读取和存入文件的更快的方法,如 .frombytes和 .tofile.

Python数组跟C语言数组一样精简.创建数组需要一个类型码,这个类型码用来表示在
底层	的C语言应该存放怎样的数据类型.比如b类型码代表的是有符号的字符(signed char),
因此array("b")创建出的数组就只能存放一个字节大小的整数,范围从-128到127,这样在序列
很大的时候,我们能节省很多空间.而且Python不会允许你在数组里存放除指定类型之外的数据(
这意思就是只能存放同一种类型的数据,因为设定的数据类型的大小有限制)

下面的例子展示了从创建一个有1000万个随机浮点数的数组开始,到如何把这个数组存放到
文件里,再到如何从文件读取这个数组.


"""
from array import array
from random import random

floats = array("d",(random() for i in range(10**7)))

print("***************>>>")
print(floats[-1])
fp = open("floats.bin","wb")
floats.tofile(fp)
fp.close()
floats2 = array("d")
fp = open("floats.bin","rb")
floats2.fromfile(fp,10**7)
fp.close()
print(floats2[-1])
print(floats == floats2)


"""
从上面的代码我们能得出结论:array.tofile和array.fromfile用起来很简单,
把这段代码跑一遍,你还会发现它的速度也很快.一个小实验告诉我,用array.fromfile
从一个二进制文件里读出1000万个双精度浮点数只需要0.1秒,这比从文本文件里读取
的速度要快60倍,因为后者会使用内置的float方法把每一行文字转换成浮点数.

另外,使用array.tofile写入到二进制文件,比以每行一个浮点数的方式把所有数字写入到
文本文件要快7倍.另外,1000万个这样的数在二进制文件里只占用80000000个字节(每个浮点
数占8个字节,不需要额外空间),如果是文本文件的话,我们需要181515739个字节.


另外一个快速序列化数字类型的方法是使用pickle模块.pickle.dump处理浮点数组的速度几乎
跟array.tofile一样快.不过前者可以处理几乎所有的内置数字类型,包含复数,嵌套集合,甚至用户自定义
的类.前提是这些类没有什么特别复杂的实现.



还有一些特殊的数字数组,用来表示二进制数据,比如光栅图像.里面涉及的bytes和bytearray类型.


从Python3.4开始,数组类型不再支持诸如list.sort()这种就地排序的方法.要给数组排序的话,得用
sorted函数新建一个数组.

	a = array.array(a.typecode,sorted(a))
	想要在不打乱次序的情况下为数组添加新的元素,bisect.insort还是能派上用场.

	如果你总是跟数组打交道,却没有听过memoryview,那就太遗憾了.下面就来谈谈memoryview.


内存视图:
	memoryview是一个内置类,它能让用户在不复制内容的情况下操作同一个数组的不同切片.memoryview
	的概念受到了NumPy的启发.	

	内存视图其实是泛化和去数学化的NumPy数组.它让你在不需要复制内容的前提下,在数据结构之间共享内存.其中
	数据结构可以是任何形式,比如PIL图片,SQLite数据库和NumPy的数组,等等.
	这个功能在处理大型数据集合的时候非常重要.	

memoryview.cast的概念跟数组模块类似,能用不同的方式读写同一块内存数据,而且内容字节不会随意移动.
这听上去又跟C语言中的类型转换的概念差不多.memoryview.cast会把同一块内存里的内容打包成一个全新的memoryview
对象给你.


"""


print("------------------------->>>")
# 通过改变数组中的一个字节来更新数组里某个元素的值
import array

numbers = array.array("h",[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))  # 5
print(memv[0])  # -2
memv_oct = memv.cast("B")
print(memv_oct.tolist())  # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
print(memv_oct[5])  # 0

# 因为我们把占两个字节的整数的高位字节改成了4,所以这个有符号整数的值就变成了1024
memv_oct[5] = 4
print(numbers)  # array('h', [-2, -1, 1024, 1, 2])



"""
另外,如果利用数组来做高级的数字处理是你的日常工作,那么NumPy和SciPy应该是你的常用武器.
"""













