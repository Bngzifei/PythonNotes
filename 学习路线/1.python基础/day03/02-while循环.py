print('媳妇,我错了!')  # ctrl + d 复制并粘贴当前光标所在行代码或选中区域的代码,效果就是将复制粘贴快捷键合并在一起了.这里要注意光标的起始位置,否则会混在一起
"""
while循环的作用:让指定的代码重复执行指定的次数
使用while循环四步:
1.定义一个计数的变量 (也就是设置一个能够终止循环的条件变量)
2.while条件:只要条件为True就会执行while内部的代码
3.在while内部写需要重复执行的代码
4.修改计数变量的值


在学了for循环之后,基本不会用到while了.除了在遇到无限循环的情况下需使用while True   break(continue) 进行某种条件下的终止循环进行下一步.最常见的就是   ...错误,请重新输入  这种要求
"""
print('开始...')
i = 0  # 计数变量,一般为0 执行1次 ,编程时计数一般都是从0开始计数.源于索引的概念0->无穷大
while i < 100:  # 0-99 共计100次
	print('媳妇,错了 %d ' % i)  # 重复执行的代码
	i = i + 1  # 计数变量的值修改,终止条件,或者是i += 1,*号在网页中会显示斜体功能 ** 网页中是加粗效果


print('完成了...')