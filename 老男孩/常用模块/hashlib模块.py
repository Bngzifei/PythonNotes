print('--------------哈希模块------------------------------->')
"""
1.>什么叫hash:hash是一种算法（3.x里代替了md5模块和sha模块，
主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法），
该算法接受传入的内容，经过运算得到一串hash值
2.>hash值的特点是：
只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
不能由hash值返解成内容=======>把密码做成hash值，不应该在网络传输明文密码
只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的

理解:hash算法就像是一座工厂,工厂接收你送来的原材料(可以使用,.update()为工厂运送原材料).
经过加工返回的产品就是hash值.

"""
# --------------------示例-------------------------------------->
import hashlib
m = hashlib.md5()
m.update('hello'.encode())

print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592

m.update('alvin'.encode())
print(m.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af

"""
注意:把一段很长的数据update多次,和一次update这段长数据,得到的结果一样,但是
update多次为校验大文件提供了可能.

缺点:通过撞库可以反解.
如何改进?
  对加密算法添加自定义的key进行加密<即改装这个函数的加密规则>

"""

# --------------------------示例-------------------------------->

import hashlib
hash = hashlib.sha256('898opFgt'.encode())
hash.update('hello'.encode())
# 二次加工后的结果:ff46d14b1f9817291faf283249d5172ee85bb61fb9fa869250158681a3c4ca2b
print(hash.hexdigest())

# --------------------模拟撞库破解密码--------------------------->
import hashlib
password = [
	'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
	'hello',
]

def make_password_dic(passwds):
	dic = {}
	for passwd in passwds:
		m = hashlib.md5()
		m.update(passwd.encode())
		dic[passwd] = m.hexdigest()
	return dic

def break_code(cryptograph,passwd_dict):
	for key,val in passwd_dict.items():
		if val == cryptograph:
			print('密码是>>>:\033[46m%s\033[0m' % key)

cryptograph = '5d41402abc4b2a76b9719d911017c592'

break_code(cryptograph,make_password_dic(password))

"""
注意:这么破解的前提是先得拿到一定量的密码字典,否则也出不来.

Python还有一个模块hmac模块,它内部对我们创建key和内容进行进一步的处理然后再加密

"""
# ----------------------示例--------------------------->

import hmac
h = hmac.new('hell'.encode())
h.update('hello'.encode())
print(h.hexdigest())  # f141c49a8b9d49169695929bad880358

"""
注意:
要想保证hmac最终的结果一致,必须保证:
1.>hmac.new括号内指定的初始key一样
2.>无论update多少次,校验的内容累加到一起是一样的内容

"""
import hmac

h1 = hmac.new(b'egon')
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2 = hmac.new(b'egon')
h2.update(b'helloworld')
print(h2.hexdigest())

# f1bf38d054691688f89dcd34ac3c27f2
# f1bf38d054691688f89dcd34ac3c27f2

# new里面的初始key已经变了
h3 = hmac.new(b'egonhelloworld')
print(h3.hexdigest())
# bcca84edd9eeb86f30539922b28f3981
