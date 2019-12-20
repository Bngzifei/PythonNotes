"""
编程：使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自 键盘的输入
"""

# name = input("姓名:")
# age = int(input("年龄:"))
# stu_num = input("学号:")
# qq = input("qq:")
# wechat = input("微信:")
# address = input("住址:")
#
# user = {
# 	"name": "%s" % name,
# 	"age": "%d" % age,
# 	"stu_num": "%s" % stu_num,
# 	"qq": "%s" % qq,
# 	"wechat": "%s" % wechat,
# 	"address": "%s" % address,
# }
# print(user)

"""
完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印出字符串长度
使用切片逆序打印出字符串
"""
# 法1:
# while True:
# 	str1 = input("输入字符串(长度小于31):")
# 	if 31 > len(str1) >= 1:
# 		print('长度为%d' % len(str1))
# 		print('逆序排列为:%s' % str1[::-1])
# 		break  # 反正是要终止循环跳出的,灵活应用
# 	else:
# 		print('输入错误,请重新输入')
# 法2:
# while True:
# 	str = input('输入字符串:')
# 	if len(str) >= 31 or len(str) < 1:
# 		print('错误')
# 		continue
# 	break
# print(len(str))
# print(str[::-1])

"""
用户名和密码格式校验程序
要求从键盘输入用户名和密码，校验格式是否符合规则，如果不符合，打印出不符合的原因，并提示重新输入
用户名长度6-20，用户名必须以字母开头
密码长度至少6位，不能为纯数字，不能有空格
"""
# str2 = ' '
# while True:
# 	username = input('输入用户名:')
# 	password = input("输入密码:")
#
# 	str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 	if 5 < len(username) < 21:
# 		if username[0] in str1:
# 			pass
# 		else:
# 			print("用户名必须以字母开头")
# 	else:
# 		print('用户名长度必须为6-20位')
#
# 	if len(password) > 5:
# 		if password.isdecimal():
# 			print("密码不能全是数字")
# 		else:
# 			pass
# 		if not password.find(str2):
# 			print("密码中不能有空格")
# 		break

# while True:
#     # 获取用户输入
#     username = input("请输入用户名：")
#     # 如果输入“QUIT”则退出程序
#     if username == "QUIT":
#         break
#     # 获取输入的密码
#     passwd = input("请输入密码：")
#     # 校验用户名格式是否在6-20之间
#     if len(username)<6 or len(username)>20:
#         print("请输入有效的用户名，长度6-20，且必须以字母开头")
#         print("请重新输入")
#         # 如果不正确直接重新开始 ，所以使用continue
#         continue
#     # 查看用户名是不是以字母开头
#     if username[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(username[0])
#         print("请输入有效的用户名，长度6-20，且必须以字母开头")
#         print("请重新输入")
#         # 如果不正确直接重新开始 ，所以使用continue
#         continue
#     # 校验密码格式6位，不能为纯数字，不能有空格
#     if len(passwd) < 6 or passwd.isdigit() or " " in passwd:
#         print("密码长度至少6位，不能为纯数字，不能有空格")
#         print("请重新输入")
#         # 如果不正确直接重新开始 ，所以使用continue
#         continue
#     print("校验成功")
#     print("="*20)
"""
名片管理器v1.0
要求优化之前的打印名片程序
控制姓名长度为6-20
电话号码长度11
性别只能允许输入男或女
每一样信息不允许为空
"""

# name = input("姓名:")
# age = int(input("年龄:"))
#
# if len(name) < 6 or len(name) > 20 or name is '' or name is ' ':
# 	print("姓名不能为空,长度为6-20位")
#
# phone = input("微信:")
# if len(phone) != 11 or phone is '' or phone is ' ':
# 	print("手机号不能为空,长度为11位")
#
# gender = input('请输入性别:(男/女)')
# if gender == '男' or gender == '女':
# 	pass
# else:
# 	print("输入性别错误")
#
# address = input("住址:")
# if address is '' or address is ' ':
# 	print('不允许地址为空')
# else:
# 	pass
#
# user = {
# 	"name": "%s" % name,
# 	"age": "%d" % age,
# 	"gender": "%s" % gender,
# 	"phone": "%s" % phone,
# 	"address": "%s" % address,
# }
# print(user)
