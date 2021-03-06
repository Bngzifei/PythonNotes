print('-----------------面试准备------------')
'''
1.>算法的特征:
	1.有穷性:一个算法必须保证执行有限步骤之后能给出最终结果
	2.确切性:算法的每一步必须有确切的定义
	3.输入:一个算法有0个或多个输入.来描述运算对象的初始情况.
	所谓0个输入是指算法本身自带了初始条件
	4.输出:一个算法有一个或多个输出,来反映对输入数据加工后的结果.
	没有输出的算法是无意义的.
	5.可行性:算法原则上能够精确地运行.而且人们用笔做有限次运算后即可完成

2.>冒泡排序的思想:
	通过无序区域中相邻记录的关键字进行比较和位置交换.使关键字最小的记录像气泡一样逐渐向上漂至水面.
	整个算法是从最下面的记录开始,对每两个相邻的关机字进行比较,把关键字较小的记录放到关键字较大的记录上面,
	经过一趟排序后,关键字最小的记录到达最上面.接着再在剩下的记录中找关键字次小的(就是倒数第二个小的)记录.
	把它放在第二个位置上.以此类型.一直到所有记录最终有序为止.
	
	复杂度:时间复杂度为O(n*n),空间复杂度为O(1)

3.>快速排序的思想:
	通过一趟排序将需要排序的数据分割成独立的两部分,其中一部分的所有数据都比另外一部分的所有数据都要小.然后再按此方法对这两部分分别进行快速排序.整个排序过程以递归方式进行.以此达到整个数据变成有序数据的目的.
	
	复杂度:快速排序是不稳定的排序算法.最坏的时间复杂度是O(n*n).最好的时间复杂度是(n*logn).空间复杂度是O(logn)

3.>桶排序:
	桶排序的基本思想:将一个数据表分割成许多buckets(n. 桶，水桶；铲斗；一桶的量).然后每个bucket各自排序.或者用不同的排序算法,或者是递归的使用桶排序.其思想是典型的分而治之的策略.它是一个分布式的排序.介于MSD基数排序和LSD基数排序之间.
	
	桶排序是稳定的
	桶排序是常见排序里最快的一种,大多数情况下比快排还要快
	桶排序非常快,但是同时也非常耗费空间,基本上是最耗费空间的一种排序算法.
	
4.>如何判断单向链表中是否有环?
	首先遍历链表,寻找是否有相同地址.借此判断链表中是否有环.如果程序进入死循环,则需要一块空间来存储指针,遍历新指针时将其和存储的旧指针比对,若有相同指针,则该链表有环,否则将这个新指针存下来后继续往下读取,直到遇见null,这说明这个链表无环.

5.>基础的算法有哪些?如何评价一个算法的好坏?
	基本的算法有:排序算法(冒泡排序,插入排序,快速排序,归并排序),查找(二分查找),
	搜索((DFS)深度优先搜索,(BFS)广度优先搜索,(Dijkstra算法),动态规则算法,
	分类(朴素贝叶斯分类算法等)
	
	评价算法的好坏一般有两种:
		时间复杂度和空间复杂度
	时间复杂度:同样的输入规模(问题规模)花费多少时间
	空间复杂度:同样的输入规模花费多少空间(主要是内存)
	以上两点都是越小越好
	
	稳定性:不会因为输入的不同而导致不稳定的情况发生.
	算法思路是否简单:越简单越容易实现的越好.

6.>哪种数据结构可以实现递归?
	栈可以实现.递归需要保存正在计算的上下文,等待当前计算完成后弹出,再继续计算.只有栈先进后出的特性才能实现.

7.>二叉树如何求两个叶节点的最近公共祖先?
	原理:二叉搜索树是排序过的,位于左子树的节点都比父节点小.位于右子树的节点都比父节点大.我们只需要从根节点开始和两个输入的节点进行比较,...
	
8.>python内置类型性能分析:
	Timer是测量小段代码执行速度的类
	stmt参数是要测试的代码语句(statment)
	setup参数是运行代码时需要的设置
	timer参数是一个定时器函数,与平台有关
	
9.>算法与数据结构的区别:
	数据结构只是静态的描述了数据元素之间的关系
	高效的程序需要在数据结构的基础上设计和选择算法
	
	即:程序=数据结构 + 算法
	
	总结:算法是为了解决实际问题而设计的.数据结构是算法需要处理的问题载体

10.>抽象数据类型(Abstract Data Type)
	抽象数据类型(ADT)的含义是指一个数学模型以及定义在此数学模型上的一组操作.
	即把数据类型和数据类型上的运算捆在一起,进行封装.
	引入抽象数据类型的目的是把数据类型的表示和数据类型上运算的实现
	与这些数据类型和运算在程序中的引用隔开,使它们相互独立.
	
	最常用的数据运算有5种:
	插入
	删除
	修改
	查找
	排序

11.>顺序表的基本形式:
	数据元素本身连续存储,每个元素所占的存储单元大小固定相同.元素的下标是其逻辑地址.而元素的物理地址(实际内存地址)可以通过存储区的起始地址加上逻辑地址与存储单元大小的乘积计算得到.
	所以,访问元素时无需从头遍历,通过计算便可获得对应地址,其时间复杂度为O(1)

12.>顺序表的结构与实现:
	包含两部分:1.表中的元素集合 2. 有关表的整体情况的信息.这个信息主要包括元素存储区的容量和当前表中已有的元素个数.
	
	两种存储方式:1.一体式结构,即表信息和元素连续的存在一起
				2.分离式结构:表对象只保存与整个表有关的信息(即容量和元素个数),实际数据元素存放在另一个独立的元素存储区里.通过链接与基本表对象关联.

13.>元素存储区替换:
	一体式:整体搬迁
	分离式:只更换表信息中的数据链接

14.>元素存储区扩充:
	分离式:更换数据区为存储空间更大的区域
	简称动态顺序表.
	扩充的两种策略:
	1.每次扩充增加固定数目的存储位置.特点:节省空间,但是扩充操作频繁.
	2.每次扩充容量加倍.如每次扩充增加一倍存储空间.特点:减少扩充次数,但可能会浪费空间资源.以空间换时间

15.>顺序表的操作:
	增加元素:末端加:O(1) 无序加:O(1) 有序加:O(n)
	删除元素:末端删:O(1) 无序删:O(1) 有序删:O(n)
	注:有序无序是指加/删元素之后原来的元素的索引位置,即顺序是否变化
	
16.>Python中的顺序表:
	Python中的list和tuple两种类型采用了顺序表的实现技术.
	tuple是不可变类型.即不可变的顺序表.因此不支持改变其内部状态的任何操作.
	Python标准类型list就是一种元素个数可变的线性表,可以加入和删除元素.并在各种操作中维持已有元素的顺序(即保序),而且还具有以下特征:
	基于下标(索引位置)的高效元素访问和更新,时间复杂度应该是O(1)
	为满足该特征,应该采用顺序表技术,表中元素保存在一块连续的存储区中.
	允许任意加入元素,而且在不断加入元素的过程中,表对象的标识(函数id()得到的值)不变.
	为满足该特征,就必须能更换元素存储区,并且为保证存储区list对象的标识id不变,只能采用分离式实现技术.
	在Python的官方实现中,list就是一种采用分离技术实现的动态顺序表.这就是为什么使用append比在指定位置插入元素效率高的原因.
	在Python的官方实现中,list实现采用了如下的策略:在建立空表(或者很小的表)时,系统分配一块能够容纳8个元素的存储区,在执行插入操作时,如果元素存储区满就换一块4倍大的存储区.但如果此时的表已经很大,则改变策略,采用加一倍的方法.引入这种改变策略的方式,是为了避免出现过多空闲的存储位置.
	
17.>链表:
	顺序表的构建需要预先知道数据大小来申请连续的存储空间,而在进行扩充时候又需要进行数据的搬迁,所以使用起来并不是很灵活.
	链表结构可以充分利用计算机内存空间,实现灵活的内存动态管理.
	链表的定义:
		链表是一种常见的基础数据结构,是一种线性表,但是不像顺序表一样连续存储数据,而是在每一个节点(数据存储单元)里存放下一个节点的位置信息(即地址)

18.>单向链表:
	单向链表也叫单链表,是链表中最简单的一种形式,它的每个节点包含两个域,一个信息域(元素域)和一个链接域.这个链接指向链表中的下一个节点,而最后一个节点的链接则指向一个空值.
	表元素域elem用来存放具体的数据.
	链接域next用来存放下一个节点的位置(Python中的标识)
	变量p指向链表的头节点(首节点)的位置,从p出发能找到表中的任意节点.
	4
约束:就是条件的意思.加了某种限制而已

19.>单向循环链表:
	单链表的一个变形是单向循环链表,链表中最后一个节点的next域不再是None,而是指	向链表的头节点
	理解:意思就是最后的next指向的是一个新的链表

20.>双向链表:
	一种更复杂的链表是"双向链表"或"双面链表".每个节点有两个链接:一个指向前一个节点,当此节点为第一个节点时,指向空值,而另一个指向下一个节点,当此节点为最后一个节点时,指向空值.

21.>栈结构的实现: 先进后出,就是后来者居上的类型.底部封口了
	栈可以用顺序表实现,也可以用链表实现
	
22.>队列:串先进先出,和排队买票一个结果,两头都是开着的,没封口,但是只能从一端出,另外一端进入.
	和栈一样,队列也可以用顺序表或者链表实现

23.>双端队列:(deque 全名double-ended queue)
	
	是一种具有队列和栈的性质的数据结构
	
	双端队列中的元素可以从两端弹出,其限定插入和删除操作在表的两端进行.双端队列可以在队列任意一端入队和出队.

24.>选择排序:
	原理:首先在未排序序列中找最小(最大)元素,存放到排序序列的起始位置,然后再从剩余未排序元素中继续寻找最小(最大)元素,然后放到已排序序列的末尾,以此类推,直到所有元素均排序完毕.
	
	优点:主要与数据移动有关.如果某个元素位于正确的最终位置上,则它不会被移动.选择排序每次交换一对元素.它们当中至少有一个将被移到其最终位置上,因此,对n个元素的表进行排序总共进行至少n-1次交换.在所有的完全依靠交换去移动元素的排序方法中,选择排序属于非常好的一种.
	
25.>插入排序:
	原理:通过构建有序序列,对于未排序数据,在已排序序列中从后向前扫描,找到相应位置并插入.插入排序在实现上,在从后向前扫描过程中,需要反复把已排序元素逐步向后挪位,为最新元素提供插入空间.
	

26.>快速排序:
	又称划分交换排序,通过一趟排序将要排序的数据分割成独立的两部分,其中一部分的所有数据都比另外一部分的所有数据都要小.然后再按照此方法对这两部分数据分别进行快速排序,整个排序过程可以递归进行.以此达到整个数据变成有序序列.
	步骤:
	1.从数列中挑出一个元素,称为基准pivot
	2.重新排序数列,所有元素比基准值小的摆放在基准前面,所有元素比基准值大的摆在基准的后面.(相同的可以放在任一边).在这个分区结束之后,该基准就处于数列的中间位置,这个称为分区操作.
	3.递归的把小于基准值元素的子序列和大于基准值元素的子序列排序
	理解:就是排序过程写一次,基准元素两边的序列直接调用之前的排序过程

27.>希尔排序:
	是插入排序的一种,又称缩小增量排序,是直接插入排序算法的一种更高效的改进版本.
	是非稳定排序
	创始人是 DL.shell  (谐音,所有叫希尔)
	原理:把记录按索引的一定增量分组,对每组使用直接插入排序算法排序,随着增量逐渐减少,每组包含的关键词越来越多,当增量减至1时,整个文件恰被分成一组,算法便终止.

28.>归并排序:
	采用分治法的一个非常典型的应用.归并排序的思想就是先递归分解数组,再合并数组.
	
	将数组分解最小之后,然后合并两个有序数组.
	基本思路是比较两个数组的最前面的数,谁小就先取谁.取了后相应的指针就往后移动一位.然后再比较.直至一个数组为空,最后把另一个数组的剩余部分复制过来即可.
	
29.>二分查找:
	又称折半查找
	优点:比较次数少,查找速度快,平均性能好
	缺点:要求待查表为有序表,且插入删除困难.
	因此,折半查找方法适用于不经常变动而查找频繁的有序列表.
	首先,假设表中元素是按升序排列,将表中间位置记录的关键字与查找关键字比较,如果两者相等,则查找成功.否则利用中间位置记录将表分成前,后两个子表,如果中间位置记录的关键字大于查找关键字,则进一步查找前一子表,否则进一步查找后一子表.重复以上过程,直到找到满足条件的记录,使查找成功.或者直到子表不存在为止.此时查找不成功.
	
	
	
	
'''

