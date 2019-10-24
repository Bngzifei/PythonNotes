"""
Python 中，有关线程开发的部分被单独封装到了模块中，和线程相关的模块有以下 2 个：
_thread：是 Python 3 以前版本中 thread 模块的重命名，此模块仅提供了低级别的、原始的线程支持，
以及一个简单的锁。功能比较有限。正如它的名字所暗示的（以 _ 开头），一般不建议使用 thread 模块；
threading：Python 3 之后的线程模块，提供了功能丰富的多线程支持，推荐使用。


本节就以 threading 模块为例进行讲解。Python 主要通过两种方式来创建线程：

1.使用 threading 模块中 Thread 类的构造器创建线程。即直接对类 threading.Thread 进行实例化，
并调用实例化对象的 start 方法创建线程。

2.继承 threading 模块中的 Thread 类创建线程类。即用 threading.Thread 派生出一个新的子类，
将新建类实例化，并调用其 start 方法创建线程。

"""

# 调用 Thread 类的构造器创建线程
"""
调用 Thread 类的构造器创建线程很简单，直接调用 threading.Thread 类的如下构造器创建线程：
__init__(self, group=None, target=None, name=None, args=(), kwargs=None, *,daemon=None)

上面的构造器涉及如下几个参数：
group：指定该线程所属的线程组。目前该参数还未实现，因此它只能设为 None。
target：指定该线程要调度的目标方法。
args：指定一个元组，以位置参数的形式为 target 指定的函数传入参数。元组的第一个元素传给 target 函数的第一个参数，
元组的第二个元素传给 target 函数的第二个参数……依此类推。

kwargs：指定一个字典，以关键字参数的形式为 target 指定的函数传入参数。
daemon：指定所构建的线程是否为后代线程。

通过 Thread 类的构造器创建井启动多线程的步骤如下：
调用 Thread 类的构造器创建线程对象。在创建线程对象时，target 参数指定的函数将作为线程执行体。
调用线程对象的 start() 方法启动该线程。

下面程序示范了通过 Thread 类的构造器来创建线程对象：

"""
import threading


def action(max):
    """定义一个普通的action函数,该函数准备作为线程执行体"""
    for i in range(max):
        # 调用threading模块中的current_thread()函数获取当前线程,
        # 调用线程对象的getName()方法获取当前线程的名字
        print(threading.current_thread().getName() + "" + str(i))


for i in range(100):
    """这个循环和下面的print才是主程序"""
    print(threading.current_thread().getName() + "" + str(i))
    if i == 20:
        # 创建并启动第一个线程
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        # 创建并启动第二个线程
        t2 = threading.Thread(target=action, args=(105,))
        t2.start()


print("主线程执行完成!")


"""

默认情况下，主线程的名字为 MainThread，用户启动的多个线程的名字依次为 Thread-1、Thread-2、Thread-3、...、Thread-n 等。

虽然上面程序只显式创建并启动了两个线程，但实际上程序有三个线程，即程序显式创建的两个子线程和主线程。前面己经提到，当 Python 程序开始运行后，程序至少会创建一个主线程，主线程的线程执行体就是程序中的主程序（没有放在任何函数中的代码）。
在进行多线程编程时，不要忘记 Python 程序运行时默认的主线程，主程序部分（没有放在任何函数中的代码）就是主线程的线程执行体。

从图 1 可以看出，此时程序中共包含三个线程，这三个线程的执行没有先后顺序，它们以并发方式执行：Thread-1 执行一段时间，然后可能 Thread-2 或 MainThread 获得 CPU 执行一段时间，接下来又换其他线程执行，这就是典型的线程并发执行，CPU 以快速轮换的方式在多个线程之间切换，从而给用户一种错觉，即多个线程似乎同时在执行。

通过上面介绍不难看出多线程的意义，如果不使用多线程，主程序直接调用两次 action() 函数，那么程序必须等第一次调用的 action() 函数执行完成，才会执行第二次调用的 action() 函数；必须等第二次调用的 action() 函数执行完成，才会继续向下执行主程序。

而使用多线程之后，程序可以让两个 action() 函数、主程序以并发方式执行，给用户一种错觉，两个 action() 函数和主程序似乎同时在执行。
说穿了很简单，多线程就是让多个函数能并发执行，让普通用户感觉到多个函数似乎同时在执行。

除此之外，上面程序还用到了如下函数和方法：
threading.current_thread()：它是 threading 模块的函数，该函数总是返回当前正在执行的线程对象。
getName()：它是 Thread 类的实例方法，该方法返回调用它的线程名字。

在 Threading 模块中，除了 current_thread() 函数外，还经常使用如下 2 个函数：
threading.enumerate()：返回一个正运行线程的 list。“正运行”是指线程处于“启动后，且在结束前”状态，不包括“启动前”和“终止后”状态。
threading.activeCount()：返回正在运行的线程数量。与 len(threading.enumerate()) 有相同的结果。
程序通过 geName() 方法返回指定线程的名字，还可以通过 setName(name) 方法为线程设置名字，这两个方法可通过 name 属性来代替。
"""


"""
二.继承 Thread 类创建线程类


通过继承 Thread 类来创建并启动线程的步骤如下：
1.定义 Thread 类的子类，并重写该类的 run() 方法。run() 方法的方法体就代表了线程需要完成的任务，因此把 run() 方法称为线程执行体。
2.创建 Thread 子类的实例，即创建线程对象。
3.调用线程对象的 start() 方法来启动线程。

下面程序示范了通过继承 Thread 类来创建并启动线程：
"""

from threading import Thread


class FkThread(Thread):
    """通过继承Thread类来创建线程类"""

    def __init__(self):
        super(FkThread, self).__init__()
        # Thread.__init__(self)
        self.i = 0

    def run(self):
        """重写run方法作为线程执行体"""
        while self.i < 100:
            """调用threading模块中的current_thread()函数获取当前线程"""
            print(threading.current_thread().getName() + " " + str(self.i))
            self.i += 1


for i in range(100):
    """主程序"""
    print(threading.current_thread().getName() + "" + str(i))
    if i == 20:
        # 创建并启动第一个线程
        ft1 = FkThread()
        ft1.start()

        # 创建并启动第二个线程
        ft2 = FkThread()
        ft2.start()

print("主线程终于执行结束!")


"""

上面程序中的 FkThread 类继承了 threading.Thread 类，并实现了 run() 方法。
run() 方法中的代码执行流就是该线程所需要完成的任务

从图 2 可以看到，此时程序中同样有主线程、Thread-1 和 Thread-2 三个线程，它们以快速轮换的方式在执行，
这就是三个线程并发执行的效果。

通常来说，推荐使用第一种方式来创建线程，因为这种方式不仅编程简单，而且线程直接包装 target 函数，
具有更清晰的逻辑结构。
"""
