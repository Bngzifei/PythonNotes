"""
ConfigParser模块在python中用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含一个或多个节(section), 每个节可以有多个参数（键=值）。使用的配置文件的好处就是不用在程序员写死，可以使程序更灵活。

注意：在python 3 中ConfigParser模块名已更名为configparser
"""
"""
read(filename) #读取配置文件，直接读取ini文件内容

sections() #获取ini文件内所有的section，以列表形式返回['logging', 'mysql']

options(sections) #获取指定sections下所有options ，以列表形式返回['host', 'port', 'user', 'password']

items(sections) #获取指定section下所有的键值对，[('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('password', '123456')]

get(section, option) #获取section中option的值，返回为string类型
>>>>>获取指定的section下的option <class 'str'> 127.0.0.1

getint(section,option) 返回int类型
getfloat(section, option)  返回float类型
getboolean(section,option) 返回boolen类型
"""
# import configparser
#
# conf = configparser.ConfigParser()
# file_path = 'F:/黑马Python20期就业班/oldboy/常用模块/config.ini'
# print('file_path :', file_path)
# conf.read(file_path)
#
# sections = conf.sections()
# print('获取配置文件所有的section', sections)
#
# options = conf.options('mysql')
# print('获取指定section下所有option', options)
#
# items = conf.items('mysql')
# print('获取指定section下所有的键值对', items)
#
# value = conf.get('mysql', 'host')
# print('获取指定的section下的option', type(value), value)

# -----------------------------------综合使用------------------------------------------------------->
# import configparser

"""
读取配置文件信息
"""

# class ConfigParser():
# 	config_dic = {}
#
# 	@classmethod
# 	def get_config(cls, sector, item):
# 		value = None
# 		try:
# 			value = cls.config_dic[sector][item]
# 		except KeyError:
# 			cf = configparser.ConfigParser()
# 			cf.read('settings.ini', encoding='utf8')  # 注意setting.ini配置文件的路径
# 			value = cf.get(sector, item)
# 			cls.config_dic = value
# 		finally:
# 			return value
#
#
# if __name__ == '__main__':
# 	con = ConfigParser()
# 	res = con.get_config('logging', 'level')
# 	print(res)

# --------------------------------另一例:------------------------------>
import configparser

conf = configparser.ConfigParser()
print(conf.read('config1.ini'))  # ['config1.ini']
print(conf.sections())  # 注意会过滤掉[DEFAULT]
# 输出:['bitbucket.org', 'topsecret.com']
print(conf.items('bitbucket.org'))  # 注意items()返回的key的 字符串会全变成小写
# 输出:[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'Tom')]
print(conf.options('topsecret.com'))

"""
注意:AttributeError: module 'configparser' has no attribute 'ConfigParser'
当你的文件名就是configparser的时候,就和模块名configparser重名了
这样就会导致在import操作的时候,编译器是首先去你自己的文件名中查找configparser模块,
而不是去真正的configparser模块里面找,这样就会出错.因为你的文件没有实现ConfigParser()
这个类.所以:
千万记住:文件名千万不能使用关键字.py,模块名.py这种方式.
"""
