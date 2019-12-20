"""
函数,面向过程的叫法(C语言中),方法.面向对象(Python中).属于某个人私有的.函数是公共的.二者本质上一样的实现思想.

增加元素
"""
# list1 = [1, 2, 3]

# """添加元素"""
# list1.append("大爷哟")  # 元素添加到列表尾部
# print(list1)
# # print('----------')
# #
# """插入元素"""
# list1.insert(0, '王五')  # 根据索引插入到指定位置,原来的元素依次向后移一位
# print(list1)
# # print('----------')
# #
# # # iterable 迭代的,就是可以有规律的推导出来的意思,就是知道1就可以推导出2这种.
# """合并列表"""
# list2 = ['水手', '司机']
# list1.extend(list2)  # extend:扩展,将list2列表中的元素放到list1中
# print(list1)
# print('----------')

# """将list2列表作为一个元素添加到list1中"""
# list1.append(list2)
# print(list1)
# print('----------')
# list1 = [1, 2, 3, '水手', '菠菜']
# """删除元素"""
# list1.remove('水手')  # remove()直接删除元素
# print(list1)
# print('----------')
# list1 = [1, 2, 3, '水手', '菠菜']
# del list1[4]  # del()根据索引删除指定元素
# print(list1)
# print('----------')
#
# list1 = ['张珊', '李四', '王五']
# print(list1.pop())  # 默认是弹出最后一个元素
# print(list1.pop(1))  # 删除指定索引元素,并且把删除的元素返回,使用print()函数可以查看删除的元素是啥
# """
# 注意:pop()弹出指定索引的元素之后,原来list的索引发生相应改变
# 形如:这样的 class list def pop(self, index: int = -1) Inferred type: (self: 
# list, index: 
# int) -> TypeVar('_T')
# 出现 -> 后面有东西,说明这个函数是有返回值的.意思就是可以将这个值赋值给一个变量,并显示出来.
# """
# name = list1.pop(0)  # 现在的list1列表已经是['张珊','王五']
# print(name)  # 输出的是现在list1对应的list1[0]位置的元素->张珊
# print(list1)  # 现在的list1只剩下一个元素王五 ['王五']
# print('----------')

# """清空列表"""
# list1 = ['张珊', '李四', '王五']
# list1.clear()  # 清空列表
# print(list1)
# print('----------')
#
# """修改列表"""
# list1 = ['张珊', '李四', '王五']
# list1[0] = 'ml'  # 就是把指定索引位置的元素重新赋值了
# print(list1)
# print('----------')

# """查询list中具体某个元素"""
# list1 = ['张珊', '李四', '王五']
# name = list1[1]  # 查询索引为1的元素
# print(name)
#
# """查找元素对应的索引位置"""
# list1 = ['张珊', '李四', '王五','我','你','他']
# index1 = list1.index('王五',1, 5)  # 控制查找范围(1,5),意思就是从索引1开始查找,一直查到索引为5的位置(不包括5)
# print(index1)
#
# """查找元素出现的次数,计数功能"""
# list1 = ['张珊', '李四', '王五','我','我','我','你','他']
# count1 = list1.count('我')  # 查找元素出现次数
# print(count1)
#
# """获取列表长度,求列表包含的元素的总数"""
#
# list1 = ['张珊', '李四', '王五','我','我','我','你','他']
# print(len(list1))  # 获取list长度,即获取元素总个数

# """某个元素在不在列表中"""
# list1 = ['张珊', '李四', '王五','我','我','我','你','他']
# if '张珊' in list1:
# 	print('在')
# else:
# 	print('不在')


# 有 ->就是有返回值,没有就是无返回值.
# nums=[119,22,11,33,44,55]

# for num in nums:
# 	print(num)
# i = 0
# while i < len(nums):
# 	print(nums[i])
# 	i += 1

# print(sorted(nums))

# 从sort排序开始
# list1 = [[], [], []]
# for i in range(3):  # i是list1索引列表,这个索引指向的元素又是一个列表
# 	print(i)
# 	name = input('输入姓名:')
# 	list1[i].append(name)
# 	print(list1)
# 	print(list1[i])
# print(list1[5-i][1])
# pop():默认删除最后一个元素
# 消耗大的操作放到后台服务器
