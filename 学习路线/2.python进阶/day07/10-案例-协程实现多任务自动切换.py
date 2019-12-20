import urllib.request
from gevent import monkey  # 你是猴子搬来的救兵吗?  猴子补丁,专门解决协程gevent 因阻塞等待而无法自动切换的'bug'

monkey.patch_all()  # 自动切换任务,并发执行
import gevent
import time


# 底层调用recv的方法,会卡在recv收数据的地方,只要我在等,就切换到其他地方执行任务,提高资源的利用率
def down_html(url):
	print('正在开始下载%s' % url)
	response = urllib.request.urlopen(url=url)
	data = response.read()
	print('下载完成,收到了来自%s的%d个字节' % (url, len(data)))


def main():
	star_time = time.time()
	# 创建并且启动协程 spawn:就是产生的意思
	g1 = gevent.spawn(down_html, 'http://baidu.com')
	g2 = gevent.spawn(down_html, 'http://qq.com')
	g3 = gevent.spawn(down_html, 'http://itcast.com')
	# 等待协程执行完成
	gevent.joinall([g1, g2, g3])
	end_time = time.time()
	print('花费了%f s' % (end_time - star_time))


if __name__ == '__main__':
	main()

"""
网络型:使用线程和协程

并发超过100,就要使用协程了.


进程/线程是os级别的多任务机制,消耗的资源多,
要求程序的稳定性高<本地程序-->进程>,任务少量-线程

协程 用户级别的多任务机制,


"""
