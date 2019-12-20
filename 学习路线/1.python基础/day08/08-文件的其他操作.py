import os

"""文件重命名"""
# dst:目标,destination

# os.rename('123.txt','888.txt')

"""删除文件"""
# os.remove('888.txt')

"""获取当前默认路径"""

# print(os.getcwd())


"""创建文件夹"""
# os.mkdir('demo')


"""修改默认路径"""
# os.chdir('demo')
# print(os.getcwd())


"""获取当目录内所有内容"""
# print(os.listdir())


"""删除空的文件夹"""
# os.remove('demo/123.txt')  # 先删除指定文件中的文件
# os.rmdir('demo')  # 先保证是空的文件夹
# [WinError 3] 系统找不到指定的路径