# -----------------冒泡排序----------------
# def bubble_sort(alist):
# 	for i in range(len(alist) - 1, 0, -1):
# 		# i 表示每次遍历需要比较的次数,是逐渐减小的
# 		for j in range(len(alist) - 1):
# 			if alist[j] > alist[j + 1]:
# 				alist[j], alist[j + 1] = alist[j + 1], alist[j]
# 	return alist
#
#
# li = [56, 68, 12, 3, 0, 7, 89, 7, 2, 0, 1]
# print(bubble_sort(li))

# ----------------快速排序------------------
# def quick_sort(alist, start, end):
# 	"""快速排序"""
# 	# 递归退出的条件
# 	if start >= end:
# 		return
# 	# 设定起始元素为要寻找位置的基准元素
# 	mid = alist[start]
# 	# low 为list左边的 从左向右移动的索引值
# 	low = start
# 	# high是list右边从右向左移动的索引
# 	high = end
# 	# 记住:循环中的判断也是实现过滤的功能.即满足了才执行循环体,
# 	# 不满足直接跳过循环体.往下执行即可
# 	while low < high:
# 		# 如果low与high未重合,high指向的元素不比基准元素小,则high向左移动
# 		while low < high and alist[high] >= mid:
# 			high -= 1
# 		# 如果...
# 		# 将high指向的元素放到low的位置
# 		alist[low] = alist[high]
# 		# 如果low和high未重合,low指向的元素比基准元素小.则low向右移动
# 		while low < high and alist[low] < mid:
# 			low += 1
# 		# 将low指向的元素放到high的位置上
# 		alist[high] = alist[low]
# 	# 退出循环后,low与high重合,此时所指位置为基准元素的正确位置
# 	# 将基准元素放到该位置
# 	alist[low] = mid
# 	print(alist)
#
#
# # 对基准元素左边的子序列进行快速排序,low的位置就是基准元素的位置
# # quick_sort(alist, start, low - 1)
# # 对基准元素右边的子序列进行快速排序,low的位置就是基准元素的位置
# # quick_sort(alist, low + 1, end)
#
#
# alist = [54, 2, 6, 93, 17, 31, 44, 55, 20]  # 初始值 ,54是基准值
# alist = [20, 2, 6, 93, 17, 31, 44, 55, 20]  # 第一次循环开始...
# alist = [20, 2, 6, 93, 17, 31, 44, 55, 93]
# alist = [20, 2, 6, 44, 17, 31, 54, 55, 93]  # 外部循环结束后.第一次快排的结果
# quick_sort(alist, 0, len(alist) - 1)
# print(alist)
# ------------------------------桶排序------------------------------
# def bucket_sort(nums):
# 	# 选择一个最大的数
# 	max_num = max(nums)
# 	# 创建一个元素全部是0的列表,当做桶,存放
# 	bucket = [0] * (max_num + 1)
# 	print(bucket)  # 66个0的list
# 	# 把所有元素放入桶中.即把对应的元素个数加1
# 	for i in nums:
# 		print('这是要排序的元素:', i)
# 		bucket[i] += 1  # 实现了对需要排序的列表中的元素出现次数的计数
# 		print('这是以要排序元素%d作为索引对应的list元素%d' % (i, bucket[i]))
# 		# 每次循环都创建一个空列表,一共创建了nums个列表<即有多少个元素排序就创建多少个空列表>
# 		sort_nums = []
# 		print('创建的空列表:', sort_nums)
# 	print('总列表中的元素是:', bucket)
# 	# 取出桶中元素
# 	for j in range(len(bucket)):  # j是从0取到9.如果len(bucket) - 1,那么就会少了最大的那个,所以这路不能-1
# 		print('总列表长度是:', len(bucket))
# 		print('这是总列表中现在的元素:', bucket[j])
# 		if bucket[j] != 0:
# 			# j索引在总列表中对应的元素不为0的情况下,j就是之前需要排序的那个元素.j本来就是总列表的索引.就是表示位置信息的
# 			for y in range(bucket[j]):  # 表示对应元素出现的次数,如果是1,就添加一次,如果是2,就循环添加2次,以此类推...
# 				print('y是', y)
# 				print('总列表中不为0的元素是%d,表示需要排序的元素是%d' % (bucket[j], j))
# 				sort_nums.append(j)
# 			# print(sort_nums)
# 	return sort_nums
#
#
# num = [5, 6, 3, 6, 9, 7]
# print('最终排序结果是:', bucket_sort(num))



