import time
import pywifi
from pywifi import const


def test_wifi_connect():
	wifi = pywifi.PyWiFi()  # 开启一个无线对象
	interface = wifi.interfaces()[0]  # 抓取无线网卡列表第一个无线网卡

	print(interface.name())  # 取出本机无限网卡的名字

	interface.disconnect()  # 断开无线网卡链接
	time.sleep(3)  # 断开以后缓冲3秒

	profile = pywifi.Profile()  # 配置文件
	profile.ssid = "ACFUN"  # 就是wifi名称
	profile.auth = const.AUTH_ALG_OPEN  # 需要密码链接
	profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法
	profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
	profile.key = "123456789"

	interface.remove_all_network_profiles()  # 删除其他所有配置文件
	tmp_profile = interface.add_network_profile(profile)  # 加载配置文件

	interface.connect(tmp_profile)  # 链接
	time.sleep(10)  # 10秒内看是否可以链接上

	isOK = False
	if interface.status() == const.IFACE_CONNECTED:
		isOK = True
		print("链接成功")
	else:
		print("链接失败")

	interface.disconnect()  # 断开连接
	time.sleep(1)
	return isOK


print(test_wifi_connect())
