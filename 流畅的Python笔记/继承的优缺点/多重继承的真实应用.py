"""
多重继承的真实应用
	
	多重继承能发挥积极作用.
	的<<设计模式:可复用面向对象软件的基础>>一书中的适配器模式用的就是多重继承,因此使用多重继承肯定没有错.

	在Python标准库中,最常使用多重继承的是collection.abc包.这没什么问题,毕竟连Java都支持接口的多重继承,而抽象基类就是接口声明,只不过它可以提供具体方法的实现.

处理多重继承

	......我们需要一种更好的,全新的继承理论.例如,继承和实例化混淆了语用和语义.

	继承有很多用途,而多重继承增加了可选方案和复杂度.使用多重继承容易得出令人费解和脆弱的设计.我们还没有完整的理论.下面是避免把类图搅乱的一些建议.

	1.把接口继承和实现继承区分开

		使用多重继承时,一定要明确一开始为什么创建子类.主要原因可能有:

			继承接口,创建子类型,实现  是什么  关系
			继承实现,通常重用避免代码重复

		其实这两条经常同时出现,不过只要可能,一定要明确意图.通过继承重用代码是实现细节,通常可以换用组合和委托模式.而接口继承则是框架的支柱.

	2.使用抽象基类显式表示接口

		现代的Python中,如果类的作用是定义接口,应该明确把它定义为抽象基类.Python3.4及以上的版本中,我们要创建abc.ABC或其他抽象基类的子类.

	3.通过混入重用代码

		如果一个类的作用是为多个不相关的子类提供方法实现,从而实现重用,但不体现"是什么"关系.应该把那个类明确地定义为混入类(mixin class).从概念上来讲,混入不定义新类型,只是打包方法,便于重用.混入类绝对不能实例化,而且具体类不能只继承混入类.混入类应该提供某方面的特定行为,只实现少量关系非常紧密的方法.

	4.在名称中明确指明混入

		因为在Python中没有把类声明为混入的正规方式,所以强烈推荐在名称中加入...Mixin后缀.

	5.抽象基类可以作为混入,反过来则不成立

		抽象基类可以实现具体方法,因此也可以作为混入使用.不过,抽象基类会定义类型,而混入做不到.此外,抽象基类可以作为其他类的唯一基类,而混入决不能作为唯一的超类,除非继承另一个更具体的混入---真实的代码很少这样做.

		抽象基类有个局限是混入没有的:抽象基类中实现的具体方法只能与抽象基类及其超类中的方法协作.这表明,抽象基类中的具体方法只是一种便利措施,因为这些方法所做的一切,用户调用抽象基类中的其他方法也能做到.

	6.不要子类化多个具体类

		具体类可以没有,或最多只有一个具体超类.也就是说,具体类的超类中除了这一个具体超类之外,其余的都是抽象基类或混入.

	7.为用户提供聚合类

		如果抽象基类或混入的组合对客户代码非常有用,那就提供一个类,使用易于理解的方式把它们结合起来.

	8.优先使用对象组合,而不是类继承

		这句话是我能提供的最佳建议.熟悉继承之后,就太容易过度使用它了.出于对秩序的诉求,我们喜欢按整洁的层次结构放置物品,程序员更是乐此不疲.
		然而,优先使用组合能让设计更灵活.

		组合和委托可以代替混入,把行为提供给不同的类,但是不能取代接口继承去定义类型层次结构.


内置类型的原生方法使用C语言实现,不会调用子类中覆盖的方法.

注意:与+相比,+=运算符对第二个操作数更宽容.+运算符的两个操作数必须是相同类型,如若不然,结果的类型可能让人摸不着头脑.而+=的情况更明确,因为就地修改左操作数,所以结果的类型是确定的.


本章小结
	
	本章首先说明了Python对运算符重载施加的一些限制:禁止重载内置类型的运算符,而且限于重载现有的运算符,不过有几个例外:is,and,or,not
	
	随后,本章讲解了如何重载一元运算符,并实现了__neg__和__pos__方法.接着重载中缀运算符,首先是+,它由__add__方法提供支持.我们得知,一元运算符和中缀运算符的结果应该是新对象,并且决不能修改操作数.为了支持其他类型,我们返回特殊的NotImplemented值(不是异常),让解释器尝试对调操作数,然后调用运算符的反向特殊方法(如__radd__).

	如果操作数的类型不同,我们要检测出不能处理的操作数.本章使用两种方式处理这个问题:一种是鸭子类型,直接尝试执行计算,如果有问题,捕获TypeError异常;另一种是显式使用isinstance测试,__mul__方法就是这么做的.这两种方式各有优缺点:鸭子类型更灵活,但是显式检查更能预知结果.如果选择使用isinstance,要小心,不能测试具体类,而要测试numbers.Real抽象基类,例如isinstance(scalar,numbers.Real).这在灵活性和安全性之间做了很好的折中,因为当前或未来由用户定义的类型可以声明为抽象基类的真实子类或虚拟子类.
	
	
	接下来的话题是众多比较运算符.我们通过__eq__方法实现了==,而且发现Python在object基类中通过__ne__方法为!=提供了便利的实现.Python处理这些运算符的方式与>,<>=和<=稍有不同,具体而言是选择反向方法的逻辑不同.此外Python还会特别处理==和!=的后备机制:从不抛出错误,因为Python会比较对象的ID,作最后一搏.


延伸阅读

	在Python编程中,运算符重载经常使用isinstance做测试.一般来说,库应该利用动态类型(提高灵活性),避免显式测试类型,而是直接尝试操作,然后处理异常,这样只要对象支持所需的操作即可,而不必一定是某种类型.但是,Python抽象基类允许一种更为严格的鸭子类型.

泛函数
	
	由Python3的@singledispatch装饰器支持.

functools.total_ordering函数是个类装饰器,它能为只定义了几个比较运算符的类自动生成全部比较运算符.






"""