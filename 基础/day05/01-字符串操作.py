str1 = "hello"
"""查找方法"""

# char = str1[0]  #获取指定索引的字符

index = str1.index("l", 3, 9)  # 从索引为3的位置开始直到索引位置为9的地方,获取字符在字符串中第一次出现的索引,如果查找的字符不存在,报错

# index = str1.rindex("l")  # 获取字符在字符串中第一次出现的索引(从右向左的顺序 right:右边)
# index = str1.find("l") # 2 从左往右 获取字符在字符串中第一次出现的索引,找不到不会报错,返回-1,表示没有找到(python的方法只用正数索引)
# index = str1.rfind("l")  # 3  从右往左 获取字符在字符串中第一次出现的索引,找不到不会报错,返回-1
print(index)
print(str1)

"""
列表.字典是可变类型, 列表.append()
元组和字符串是不可变类型

在代码中的区别是:可变的在修改时,一般不用接收新值(就是需要一个变量来接收新值的意思),但是元组.字符串如果对它进行操作,一般都要接收新值 即  变量 = xx

"""

"""替换"""

# str2 = str1.replace("l","a",1)  # 字符.replace(被替换的字符,新字符,替换次数)
# print(str1) str1不会变
# print(str2)


# str1[0] = "G"  #报错,不可以被修改,字符串定义之后不能修改


"""连接/拼接"""

# str2 = "python"
# str3 = str1 + " " + str2
# print(str3)

# list1 = ["2018",'8',"12"]  # 有数字就报 TypeError: sequence item 2: expected str instance, int found
# sep = "-"
# list2 = sep.join(list1)  # sep是separate:英文分隔的意思
# print(list2)  # 2018-8-12

"""拆分"""

# str2 = "2018-8-12"
# list1 = str2.split("-")  # 以指定字符来拆分字符串,返回一个字符串列表 特殊数据处理,比如爬虫下来的日期进行切割等等
# print(list1)

# Py2中数字可以和字母比较大小,原则是:"0"<"A"<"a"
# Py3中不能比较
