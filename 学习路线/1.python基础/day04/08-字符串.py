# 展示信息
# str1 = "he'l'lo"  # he'l'lo
# str11 = "hel\"l\"p"  # 转义
# str2 = 'python'
# # 外单里双
# print(str1)
# print(str11)
# str3 = '''
# sfsfsf
# sdfsd
# ffff
# sfsfs
#
# '''  # 换行展示''号
# print(str3)
# for char in str1:
# 	print(char)
"""三双""用来注释,三单''用来展示多行字符串,展示多行文本内容的意思 """
# Python: 所有的索引均支持正负索引 for 循环中可以有  for i in range(1,8,2) 也可以有 for i in range(9,2,-1) 这种表示方法.

# 后期所有的字符串全部使用正则表达式处理,这里的内容简单处理,知道有就行,忘记了去百度搜索

"""判断:"""
# str1 = '012Asd@!#'
# print(str1.isalpha())
# print(str1.isdecimal())
# print(str1.islower())
# print(str1.isupper())
# print(str1.startswith('0'))
# print(str1.endswith('#'))

"""查找和替换"""

# str2 = 'hello world'
# print(str2.find('e'))  # 返回'e'在str2中的索引位置
# print(str2.find('q'))  # 找不到就返回-1
# print(str2.rfind('e'))  # 从右向左查找,返回的是正索引,仍然是1
# print(str2.index('e'))
# # str2.index('2')  # index()找不到就会报错
# str2.rindex('e')  # rindex()找不到就会报错 从右向左查找,返回的是正索引,仍然是1
# print(str2.replace('hello', 'Python'))

"""拆分和连接"""

# str3 = 'hello Python'
# str4 = 'C is everying'
# # 返回元组，把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
# print(str3.partition(' '))
# # 返回列表，以 str 为分隔符拆分 string，如果 num 有指定值，则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
# print(str3.split(' '))
# print(str3 + str4)
# # 返回字符串，以 string 作为分隔符，将 seq 中所有的元素（的字符串表示）合并为一个新的字符串
# print(' '.join(str4))
"""大小写转换"""

# str5 = 'Hello World!'
# print(str5.lower())
# print(str5.upper())
"""文本对齐"""
# print(str5.ljust(15))
# print(str5.rjust(15))
# print(str5.center(18, '*'))

"""去除空白符"""

str7 = '   这世界不太平,  谁能 保证 明天那那那   '
# 返回新字符串，截掉 string 左边（开始）的空白字符
print(str7.lstrip())
# 返回新字符串，截掉 string 右边（末尾）的空白字符
print(str7.rstrip())
# 返回新字符串，截掉 string 左右两边的空白字符
print(str7.strip())











