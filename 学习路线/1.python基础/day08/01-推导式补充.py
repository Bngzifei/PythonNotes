print('推导式补充:')

"""推导式补充:

列表推导式,字典推导式,无序集合推导式

格式:列表 [计算公式,for循环], 无序集合 {计算公式,for循环}


字典推导式:{key:value for 循环}


dict1 = {'1':1,'2':4,'3':9....}

"""

# dict1 = {str(i):i**2 for i in range(1,11)}  # i是整数,这里需要把i转换成字符串
# print(dict1)


dict1 = {'name': 'zhangsan', 'age': 18}  # key-value互换位置

# dict2 = {dict1[key] :key for key in dict1}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)
