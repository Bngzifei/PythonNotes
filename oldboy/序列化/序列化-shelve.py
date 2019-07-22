print('序列化shelve...')

"""
shelve模块:
缺点:支持的数据类型有限
用途:跨语言传输数据
把所有数据内容全部处理成一个字典类型

只有一个open()函数,返回类似字典的对象,key必须为字符串,
value是Python支持的所有数据类型

"""

# 定义一个空字典
# dic = {}
# 给空字典添加元素
# dic['name'] = 'alex'
# dic['info'] = {'name':'alex1'}


import shelve
# txt:就是text的简写格式的文本,window下面就是记事本建立的文本文件

f = shelve.open(r'shelve.txt')  # 目的:将一个字典放入文本

# 先把下列的字典形式的数据写入到文本中,然后注释掉这部分
# f['stu1_info'] = {'name':'alex1','age':18}
# f['stu2_info'] = {'name':'alex2','age':28}
# f['stu3_info'] = {'name':'alex3','age':38}
# f.close()
# 使用get获取指定键key对应的值.
print(f.get('stu1_info')['age'])
print(f.get('stu2_info')['name'])
print(f.get('stu3_info')['age'])

