https://blog.csdn.net/guoxiang3538/article/details/79376191
http://www.coolpython.net/python_senior/concurrent/multithreading_event.html

1. Event
借助Event，可以灵活的协调线程间的操作，它提供了下面几个方法

1.1 set()
将事件内部标识设置为True，Event对象最初创建时，内部标识默认是False

1.2 wait()
当在线程中调用wait时，如果事件内部标识为False，则会阻塞，直到set方法被调用，将内部标识设置为True

1.3 clear()
将内部标识重新设置为False

1.4 is_set()
如果内部标识是True，则返回True，反之，返回False