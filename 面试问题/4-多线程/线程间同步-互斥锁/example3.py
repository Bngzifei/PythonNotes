# -*- coding: utf-8 -*-
import threading
import time

# 可重入锁部分

class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name \
              + "取钱成功！吐出钞票:" + str(draw_amount))
        time.sleep(0.001)
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name \
              + "取钱失败！余额不足！")


# 创建一个账户
acct = Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()

"""
假设系统线程调度器在注释代码处暂停，让另一个线程执行（为了强制暂停，只要取消程序中注释代码前的注释即可）。取消注释后，再次运行程序，
将总可以看到如图 1 所示的错误结果。

问题出现了，账户余额只有 1000 元时取出了 1600 元，而且账户余额出现了负值，远不是银行所期望的结果。
虽然上面程序是人为地使用 time.sleep(0.001) 来强制线程调度切换，但这种切换也是完全可能发生的（100000 次操作只要有 1 次出现了错误，
那就是由编程错误引起的）。

同步锁:
之所以出现如图 1 所示的错误结果，是因为 run() 方法的方法体不具有线程安全性，程序中有两个并发线程在修改 Account 对象，
而且系统恰好在注释代码处执行线程切换，切换到另一个修改 Account 对象的线程，所以就出现了问题。

为了解决这个问题，Python 的 threading 模块引入了锁（Lock）。threading 模块提供了 Lock 和 RLock 两个类，
它们都提供了如下两个方法来加锁和释放锁：
1.acquire(blocking=True, timeout=-1)：请求对 Lock 或 RLock 加锁，其中 timeout 参数指定加锁多少秒。
2.release()：释放锁。

Lock 和 RLock 的区别如下：
threading.Lock：它是一个基本的锁对象，每次只能锁定一次，其余的锁请求，需等待锁释放后才能获取。
threading.RLock：它代表可重入锁（Reentrant Lock）。对于可重入锁，在同一个线程中可以对它进行多次锁定，也可以多次释放。如果使用 RLock，
那么 acquire() 和 release() 方法必须成对出现。如果调用了 n 次 acquire() 加锁，则必须调用 n 次 release() 才能释放锁。

Lock 是控制多个线程对共享资源进行访问的工具。通常，锁提供了对共享资源的独占访问，每次只能有一个线程对 Lock 对象加锁，
线程在开始访问共享资源之前应先请求获得 Lock 对象。当对共享资源访问完成后，程序释放对 Lock 对象的锁定。

在实现线程安全的控制中，比较常用的是 RLock。通常使用 RLock 的代码格式如下：
class X:
    #定义需要保证线程安全的方法
    def m () :
        #加锁
        self.lock.acquire()
        try :
            #需要保证线程安全的代码
            ＃...方法体
        #使用finally 块来保证释放锁
        finally :
            #修改完成，释放锁
            self.lock.release()

使用 RLock 对象来控制线程安全，当加锁和释放锁出现在不同的作用范围内时，通常建议使用 finally 块来确保在必要时释放锁。

通过使用 Lock 对象可以非常方便地实现线程安全的类，线程安全的类具有如下特征：
该类的对象可以被多个线程安全地访问。
每个线程在调用该对象的任意方法之后，都将得到正确的结果。
每个线程在调用该对象的任意方法之后，该对象都依然保持合理的状态。


总的来说，不可变类总是线程安全的，因为它的对象状态不可改变；但可变对象需要额外的方法来保证其线程安全。例如，
上面的 Account 就是一个可变类，它的 self.account_no和self._balance（为了更好地封装，将 balance 改名为 _balance）
两个成员变量都可以被改变，当两个钱程同时修改 Account 对象的 self._balance 成员变量的值时，程序就出现了异常。
下面将 Account 类对 self.balance 的访问设置成线程安全的，那么只需对修改 self.balance 的方法增加线程安全的控制即可。


"""
