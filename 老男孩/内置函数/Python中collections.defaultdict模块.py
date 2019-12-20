# coding:utf-8

from collections import defaultdict
import collections
"""
认识defaultdict：
当我使用普通的字典时，用法一般是dict = {}, 添加元素的只需要dict[element] = value即，
调用的时候也是如此，dict[element] = xxx, 但前提是element字典里，如果不在字典里就会报错，如：


这时defaultdict就能排上用场了，defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值，这个默认值是什么呢，下面会说
如何使用defaultdict
defaultdict接受一个工厂函数作为参数，如下来构造：
dict = defaultdict(factory_function)

这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[]，str对应的是空字符串，set对应set()，int对应0，如下举例：


"""
dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] = 'two'

print(dict1[1])
print(dict3[1])
print(dict4[1])


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

print(list(d.items()))
print(d)
