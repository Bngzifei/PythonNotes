"""

list.sort方法会就地排序列表,也就是说不会把原列表复制一份.

这也是这个方法的返回值是None的原因(就是在自己列表内部直接进行一个排序,
没有新建一个列表来存放排序后的元素值).提醒你本方法不会新建一个列表.
在这种情况下返回None其实是Python的一个惯例:如果一个函数或者非法对
对象进行的是就地改动,那它就应该返回None,好让调用者知道传入的参数发生了
变动,而且并未产生新的对象.例如:random.shuffle函数也遵守了这个惯例.

用返回None来表示就地改动这个惯例有个弊端,那就是调用者无法将其串联起来.
而返回一个新对象的方法(比如说str里的所有方法)则正好相反,它们可以串联起来调用,
从而形成连贯接口.


连贯接口:连贯接口（fluent interface），有时候也会叫做方法链(链式调用)，
可以起到简化编码的作用，同时保持对象间的贯通一致。

与list.sort方法相反的是内置函数sorted,它会新建一个列表作为返回值.
这个函数可以接受任何形式的可迭代对象作为参数,甚至包括不可变序列或生成器.
而不管sorted接受的是怎样的参数,它最后都会返回一个列表.


sorted(可迭代对象)  --> 返回一个列表


不管是list.sort方法还是sorted函数,都有两个可选的关键字参数.

1.>reverse:如果被设定为True,被排序的序列里的元素会议降序输出(也就是说把最大值当作
最小值来排序).这个参数的默认值是False

2.>key:一个只有一个参数的函数,这个阿寒湖会被用在序列里的每一个元素上,所产生的结果
将是排序算法依赖的对比关键字.比如说,在对一些字符串排序时,可以使用key=str.lower来实现
忽略大小写的排序.或者是用key=len进行基于字符串长度的排序.这个参数的默认值是恒等函数,
也就是默认用元素自己的值来排序.

	可选参数key还可以在内置函数min()和max()中起作用.另外,还有些标准库里的函数也接受这个
	参数,像itertools.groupby()和heapq.nlargest()等.



下面通过几个小例子来看看这两个函数和它们的关键字参数:

说明:这几个例子说明了Python的排序算法----Timsort(介绍链接:https://blog.csdn.net/yangzhongblog/article/details/8184707)
是稳定的,意思是就算两个元素比不出大小,在每次排序的结果里它们的相对位置是固定的.


"""

fruits = ["grape","raspberry","apple","banana"]


print(sorted(fruits))  # 输出:['apple', 'banana', 'grape', 'raspberry']
# 是按照字母的ascii大小进行排序的

print(sorted(fruits,reverse=True))  # 输出:['raspberry', 'grape', 'banana', 'apple']  倒序排列


print(sorted(fruits,key=len))   # 输出:['grape', 'apple', 'banana', 'raspberry']
# 新建一个按照长度排序的字符串列表.
# 指定排序规则为元素的长度,因为这个排序算法是稳定的,
# grape和apple的长度都是5,它们的相对跟在原来的列表里是一样的.

print(sorted(fruits,key=len,reverse=True))  # 输出:['raspberry', 'banana', 'grape', 'apple']
# 按照长度降序排序的结果.
# 结果并不是上面那个结果的完全翻转,因为用到的排序算法是稳定的,也就是说,在长度一定时,
# grape和apple的相对位置不会改变.



# 使用list.sort()就地排序,返回值None会被控制台忽略
print(fruits.sort())  # 输出:None

# 此时,fruits本身被排序
print(fruits)  # 输出:['apple', 'banana', 'grape', 'raspberry']

"""

已排序的序列可以用来进行快速搜索,而标准库的bisect模块给我们提供了二分查找算法.
"""