# print([0] * (9 + 1))
# # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# a = [0]  # <class 'list'>
# print(type(a))
# ------------------------------单链表--------------------------------
# 节点实现
# class SingleNode:
# 	"""单链表的节点"""
#
# 	def __init__(self, item):
# 		# _item存放数据元素
# 		self.item = item
# 		# _next是一个节点的标识,就是下一个节点的链接
# 		self.next = None


# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item)链表尾部添加元素
# insert(pos,item)指定位置添加元素
# remove(item)删除节点
# search(item)查找节点是否存在

# 单链表的实现
# class SingleLinkList:
# 	"""单链表"""
#
# 	def __init__(self):
# 		self._head = None
#
# 	def is_empty(self):
# 		"""判断链表是否为空"""
# 		return self._head == None
#
# 	def length(self):
# 		"""链表长度"""
# 		# cur初始时指向头节点
# 		cur = self._head
# 		count = 0
# 		# 尾节点指向None,当未到达尾部时
# 		while cur != None:
# 			count += 1
# 			# 将cur后移一个节点
# 			cur = cur.next
# 		return count
#
# 	def travel(self):
# 		"""遍历链表"""
# 		cur = self._head
#
# 		while cur != None:
# 			print(cur.item)
# 			cur = cur.next
# 		print('....')
#
# 	def add(self, item):
# 		"""头部添加元素"""
# 		# 先创建一个保存item值的节点
# 		node = SingleNode(item)
# 		# 将新节点的链接域next指向头节点,即_head指向的位置
# 		node.next = self._head
# 		# 将链表的头_head指向新节点
# 		self._head = node
#
# 	def append(self, item):
# 		"""尾部添加元素"""
# 		node = SingleNode(item)
# 		# 先判断链表是否为空,若是空链表,则将_head指向新节点
# 		if self.is_empty():
# 			self._head = node
# 		# 若不为空,则找到尾部,将尾节点的next指向新节点
# 		else:
# 			cur = self._head
# 			while cur.next != None:
# 				cur = cur.next
# 			cur.next = node
#
# 	def insert(self, pos, item):
# 		"""指定位置添加元素"""
# 		# 若指定位置pos为第一个元素之前,则执行头部插入
# 		if pos <= 0:
# 			self.add(item)
# 		# 若指定位置超过链表尾部,则执行尾部插入
# 		elif pos > self.length() - 1:
# 			self.append(item)
# 		# 找到指定位置
# 		else:
# 			node = SingleNode(item)
# 			count = 0
# 			# pre用来指向指定位置pos的前一个位置pos-1,初始从头节点开始移动到指定位置
# 			pre = self._head
# 			while count < (pos - 1):
# 				count += 1
# 				pre = pre.next
# 			# 先将新节点node的next指向插入位置的节点
# 			node.next = pre.next
# 			# 将插入位置的前一个节点的next指向新节点
# 			pre.next = node
#
# 	def remove(self, item):
# 		"""删除节点"""
# 		cur = self._head
# 		pre = None
# 		while cur != None:
# 			# 找到了指定元素
# 			if cur.item == item:
# 				# 如果第一个就是删除的节点
# 				if not pre:
# 					# 将头指针指向头节点的后一个节点
# 					self._head = cur.next
# 				else:
# 					# 将删除位置前一个节点的next指向删除位置的后一个节点
# 					pre.next = cur.next
# 				break
# 		else:
# 			# 继续按链表后移节点
# 			pre = cur
# 			cur = cur.next
#
# 	def search(self, item):
# 		"""链表查找节点是否存在,并返回True或者False"""
# 		cur = self._head
# 		while cur != None:
# 			if cur.item == item:
# 				return True
# 			cur = cur.next
# 		return False
#
#
# if __name__ == '__main__':
# 	l1 = SingleLinkList()
# 	l1.add(1)
# 	l1.add(2)
# 	l1.append(3)
# 	l1.insert(2, 4)
# 	print('length:', l1.length())
# 	l1.travel()
# 	print(l1.search(3))
# 	print(l1.search(5))
# 	l1.remove(1)
# 	print('length:', l1.length())
# 	l1.travel()

