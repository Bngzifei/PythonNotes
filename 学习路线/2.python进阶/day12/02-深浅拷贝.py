"""
不是底层语言的赋值就是引用,C语言那种才说地址赋值

"""

# --------------------对象之间的赋值本质上是引用传递<id一样,数据一样>--------------->
# 对象之间赋值都是引用传递<Java,Python这种高级语言赋值都是说引用传递>
# 不可变类型的拷贝是没有意义的.不可变类型只有赋值操作一说,赋值就是引用的传递
# 只要是对象赋值,就是引用传递

# 拷贝的目的是为了数据的独立性,实现   你操作你的那一份数据,我操作我的那一份数据,相互独立,互不影响
# -----------------------浅拷贝:只拷贝容器第一层的,如果容器内部还有容器类型数据,那只是拷贝了这个容器的引用--------------------------------------->
# 使用场景:如果有东西给别人使用,但是又不想把自己的东西让人使用,就拷贝,复制一份给别人
import copy

def modify_data(data):  # 隐含的是 data = d
	data[0] = '抽烟'
	print(data)  # ['抽烟', '喝酒', '烫头']
	print(id(data))  # 2735579457928


if __name__ == '__main__':
	d = ['冲浪', '喝酒', '烫头']
	# 完成对一个对象的拷贝<克隆> 里面的元素一样/类型一样,但是id不一样
	# 这一步的实际效果是把d对应的数据类型<容器>复制一个,把d的内部数据放到这个新的容器中
	# 就是拿了一个新的盒子来装复制之后的数据<元素>
	dd = copy.copy(d)
	modify_data(dd)  # 调用
	print(d)  # ['冲浪', '喝酒', '烫头']
	print(id(d))  # 2735579457672
"""
总结:没有完全拷贝,只拷贝数据的顶层结构  [1,2,3,4,x],x是一个数据的引用,x如果是一个列表,那么修改x,两个都会变

"""

# d1 = [1,2,3,4,(2,3)]
# d2 = copy.copy(d1)
# d2[3] = 8
# print(d1)  # [1, 2, 3, 4, (2, 3)]
# print(d2)  # [1, 2, 3, 8, (2, 3)]

# d1 = [1, 2, 3, 4, (2, 3)]
# d2 = copy.copy(d1)
# d2[4] = 8
# print(d1)  # [1, 2, 3, 4, (2, 3)]  外部的独立
# print(d2)  # [1, 2, 3, 4, 8]

# -------------------------深拷贝------------------------->
"""
递归的拷贝,所有的,第一层内部的[]里面的也要拷贝
不仅拷贝数据,引用,还拷贝引用里面对应的数据
x = [5,6]  a = [1,2,3,x] --> x' = [5,6]  b = [1,2,3,x']

总结:不仅拷贝数据,引用,还拷贝引用对应的数据
"""
import copy

d1 = [1, 2, 3, 4,[9,7]]
d2 = copy.deepcopy(d1)
d3 = copy.copy(d1)
d2[4][0]=19
print(d1)  # [1, 2, 3, 4, [9, 7]]
print(d2)  # [1, 2, 3, 4, [19, 7]]
print(d3)  # [1, 2, 3, 4, [19, 7]]

"""
浅拷贝的其他形式:
1.>c=[1,2,3,4], c[:]  g = c[:] 这样c和g就是独立的两份数据   切片也是浅拷贝
2.>字典/列表的copy()方法 也是一个浅拷贝
地址不一样,数据一样的就是浅拷贝


为啥大部分都是浅拷贝?
节约资源,效率高

深拷贝和浅拷贝 对于不可变类型<str,int,tuple>没有意义,全部都是引用传递<赋值>

不可变类型的拷贝是没有意义的.不可变类型只有赋值操作一说,赋值就是引用的传递

赋值就是引用传递
拷贝是id不一样,数据一样.

"""
# -----------------------不可变类型赋值-------------------------->
a = 100
b = a
a += 99  # 实际情况是a已经不再是原来a=100的那个引用了,a是一个新的引用了
print(a)  # 199
print(b)  # 100
# ------------------------可变类型赋值----------------------->
c = [1,2]
d = c
d += [3]
print(c)  # [1, 2, 3]
print(d)  # [1, 2, 3]

# --------------------------深浅拷贝------------------------------------>
b = [9,9,9]
a = [1,2,3,b]
c = copy.copy(a)
d = copy.deepcopy(a)

a[0] = 9

print(c)  # [1,2,3,[9,9,9]]
print(d)  # [1,2,3,[9,9,9]]
# a 变了,但是c 和 d 是独立的  所以c和d不会变化
print(a)  # [9,2,3,[9,9,9]]












