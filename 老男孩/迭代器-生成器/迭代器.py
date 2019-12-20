"""
递归:自己调自己
迭代:能使用for循环遍历  更新换代  依赖于父亲 ,每次出来的结果都依赖于上一次的结果

迭代器协议:是指对象必须提供一个next方法,执行该方法要么返回迭代中的下一项,要么引起一个
StopIteration异常,以终止迭代(只能往后走不能往前退)

可迭代对象:实现了迭代器协议的对象(如何实现:对象内部定义一个__iter__()方法)


协议:就是一种规定,可迭代对象实现了迭代器协议,Python的内部工具如for循环,max()函数等使用
迭代器协议访问对象

Python中强大的for循环机制:
for循环的本质:循环所有对象,全部是使用迭代器协议.

很多人会想,for循环的本质就是遵循迭代器协议去访问对象,那么循环的对象肯定都是迭代器了啊,没错,那既然这样,
for循环可以遍历(字符串,列表,元组,,字典,集合,文件对象),那么这些类型的数据肯定都是可迭代对象啊?
但是,为什么定义一个列表l=[1,2,3]没有l.next()方法?
解释:
(字符串,列表,字典,集合,文件对象等)这些都不是可迭代对象,只不过在for循环里,调用了他们内部的
__iter__()方法,把他们变成了可迭代对象.
然后for循环调用可迭代对象的__next__()方法去取值,而且for循环会捕捉StopIteration异常,以终止迭代.


序列类型:字符串,元组,列表.就是有序的可以使用索引取值
非序列类型:字典,集合,文件对象

所以提供for循环提供了一个统一的可以遍历所有对象的方法.即在遍历之前,先调用对象的__iter__()方法,将其转成
一个迭代器,然后使用迭代器协议去实现循环访问.这样所有的对象就可以通过for循环来遍历了.


"""

# l = [1, 2, 3]
# # for i in l:  # 1.先执行 l1 = i.__iter__()方法,然后执行l1.__next__()方法
# # 	print(i) # 3. 然后在取不出来的时候去捕获异常 StopIteration
#
# # print(l[0])  # 法1 下标法  for循环和索引无关
# index = 0
# while index <= len(l) - 1:
# 	print(l[index])
# 	index += 1

# iter_l = l.__iter__()  # 法2 迭代器法: 遵循迭代器协议,生成可迭代对象
# print(iter_l.__next__())
# print(iter_l.__next__())
# print(iter_l.__next__())

"""
字符串:
"""
# x = 'hello'
# iter_test = x.__iter__()
# print(iter_test)  # <str_iterator object at 0x000001F1216AA780>
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())
# print(iter_test.__next__())  # StopIteration  生不出了,报错

# 集合
# s = {1, 2, 4}
# # for i in s:
# # 	print(i)
#
# iter_s = s.__iter__()
# print(iter_s)  # <set_iterator object at 0x000001DE76FE85E8>
# print(iter_s.__next__())
# print(iter_s.__next__())
# print(iter_s.__next__())

# 只要是可以被for遍历的都是有一个__iter__()方法


# 字典
# dic = {'a':1,'b':2}
# iter_d = dic.__iter__()
# print(iter_d.__next__())
# print(iter_d.__next__())

# 文件对象  推荐使用这种方法,因为在使用的时候才会调用取到内存中,用完就回收掉,
# 不会直接全部放到内存中.
# f = open('test.txt', 'r+')
# # for i in f:  # 实际在调用f的__iter__()方法
# print(f.__iter__())
# print(f.__iter__().__next__(), end='')
# print(f.__iter__().__next__(), end='')
# print(f.__iter__().__next__(), end='')
# print(f.__iter__().__next__(), end='')
# print(f.__iter__().__next__(), end='')
# print(f.__iter__().__next__().encode('cp936', errors='strict').decode('cp936'),end='')
# print(f.__iter__().__next__().encode('cp936', errors='strict').decode('cp936'))
# print(f.__iter__().__next__().encode('cp936', errors='strict').decode('cp936'))


"""使用while 循环模拟for循环工作机制"""

# l = [1, 2, 3]
# iter_l = l.__iter__()
# while True:
# 	try:
# 		print(iter_l.__next__())
# 	# except Exception as StopIteration:
# 	except StopIteration:
# 		print('迭代完毕了,循环终止了')
# 		break


"""迭代器补充:截然不同的存在形式"""

l = ['die','erzi','sunzi','chongsun']  # 一次全部加载到内存
iter_l = l.__iter__()  # 只是存了一个地址,每次用一个,就往内存中取一个
# print(iter_l.__next__())  # die
# print(iter_l.__next__())  # erzi
# print(iter_l.__next__())  # sunzi
# print(iter_l.__next__())  # chongsun
#

# 内置函数next()实际就是在调用iter_l的__next__()方法
print(next(iter_l))  # next()实际就是在调用iter_l的__next__()方法
print(next(iter_l))
print(next(iter_l))
print(next(iter_l))

# 理解:迭代器就是可迭代对象,就是一回事
# 只要遵循迭代器协议,就是可迭代对象

















