import pywifi  # pywifi模块
from pywifi import const  # 导入wifi模块的定义，


def test_status():
	wifi = pywifi.PyWiFi()  # 创建一个wifi对象

	interface = wifi.interfaces()[0]  # 取出第一个无线网卡

	if interface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:  # 没有连接上
		print("没有链接")
	else:
		print("链接上了")


test_status()
