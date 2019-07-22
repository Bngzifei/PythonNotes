print('pickle...')
"""
pickle : 英文腌制的意思,只能做Python的数据交换.<意思就是将各种数据类型转换成bytes类型>

注意:pickle 的问题是它只能用于Python,并且可能不同版本的Python彼此都不兼容,因此,
只能用pickle保存那些不重要的数据,不能成功地反序列化也没有关系.<意思就是只能写入
保存到磁盘,能不能读取不重要了>


pickle支持的数据类型更多,函数,类统统可以,json不可以序列化类

"""
import pickle

# dic = {'name': 'alex', 'age': 23, 'sex': 'male'}

# j = pickle.dumps(dic)  # 也是dumps(),只是换成了pickle.dumps()
# 使用方式和json完全一样,只是json处理后的结果是str类型,pickle处理后是bytes字节类型
# json写入后的str我们可以直接 看到,pickle写入 后的bytes类型我们看不到具体内容,二进制类型的数据,
# 计算机可以解析出来,这也是pickle不好的原因.
# print(type(j))  # <class 'bytes'> 字节类型
#
# f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
# f.write(j)  # 等价于pickle.dump(dic,f) ---> 打开和写入的功能合并了
# f.close()

# -------------------------反序列化--------------------------------------------

f = open('序列化对象_pickle', 'rb')  # 注意是rb 二进制读的模式
data = pickle.load(f)
# data = pickle.loads(f.read())  # 等价于data=pickle.load(f)--->f 就是 打开的文件,把f.read()和loads() 合并了
print(data['sex'])  # male
print(data['age'])  # 23