"""
最为人熟知的是reduce,最有用的是partial及其变体,partialmethod.

functools.partial这个高阶函数用于部分应用一个函数.部分应用是指:
基于一个函数创建一个新的可调用对象,把原函数的某些参数固定.使用这个
函数可以把接受一个或多个参数的函数改编成需要回调的API,这样参数更少.

"""


# 使用partial把一个两参数函数改编成需要单参数的可调用对象
from operator import mul
from functools import partial
triple = partial(mul,3)
print(triple(7))  # 21
print(list(map(triple,range(1,10))))  # [3, 6, 9, 12, 15, 18, 21, 24, 27]

"""


使用unicode.normalize函数再举个例子.
	
	如果处理多国语言编写的文本,在比较或排序之前可能会想使用unicode.normalize("NFC",s)
	处理所有的字符串s.如果经常这么做,可以定义一个nfc函数.
"""


import unicodedata,functools

nfc = functools.partial(unicodedata.normalize,"NFC")
s1 = "café"
s2 = "cafe\u0301"
print(s1,s2)  # café café
print(s1 == s2)  # False
print(nfc(s1)==nfc(s2))  # True

"""
partial的第一个参数是一个可调用的对象,后面跟着任意个要绑定的定位参数和关键字参数.
partial()返回一个functools.partial对象
functools.partial对象提供了访问原函数和固定参数的属性.
functools.partialmethod函数的作用与partial一样,不过是用来处理方法的.


functools模块中的lru_cache函数令人印象深刻,它会做备忘(memoization),这是一种自动优化措施,
它会存储耗时的函数调用结果,避免重新计算.


函数式编程:
	
	除了匿名函数句法上的限制之外,影响函数式编程惯例用发在Python中广泛使用的最大障碍是 缺少 
	尾递归消除(tail-recursion-elimination),这是一项优化措施.在函数的定义体"末尾"递归调用,
	从而提高计算函数的内存使用效率.


匿名函数:
	
	除了Python独有句法上的局限,在任何一门语言中,匿名函数都有一个严重的缺点:没有名称.
	
	因为:函数如果有名称,栈跟踪更易于阅读.匿名函数式一种便利的简洁方式,人们乐于使用它们,但是
	有时会忘乎所以,尤其是在鼓励深层嵌套匿名函数的语言和环境中.如果JavaScript和Node.js
	匿名函数嵌套的层级太深,不利于调试和处理错误.Python中的异步编程结构更好,或许就是因为lambda
	表达式有局限.
	
	promise对象,期物(future)和deferred对象是现代异步API中使用的概念.把它们与协程结合起来,能避免
	掉入"回调地狱".




"""



