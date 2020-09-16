# -*- coding: utf-8 -*-

# 将 Account 类改为如下形式，它就是线程安全的：
import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        # 账户余额
        self._balance = balance
        # 可重入锁
        self.lock = threading.RLock()

    # 因为账户余额不允许随便修改，所以只为self._balance提供getter方法
    def getBalance(self):
        return self._balance

    # 提供一个线程安全的draw()方法来完成取钱操作
    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            # 账户余额大于取钱数目
            if self._balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name \
                      + "取钱成功！吐出钞票:" + str(draw_amount))
                time.sleep(0.001)
                # 修改余额
                self._balance -= draw_amount
                print("\t余额为: " + str(self._balance))
            else:
                print(threading.current_thread().name \
                      + "取钱失败！余额不足！")
        finally:
            # 修改完成，释放锁
            self.lock.release()


"""
上面程序中的定义了一个 RLock 对象。在程序中实现 draw() 方法时，进入该方法开始执行后立即请求对 RLock 对象加锁，当执行完 draw() 方法的取钱逻辑之后，程序使用 finally 块来确保释放锁。

程序中 RLock 对象作为同步锁，线程每次开始执行 draw() 方法修改 self.balance 时，都必须先对 RLock 对象加锁。当该线程完成对 self._balance 的修改，将要退出 draw() 方法时，则释放对 RLock 对象的锁定。
这样的做法完全符合“加锁→修改→释放锁”的安全访问逻辑。

当一个线程在 draw() 方法中对 RLock 对象加锁之后，其他线程由于无法获取对 RLock 对象的锁定，因此它们同时执行 draw() 方法对 self._balance 进行修改。这意味着，并发线程在任意时刻只有一个线程可以进入修改
共享资源的代码区（也被称为临界区），所以在同一时刻最多只有一个线程处于临界区内，从而保证了线程安全。

为了保证 Lock 对象能真正“锁定”它所管理的 Account 对象，程序会被编写成每个 Account 对象有一个对应的 Lock（就像一个房间有一个锁一样）。

上面的 Account 类增加了一个代表取钱的 draw() 方法，并使用 Lock 对象保证该 draw() 方法的线程安全，而且取消了 setBalance() 方法（避免程序直接修改 self._balance 成员变量），
因此线程执行体只需调用 Account 对象的 draw() 方法即可执行取钱操作。

"""


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 直接调用account对象的draw()方法来执行取钱操作
    account.draw(draw_amount)


# 创建一个账户
acct = Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()

"""
上面程序中代表线程执行体的 draw() 函数无须自己实现取钱操作，而是直接调用 account 的 draw() 方法来执行取钱操作。
由于 draw() 方法己经使用 RLock 对象实现了线程安全，因此上面程序就不会导致线程安全问题。


可变类的线程安全是以降低程序的运行效率作为代价的，为了减少线程安全所带来的负面影响，程序可以采用如下策略：
不要对线程安全类的所有方法都进行同步，只对那些会改变竞争资源（竞争资源也就是共享资源）的方法进行同步。
例如，上面 Account 类中的 account_no 实例变量就无须同步，所以程序只对 draw() 方法进行了同步控制。
如果可变类有两种运行环境，单线程环境和多线程环境，则应该为该可变类提供两种版本，即线程不安全版本和线程安全版本。
在单线程环境中使用钱程不安全版本以保证性能，在多线程环境中使用线程安全版本。


"""
