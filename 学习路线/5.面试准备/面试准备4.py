nums = [2, 7, 11, 15, 86, 23]

target = 30

"""
理解题意:
就是在nums列表中找两个元素,这两个元素的和等于target.函数的返回值是
这两个元素的索引

最简单的思路:
遍历这个nums列表,对其里面的每两个元素都进行求和运算,看是否和target相等.


"""

# def two_Sum(nums, target):
# 	"""target = nums[0] + nums[1]"""
# 	"""
# 	这才是完美的版本:直接倒序取,一个从头取,一个从末尾取,肯定不会重复.
# 	嵌套循环的本质理解:就是在外层一次操作时候,内层需要把每一个自己范围内
# 	的元素都遍历一次,每次都和外部循环的i进行相关操作.直到外层循环结束
# 	"""
# 	for i in range(len(nums) - 1, 0, -1):
# 		print(i)
# 		for j in range(i):
# 			print(j)
# 			if nums[i] + nums[j] == target:
# 				return j, i
#
#
# print(two_Sum(nums, target))

# def twoSum(nums, target):
# 	"""target = nums[0] + nums[1]"""
# 	i = 0
# 	while i < len(nums):  # 控制循环次数 一共是 len(nums)次
# 		j = i + 1
# 		while j < len(nums):  # j是下一个元素
# 			sum1 = nums[i] + nums[j]  # 相邻两个元素求和
# 			if sum1 == target:
# 				res = [i, j]
# 				return res
# 			j += 1
# 		i += 1


# print(twoSum(nums, target))


"""
数据库mysql,redis的版本

框架django flask的版本
Flask            0.10.1
django           1.11.11

mysql版本:

mysql> select @@version;
+------------+
| @@version  |
+------------+
| 5.7.21-log |
+------------+
1 row in set (0.00 sec)


redis数据库的版本:

redis-server --version
Redis server v=3.0.501 sha=00000000:0 malloc=jemalloc-3.6.0 bits=64 build=ba05b51e58eb9205


>redis-cli --version
redis-cli 3.0.501
"""

"""
合并两个有序列表,并返回一个新的有序链表

记住:写这种题目一定是先按照自己的套路来,至于更高级的实现方法,等实现了
需求再去优化改进.
"""

list1 = [1, 2, 4]
list2 = [1, 3, 4]


def sortlist(list1, list2):
	"""先把这两个列表中的元素添加到list3中,然后再排序输出"""
	list3 = []
	for l1 in list1:
		list3.append(l1)
	
	for l2 in list2:
		list3.append(l2)
	
	# 注意: sorted() 是一个内置函数.sort()是一个列表的方法.所以下面的写法都可以
	
	# 法一:使用sorted()内置函数实现
	# list3 = sorted(list3)
	
	# 法二:使用.sort()方法实现
	list3.sort()
	
	return print(list3)


sortlist(list1, list2)
