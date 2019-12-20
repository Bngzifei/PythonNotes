"""
下面程序抛出错误:UnboundLocalError: local variable 'b' referenced before assignment

注意:首先输出了3,这表明print(a)语句执行了.但是第二个语句print(b)执行不了.
一开始我很吃惊,因为有个全局变量b,而且是在print(b)后为局部变量b赋值的.

可事实是,Python编译函数的定义体时,它判断b是局部变量,因为在函数中给它赋值了.生成的字节码证实
了这种判断.Python会尝试从本地环境获取b.后面调用f2(3)时,f2的定义体会获取并打印局部变量a的值.
但是尝试获取局部变量b的值时,发现b没有绑定值.

这不是缺陷,而是设计选择:Python不要求声明变量,但是假定在函数定义体中赋值的变量是局部变量.这比
JavaScript的行为好多了,JavaScript也不要求声明变量,但是如果忘记把变量声明为局部变量(使用var)
可能会在不知情的情况下获取全局变量.




"""

b = 6
def f2(a):
	global b  #声明b为全局变量,意思就是b只有一个,开始b是6,进入f2之后b=9,b就是9了
	print(a)
	b = 9
	print(b)

f2(3)



"""
如果在函数中赋值时想让解释器把b当成全局变量,要使用globals声明:

比较字节码:
	
	dis模块为反汇编Python函数字节码提供了简单的方式

	编译器把b视作局部变量,即使在后面才为b赋值,因为变量的种类(是不是局部变量)不能改变函数的定义体.

	dis 模块文档:  http://docs.python.org/3/library/dis.html
	

"""