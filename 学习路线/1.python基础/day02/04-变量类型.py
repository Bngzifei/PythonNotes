print('xxxxxx')
name = '小米'  # str string字符串
age = 18  # int integer 整数类型 整型
boy = True  # bool 布尔类型 True False
height = 1.75  # float 小数类型 浮点类型
weight = 75.0
print('aaaaa')
age1 = '123'  # 动态类型语言 Python是动态语言类型,C是静态语言类型 (意思指在创建变量时需要指定变量类型)
age_str = type(age)  # 查看变量的类型
print(age_str)
print(type(age))
# 断点调试:让代码通过手动控制一行一行的执行
# step over 步过  下一步  快捷键:F8
# Python 中的变量在定义时不需要指定类型,他会根据赋值的类型自动进行类型推导
'''
断点调试:先设置断点行,选择Debug按钮 再选择 Step Over(F8)
快捷键:关闭控制台Shift+esc
alt + 1: 打开或关闭文件导航区域
查看变量类型两种方式:1.断点调试2.type()函数
'''