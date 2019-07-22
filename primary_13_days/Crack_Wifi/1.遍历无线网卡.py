import time
import pywifi


def test_wifi():
	wifi = pywifi.PyWiFi()  # 初始化wifi
	interface = wifi.interfaces()[0]  # 取出第一个无线网卡
	interface.scan()  # 扫描
	time.sleep(15)  # 扫描wifi
	basses = interface.scan_results()  # 扫描结果

	for data in basses:
		# print(data.bssid)
		print(data.ssid)  # wifi名称


test_wifi()  # 扫描wifi,
