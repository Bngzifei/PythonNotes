# 不能进行增.删.改,其余的规则和列表一样,元组用的不多
"""
格式:(元素1,元素2...)
只能进行查询,不能对其进行增.删.改
元组(索引)
"""

tuple1 = ("zhang", 18, 15.87, True)
print(tuple1)
print(type(tuple1))
print(tuple1[0])
# tuple1[0] = 6  TypeError: 'tuple' object does not support item assignment
tuple1 = (50)
print(type(tuple1))  # <class 'int'>
tuple1 = (50,)  # 如果元组中只有一个元素时,会自动进行类型推导,需要加个,号
print(type(tuple1))