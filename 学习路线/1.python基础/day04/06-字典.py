# 所有的编程语言都有字典这种数据类型,用法都一样
# 描述一个物体相关信息,一对
# 数据类型不一样,意思也不一样,不同类型,但是这些数据联合在一起都表示同一个物体的信息
# 值可以是任何数据类型,键只能使用字符串.数字或元组,通常键只用字符串表示(为了和其他语言保持一致)
# 键必须是唯一的
# 没有真正的索引,所以是无序的,打印输出会出现顺序不一致的情况
"""
作用:描述一个物体的信息,类型可以不同
格式:{key1:value1,key2:value2...}
字典[key]
key唯一
"""
dict1 = {"name": "zhangshan", "age": 18, "boy": True, "name": "456"}  # 如果key重复了,value会取最后的那个key对应的value
# 个数 = ,数 + 1
# print(dict1["name"])  # 获取指定key对应的value
# print(type(dict1))
print(dict1)
dict1["name"] = "op"  # 修改指定key对应的value
print(dict1)
dict1["height"] = 1.75  # 如果key存在就是修改,key不存在就是增加键值对
print(dict1)
