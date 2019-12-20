"""
w:write 只能写入
r:read 只读
a:add 追加

utf-8:一个汉字占用3个字节
GBK:一个汉字占用2个字节
所以优先使用GBK进行中文编码
8个字节是一个Bytes
编码和解码一定要一致
GBK(简体汉字) BIG(繁体汉字) UTF-8(英文字符,国际码)

"""

with open('22223.txt', 'w+') as f:
	f.write('12333')
	# print(f.read())  # 这样又读又写是不可以的,在指定的模式下只能进行对应的操作.

# with open('222.txt', 'r') as f:
# 	content = f.read()
# print(content)

with open('22224.txt', 'w',encoding='utf-8') as f:
	f.write('您好吗?')  # 会自动识别编码格式 GBK(简体汉字) BIG(繁体汉字) UTF-8(英文字符,国际码)
