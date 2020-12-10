# coding:utf-8


# infos = [
# 	{"boot_err01": "10.103.112.221"},
# 	{"boot_err01": "10.103.112.222"},
# 	{"boot_err02": "10.103.112.223"}
# ]

ip2errcode_info = {
	"10.103.112.221": "boot_err01",
	"10.103.112.222": "boot_err01",
	"10.103.112.223": "boot_err02",
	"10.103.112.224": "boot_err02",
	"10.103.112.225": "boot_err04",
	"10.103.112.226": "boot_err05",
}
# {'boot_err01': ['10.103.112.222'], 'boot_err02': ['10.103.112.223']}
errcode2ip_info = {v: [k] for k, v in ip2errcode_info.items()}
print(errcode2ip_info)

# 其实就是对一个字典来说,知道了value,如何取key?
for ip, err_code in ip2errcode_info.items():
	# boot_err01 这个参数是咋来的
	for code in errcode2ip_info.keys():
		if err_code == code and ip not in errcode2ip_info[err_code]:
			errcode2ip_info[err_code].append(ip)
# 对,就是这样
print(errcode2ip_info)
# {'boot_err01': ['10.103.112.222', '10.103.112.221'], 'boot_err02': ['10.103.112.224', '10.103.112.223'], 'boot_err04': ['10.103.112.225'], 'boot_err05': ['10.103.112.226']}
# 然后,后面的步骤就是,先根据这个err_code去异常类型的json文件里面去查找,判等,如果找到了,
# 就拼接异常信息类型, 怎么拼接?
# 主机 10.103.80.20 boot_err01对应的异常信息
# 还要注意中英文转换

		



