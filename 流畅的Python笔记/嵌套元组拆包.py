"""
接受表达式的元组可以是嵌套式的,例如(a,b,(c,d)). 只要这个接受元组的嵌套结构符合表达式本身的
嵌套结构,Python就可以做出正确的对应.


示例:用嵌套元组来获取经度
"""

metro_areas = [
	("Tokyo","JP",36.933,(35.689722,139.6991677)),
	("Delhi NCR","IN",21.935,(28.613889,77.208889)),
	("Mexico City","MX",20.142,(19.433333,-99.133333)),
	("New Your-Newark","US",20.104,(40.808611,-74.020386)),
	("Sao Paulo","BR",19.649,(-23.547778,-46.635833)),
]

print("{:15} | {:^9} | {:^9}".format("","lat.","long."))
fmt = "{:15} | {:9.4f} | {:9.4f}"
for name,cc,pop,(latitude,longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name,latitude,longitude))
