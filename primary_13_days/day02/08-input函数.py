#coding:utf-8  # Python 2 中需要首先声明编码方式
# name = input('请输入:')  # 阻塞式函数,提示作用
# print(name)  # 接收,只有回车键后才接收.就是enter键按下之后计算机才会接收刚刚输入的数据值,并将它保存到name变量中,使用print()函数进行输出显示.
# # Python3中input函数接收到的数据都是字符串类型
# print(type(name))


# Python2中的input数据接收到数据会进行自动类型推导,如果想让输入字符串正常显示,需要手动添加 ""双引号
# name = input('请输入:')
# print(type(name))
#
# name = raw_input('请输入:')  # 和Python3中的input一样,接收到数据都是字符串类型.不会进行int等类型的推导
# print(type(name))

'''
输出结果:
请输入:123
<type 'int'>
请输入:123
<type 'str'>

'''