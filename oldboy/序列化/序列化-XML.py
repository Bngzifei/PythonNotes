print('序列化XML...')

"""
XML是实现不同语言或者程序之间进行数据交换的协议,和json类似,但是json使用起来更加简单.
不过,在json还没有诞生之前,大家只能使用XML,目前很多传统的金融行业的系统接口还主要是XML
格式.

就是通过标签封装了数据,只是包装数据的方式不同而已.

json比较简洁

标签语言
标签:1.> 自闭合标签  --->  <neighbor name="Austria" direction="E"/>  就是自己一个标签,neighbor只有自己一个 
	 2.> 非自闭合标签 --->  <rank updated="yes">2</rank>  就是有头有尾的 rank 出现在头部和尾部

也可以使用字典套字典的格式来存储这些数据信息

模块就是一个接口,我们是想拿到接口里面的方法等等
操作:就是增删改查四种.

import ... as ... 简写,无所谓了

parse:解析的意思

结构是一个树形结构,简称为文倒树.
"""

# import xml.etree.ElementTree as ET
# parse():解析方法,tree出来就是一个对象
# tree = ET.parse("xml_lesson")
# 获取根节点data对象
# root = tree.getroot()
# print(root)  # <Element 'data' at 0x00000124E5247868>  看到这种有地址的都是一个对象.
# 根标签的名字 data
# print(root.tag)  # data  根节点这里没有属性

# 属性(attrib)是一个键值对,key-value成对出现,譬如 {'name': 'Liechtenstein'},就是解释这个标签的作用,意思.
# 遍历xml文档
# for child in root:
# 	print(child.tag, child.attrib)
# 	for i in child:
# 		print(i.tag, i.text)
#
# 只遍历year节点
# for node in root.iter('year'):
# 	print(node.tag, node.text)
# ---------------------------------------

# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xml_lesson")
# root = tree.getroot()

# 修改
# for node in root.iter('year'):
# 	new_year = int(node.text) + 1
# 	node.text = str(new_year)
# 	# set() 修改属性,是一个键值对 key-value
# 	node.set("updated", "yes")
# 重新写入一个新的文件中才会把之前在内存中进行的修改操作生效.
# tree.write("xmltest.xml")  # 文件名可以和原来一样(覆盖原来的文件),也可以不一样.

# 删除node
# for country in root.findall('country'):
# 	rank = int(country.find('rank').text)
# 	if rank > 50:
# 		root.remove(country)

# tree.write('output.xml')


"""
tag:标签
attrib:属性,返回值是一个键值对,字典类型
text:文本内容,具体的数据值,标签实际包裹的内容.

"""

"""自己创建一个XML文件"""

import xml.etree.ElementTree as ET
# 创建根节点namelist  <namelist></namelist>
new_xml = ET.Element("namelist")
# 插入子节点   <namelist><name enrolled="yes"></name></namelist>
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'

name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'
# 生成文档树
et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)
# 打印生成的格式
# <namelist><name enrolled="yes"><age checked="no" /><sex>33</sex></name><name enrolled="no"><age>19</age></name></namelist>
# 生成样式
# <namelist>
# 	<name enrolled="yes">
# 		<age checked="no">
# 		<sex>33</sex>
# 		</age>
# 	</name>
# </namelist>