"""
抓主要,别慌.


扩展:使用哪个资源多一些分类:
CPU密集型程序:主要消耗CPU资源,建议使用进程实现
IO密集型程序:需要消耗网络/文件  I/O资源 建议使用协程
如果任务量比较少,建议使用线程.


from gevent import monkey
monkey.patch_all()

import gevent
在上述代码中,import gevent已经导入了gevent模块了,为什么还要再导入一遍monkey?
monkey已经在gevent里面了吧
gevent是模块,monkey也是一个模块,也是一个包.可以使用:import gevent.monkey
gevent.monkey.patch_all() 来调用

__next__提供下一个元素的值是怎么实现的
	返回值实现计算好后就return返回即可.


生成器函数的应用场景,相比一般的函数有什么优势?
	需要一个代码执行一下,然后回来再执行一次,就可以考虑生成器函数
"""