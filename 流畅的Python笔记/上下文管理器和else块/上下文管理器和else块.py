"""
for/else,while/else和try/else的语义关系紧密,不过与if/else差别很大.起初,else这个单词的意思阻碍了我对这些特性的理解,但是最终我习惯了.


else子句的行为如下:

	for
		仅当for循环运行完毕时(即for循环没有被break语句中止)才运行else块.

	while

		仅当while循环因为条件为假值而退出时(即while循环没有被break语句中止)才运行else块.

	try

		仅当try块中没有异常抛出时才运行else块.官方文档还指出,else子句抛出的异常不会由前面的except子句处理.

	在所有情况下,如果异常或者return,break或continue语句导致控制权跳到了复合语句的主块之外,else子句也会被跳过.


我觉得除了if语句之外,其他语句选择使用else关键字是个错误.else蕴含着"排他性"这层意思,例如"要么运行这个循环,要么做那件事".可是,在循环中,else的语义恰好相反:"运行这个循环,然后做那件事."因此,使用then关键字更好.then在try语句的上下文中也说得通:"尝试运行这个,然后做那件事."可是,添加新关键字属于语言的重大变化,而Guido唯恐避之不及.


在这些语句中使用else子句通常能让代码更易于阅读,而且能省去一些麻烦,不用设置控制标志或者添加额外的if语句.

一开始,你可能觉得没必要在try/except块中使用else子句.比较,在下述代码片段中,只有dangerous_call()不抛出异常,after_call()才会执行,对吧?

try:
	dangerous_call()
	after_call()
except OSError:
	log("OSError...")


然而,after_call()不应该放在try块中.为了清晰和准确,try块中应该只抛出预期异常的语句.因此,像下面这样写更好:

try:
	dangerous_call()
except OSError:
	log("OSError...")
else:
	after_call()

现在很明确,try块防守的是dangerous_call()可能出现的错误,而不是after_call().而且很明显,只有try块不抛出异常,才会执行after_call().

在python中,try/except不仅用于处理错误,还常用于控制流程.为此,Python官方词汇表还定义了一个缩略词.

EAFP
	
	取得原谅比获得许可容易.这是一种常见的Python编程风格.先假定存在有效的键或属性,如果假定不成立,那么捕获异常.这种风格简单明快,特点是代码中有很多try和except语句.与其他很多语言一样(如c语言),这种风格的对立面是LBYL风格.

LBYL
	
	三思而后行.这种编程风格在调用函数或者属性或键之前显式测试前提条件.与EAFP风格相反,这种风格的特点是代码中有很多if语句.在多线程环境中,LBYL风格可能会在检查和行事的空当引入条件竞争.例如,对if key in mapping:return mapping[key]这段代码来说,如果在测试之后,但在查找之前,另一个线程从映射中删除了那个键,那么这段代码就会失败.这个问题可以使用锁或者EAFP风格解决.


如果选择使用EAFP风格,那就要更深入地了解else子句,并在try/except语句中合理使用.










"""