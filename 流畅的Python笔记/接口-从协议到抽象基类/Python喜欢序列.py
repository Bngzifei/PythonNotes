"""
Python数据类型的哲学是尽量支持基本协议.对序列来说,即便是最简单的实现,Python也会力求做到最好.


综上,建议序列协议的重要性,如果没有__iter__和__contains__方法,Python会调用__getitem__方法,设法让迭代和in运算符可用.


使用猴子补丁在运行时实现协议

我发现如果FrenchDeck实例的行为像序列,那么它就不需要shuffle方法,因为已经有random.shuffle函数可用,文档中说它的作用是就地打乱序列.

https://github.com/houshanren/hangzhou_house_knowledge

如果遵守既定协议,很有可能增加利用现有的标准库和第三方代码的可能性,这得益于鸭子类型.


xxx object does not support item assignment:某某对象不支持为元素赋值.
这个问题的原因是,shuffle函数要调换集合中元素的位置,而FrenchDeck只实现了不可变的序列协议.可变的序列还必须提供__setitem__方法.

Python是动态语言,因此我们可以在运行时修正这个问题,甚至还可以在交互式控制台中,修正方法如下:


特殊方法__setitem__的签名在https://docs.python.org/3/reference/datamodel.html#emulating- container-types）中定义.

语言参考中使用的参数是self,key和value,而这里使用的是deckposition和card.这么做事为了告诉你,每个Python方法说到底都是普通函数,把第一个参数命名为self只是一种约定.在控制台会话中使用那几个参数没问题,不过在Python源码文件中最好按照文档那样使用self,key和value.

这里的关键是,set_card函数要知道deck对象有一个名为_cards的属性,而且_cards的值必须似乎可变序列.然后,我们把set_card函数赋值给特殊方法__setitem__,从而把它依附在FrenchDeck类上.这种技术叫猴子补丁:在运行时修改类或模块,而不改动源码.猴子补丁很强大,但是打补丁的代码与要打补丁的程序耦合十分紧密,而且往往要处理隐藏和没有文档的部分.

除了举例说明猴子补丁之外,示例还强调了协议是动态的:random.shuffle函数不关心参数的类型,只要那个对象实现了部分可变序列协议即可.即便对象一开始没有所需的方法也没关系,后来再提供也行.

目前,本章讨论的主题是"鸭子类型":对象的类型无关紧要,只要实现了特定的协议即可.



水禽和抽象基类:

忽略对象的真正类型,转而关注对象有没有实现所需的方法,签名和语义.

对Python来说,这基本上是指避免使用isinstance检查对象的类型,更别提type(foo) is bar这种更糟的检查方式了,这样做没有任何好处,甚至禁止最简单的继承方式.

总的来说,鸭子类型在很多情况下十分有用,但是在其他情况下,随着发展,通常有更好的方式.事情是这样的...

白鹅类型(goose typing)
	
	白鹅类型指,只要cls是抽象基类,即cls的元类是abc.ABCMeta,就可以使用isinstance(obj,cls)

	collections.abc中有很多有用的抽象类(Python标准库的numbers模块中还有一些)

	与具体类相比,抽象基类有很多理论上的优点.Python的抽象基类还有一个重要的实用优势:可以使用register类方法在终端用户的代码中把某个类声明为一个抽象基类的虚拟子类(为此,被注册的类必须满足抽象基类对方法名称和签名的要求,最终要的是满足底层语义契约;但是,开发那个类时不用了解抽象基类,横不用继承抽象基类).这大大地打破了严格的强耦合,与面向对象编程人员掌握的知识有很大出入,因此使用继承时要小心.
	
	有时,为了让抽象基类识别子类,甚至不用注册.

	其实,抽象基类的本质就是几个特殊方法,例如:
	可以看出,无需注册,abc.Sized也能把Struggle识别为自己的子类,只要实现了特殊方法__len__即可(要使用正确的句法和语义实现),前者要求没有参数,后者要求返回一个非负整数.指明对象的长度;如果不使用规定的句法和语义实现特殊方法,如__len__,会导致非常严重的问题.

	最后我想说的是:如果实现的类体现了numbers,collections.abc或其他框架中抽象基类的概念,要么继承相应的抽象基类,要么把类注册到相应的抽象基类中,开始开发程序时,不要使用提供注册功能的库或框架,要自己动手注册;如果必须检查参数的类型,这是最常见的,例如检查是不是序列,那就这样做:
	isinstance(the_arg,collections.abc.Sequence)
	此外,不要在生产代码中定义抽象基类(或元类),如果你很想这样做,我打赌可能是因为你想找茬,刚拿到新工具的人都有大干一场的冲动.如果你能避开这些深奥的概念,你(以及未来的代码维护者)的生活将更愉快,因为代码会变得简洁明了.

	当然,你还可以自己定义抽象基类,但是我不建议高级Python程序员之外的人这么做;同样,我也不建议你自己定义元类...我说的高级Python程序员是指对Python语言的一招一式都了如指掌,即便对这类人来说,抽象基类和元类也不是常用工具.如此"深层次的元编程",如果可以这么讲的话,适合框架的作者使用,这样便于众多不同的开发团队独立扩展框架...真正需要这么做的高级Python程序员不超过1%.

	
	继承抽象基类很简单,只需要实现所需的方法,这样也能明确表明开发者的意图.这一意图还能通过注册虚拟子类来实现.

	此外,使用isinstance和issubclass测试抽象基类更为人接受.过去,这两个函数用来测试鸭子类型,但用于抽象基类会更灵活.毕竟,如果某个组件没有继承抽象子类,事后还可以注册,让显式类型检查通过.

	然而,即便是抽象基类,也不能滥用isinstance检查,用得多了可能导致代码异味,即表明面向对象设计得不好.在一连串if/elif/elif中使用isinstance做检查,然后根据对象的类型执行不同的操作,通常是不好的做法;此时应该使用多态,即采用一定的方式定义类,让解释器把调用分派给正确的方法,而不使用if/elif/elif块硬编码分派逻辑.

	具体使用时,上述建议有一个常见的例外:有些Python API接受一个字符串或字符串序列;如果只有一个字符串,可以把它放到列表中,从而简化处理.因为字符串是序列类型,所以为了把它和其他不可变序列区分开,最简单的方式是用isinstance(x,str)检查.

	另一方面,如果必须强制执行API契约,通常可以使用isinstance检查.老兄,如果你想调用我,必须实现这个,正如本书技术审校所说的.这对采用插入式架构的系统来说特别有用.在框架之外,鸭子类型通常比类型检查更简单,也更灵活.

	本书有几个示例要使用序列,把它当成列表处理.我没有检查参数的类型是不是list,而是直接接受参数,立即使用它构建一个列表.这样,我就可以接受任何可迭代对象;如果参数不是可迭代对象,调用立即失败,并且提供非常清晰的错误消息.
	

	要抑制住创建抽象基类的冲动.滥用抽象基类会造成灾难性后果,表明语言太注重表面形式,这对以实用和务实著称的Python可不是好事.

	抽象基类是用于封装框架引入的一般性概念和抽象的,例如一个序列和一个确切的数.读者基本上不需要自己编写新的抽象基类,只要正确使用现有的抽象基类,就能获得99.9%的好处,而不用冒着设计不当导致的巨大风险.




定义抽象基类的子类:

"""

	
	

import collections

Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck2(collections.MutableSequence):
	ranks = [str(n) for n in range(2,11)] + list("JQKA")
	suits = "spades diamonds clubs hearts".split()

	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits for rangk in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self,position):
		return self._cards[position]

	def __setitem__(self,position,value):
		self._cards[position] = value

	def __delitem__(self,position):
		del self._cards[position]

	def insert(self,position,value):
		self._cards.insert(position,value)

"""
导入时(加载并编译xxx模块时),Python不会检查抽象方法的实现,在运行时实例化FrenchDeck2类时才会真正检查.因此,如果没有正确地实现某个抽象方法,Python会抛出TypeError异常,并把错误消息设为Cannot instantiate abstract class FrenchDeck2 with abstract methods __delitem__,insert.



要想实现子类,我们可以覆盖从抽象基类中继承的方法,以更高效的方式重新实现.例如,__contains__方法会全面扫描序列,可是,如果你定义的序列按顺序保存元素,那就可以重新定义__contains__方法,使用bisect函数做二分查找,从而提升搜索速度.

为了充分使用抽象基类,我们要知道有哪些抽象基类可用.

"""