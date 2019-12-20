print("I\'m the first.")
print(__name__)

# 下面这种格式,就是如果直接运行这个.py就会执行if之后的语句.如果是别的.py文件使用import方式导入这个文件,然后执行,这时候就不会执行if之后的语句.


if __name__ == "__main__":
	print("I\'m the second.")
