
def clip(text:str,max_len:"int>0"=80) -> str:
	"""在max_len前面或后面的第一个空格处截断文本"""
	end = None
	if len(text) > max_len:
		space_before = text.rfind(" ",0,max_len)
		if space_before >= 0:
			end = space_before
		else:
			space_after = text.rfind(" ",max_len)
			if space_after >= 0:
				end = space_after
	if end is None:
		end = len(text)
	return text[:end].rstrip()


"""
函数声明中的各个参数可以在:之后增加注解表达式.如果参数有默认值,注解放在参数名和=号之间.
如果想注解返回值.在)和函数声明末尾的:之间添加->和一个表达式.那个表达式可以是任何类型.注解
中最常用的类型是类(如str或int)和字符串(如"int>0").

注解不会做任何处理,只是存储在函数的__annotations__属性中.
Python对注解所做的唯一的事情是,把它们存储在函数的__annotations__属性里.仅此而已,Python不做检查,
不做强制,不做验证,什么操作也不做.换句话说,注解对Python解释器没有任何意义.注解只是元数据,可以供IDE,
框架和装饰器等工具使用.目前仅知道inspect.signature()函数知道怎么提取注解.


"""