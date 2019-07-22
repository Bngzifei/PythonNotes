import multiprocessing
import os


# 拷贝文件夹里面的文件,多个任务的复制

# 线程/进程/进程池 : 三种方式均可以

# 拷贝目录的本质及时拷贝目录下的文件

# 执行拷贝  -->
def copy_file(file_name, src_path, dest_path):
	"""从源目录src_path拷贝一个文件到目的目录 dest_path"""
	# 打开源文件,目的文件
	src_file = open(src_path + '/' + file_name, 'rb')  # 打开文件的都是绝对路径,所以要我们自己去拼接绝对路径<意思就是打开哪个位置的哪个文件>
	# 使用rb/wb的方式去读写数据,避免只能 读写文本字符串的单一情况.通常我们的数据有图片,视频,音频等等,都是可以使用二进制方式进行读写操作的.
	dest_file = open(dest_path + '/' + file_name, 'wb')

	# 拷贝文件
	while True:
		file_data = src_file.read(4096)
		# 读取固定长度的数据  其他的读取方式都是文本模式下的读取方式,
		# 按照readline,readlines等方式是无法去读取图片,音频,视频等数据的,
		# 所以我们只能使用read()的方式去读取,并且设置一次读取的最大长度为4096个字节,以防止数据过大,一次读取不出来.

		if not file_data:  # 建议这么写,更加简洁,意为 如果数据不存在为真,执行if语句块里面的break跳出循环,如果不存在为假,则继续往下执行写入数据的操作. 记住:先读后写.
			break
		dest_file.write(file_data)  # 写入目标文件

	# 关闭文件
	src_file.close()
	dest_file.close()


def main():
	# 1.接收用户输入:拷贝的文件夹名称
	source_path = input('备份的目录名:')
	# 2.根据输入的文件夹名字新建一个目录 目的目录
	dest_path = source_path + '备份'
	os.mkdir(dest_path)
	# 3.获取源目录下的所有文件 返回一个列表
	file_list = os.listdir(source_path)

	# 4.创建进程池
	pool = multiprocessing.Pool(5)
	# 添加任务,使用异步的

	# 可以使用多进程,但是创建和销毁会消耗资源很多,所以使用进程池

	for i in file_list:
		# copy_file(i, source_path, dest_path)
		pool.apply_async(copy_file,args=(i, source_path, dest_path))

	# 关闭进程池
	pool.close()
	# 等待
	pool.join()


if __name__ == '__main__':
	main()
