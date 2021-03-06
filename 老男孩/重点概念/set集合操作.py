"""
集合:无序,不重复
作用:1.>去重 2.> 关系测试<测试两组数据之间的交集,差集,并集,对称差集等关系>

可变类型的集合的更新操作:
add:添加元素
update:更新,添加
remove:删除集合中指定的元素
del:删除集合本身,即把集合这个容器删除
"""

# a = {1, 2, 3, 4, 5, 6, 7}
# b = {11, 12, 13, 4, 15, 6, 7}
#
# print(a.intersection(b))  # 交集<二者均有的元素> {4, 6, 7}
#
# # {1, 2, 3, 5}
# print(a.difference(b))  # 差集<所有属于a且不属于b的元素构成的集合>
# # {1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 15}
# print(a.union(b))  # 并集<a和b中所有的元素>
# # {1, 2, 3, 5, 11, 12, 13, 15}
# print(a.symmetric_difference(b))  # 对称差集:也叫反向交集<并集 - 交集>   {1, 2, 3, 5, 11, 12, 13, 15}

A = {1, 2, 3}
B = {1, 2}
print(B.issubset(A))  # B是否是A的子集    super:超,代表父一级,sub:代表子一级
print(A.issuperset(B))  # A是否是B的超集(父集)

"""符号表示:这种更常用"""

A = {1, 2, 3}
B = {1, 2, 4}

print((A | B))  # 并集
print((A & B))  # 交集
print((A - B))  # 差集
print((A ^ B))  # 对称差集  {3, 4}  就是  并集 - 交集


"""
可变集合和不可变集合:

可变set:可以添加,删除元素,不可哈希的(因为是可变数据类型)

不可变 frozenset :和元组一样,不可修改,删除.一旦定义创建之后就不能被修改

"""