"""
链表失去了顺序表随机读取的优点,同时链表由于增加了节点的指针域,空间开销比较大,但对存储空间的使用要相对灵活.

链表的主要耗时操作是遍历查找,删除和插入操作本身的复杂度O(1).顺序表查找很快,主要耗时的操作是拷贝覆盖.因为除了目标元素在尾部的特殊情况,顺序表进行插入和删除时需要对操作点之后的所有元素进行前后移位操作,只能通过拷贝和覆盖的方法进行.
"""
# ------------------------------单向循环链表---------------------------------
"""
单链表的一个变形是单向循环链表,链表中最后一个节点的next域不再是None,而是指向链表的头节点
理解:意思就是next指向的是一个新的链表

"""


# -------------------二分查找:非递归实现---------------------------
def binary_search(alist, item):
	first = 0  # 开始位置
	last = len(alist) - 1  # 末尾位置
	while first <= last:
		# midpoint = first + (last-first)
		midpoint = (first + last) // 2  # 中间位置
		print('中间位置是:', midpoint)
		if alist[midpoint] == item:
			print('找到了,要找元素的位置是:', midpoint)
			return True
		elif item < alist[midpoint]:
			last = midpoint - 1
		else:
			first = midpoint + 1

# 不清楚就打断点调试.逐步理解,记住就行.
testlist = [0, 1, 2, 6, 79, 18, 90]
print(binary_search(testlist, 90))

# ----------------------------递归实现---------------------
# def binary_search(alist, item):
# 	if len(alist) == 0:
# 		return False
# 	else:
# 		midpoint = len(alist) // 2
# 		if alist[midpoint] == item:
# 			return True
# 		else:
# 			if item < alist[midpoint]:
# 				return binary_search(alist[:midpoint], item)
# 			else:
# 				return binary_search(alist[midpoint + 1:], item)
