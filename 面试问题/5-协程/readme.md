## 异步IO

### 异步处理

```
从调度程序的任务队列中挑选任务,该调度任务以交叉的形式执行这些任务,我们并不能保证任务将以某种顺序去执行,因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行的结果。Python3通过asyncio模块和await关键字来支持异步处理。
```

```python
# -*- coding: utf-8 -*-
"""
异步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


if __name__ == '__main__':
    main()

```

```
说明:
    上面的代码使用get_event_loop函数获得系统默认的事件循环,这个三方库可以跟asyncio模块一起工作,并提供了对Future对象的支持。
```

```python
# -*- coding: utf-8 -*-
import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()

```

说明:

```
异步IO与多进程的比较:
    当程序不需要真正的并发性或并行性,而是更多的依赖于异步处理和回调时,asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑asyncio,它很适合编写没有实时数据处理需求的Web应用服务器。
```

```
Python还有很多用于处理并行任务的扩展库,例如:joblib,PyMP等。实际开发中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）和水平扩展（将单个节点变成多个节点）两种做法，可以通过消息队列来实现应用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，不同机器上的应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队列协议），AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，最著名的实现包括：Apache的ActiveMQ,RabbitMQ等。

要实现任务的异步化,可以使用名为Celery的三方库。Celery是Python编写的分布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或者Redis来作为后端的消息代理。
```

