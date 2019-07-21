"""文件备份:
原理:先读取旧文件,后写入新文件
1.[附件]123.txt

2.123[附件].txt
"""

# old_file_name = input('备份文件名:')
# # new_file_name = '[附件]' + old_file_name # 拼接新文件名
# index = old_file_name.rfind('.')  # 为了确保查找到的最后一个.,所以从右向左查找索引,查找指定字符的索引
#
# new_file_name = old_file_name[:index] + '[附件]' + old_file_name[index:]
#
# with open(old_file_name, 'r') as old_f:
# 	with open(new_file_name, 'w') as new_f:
# 		# 1.先读取旧文件,再写入新文件
# 		content = old_f.read()
# 		new_f.write(content)

# oldf = input('输入需要备份的文件:')
# index = oldf.rfind('.')  # 找到.所在的索引位置,目的是为了文件后缀的名字
# newf = oldf[:index] +'副本'+ oldf[index:]
#
# with open(oldf,'r') as f1:
#     with open(newf,'w') as f2:
#         file = f1.read()
#         f2.write(file)

old_file = input('输入需要备份的文件:')
index = old_file.rfind('.')  # 找.分隔符索引位置
new_file = old_file[:index] + '{副本}' + old_file[index:]

with open(old_file, 'r+') as of:
	with open(new_file, 'w') as nf:
		file = of.read()
		nf.write(file)
