# Python readline()和readlines()函数：按行读取文件

"""
使用read()函数读取文件时,如果文件过大,则一次读取全部内容到内存.
容易造成内存不足.而相比每次限制读取字符(或者字节)的个数,
更推荐大家使用逐行读取文件的方式.


一般情况下,逐行读取只适用于以文本格式打开的文件,道理很简单,
只有文本才有行的概念,二进制文件没有所谓行的概念.

文件对象提供了eradline()和readlines()两个函数来逐行读取文件,其中readline()
函数用于读取一行内容,而readlines()函数用于读取文件内的所有行.

readline()函数

readline()函数用于读取文件中的一行,包括最后的换行符\n.
此函数的基本语法格式为:
file.readline([size])

其中,file为打开的文件对象,size为可选参数.用于指定读取每一行时,一次最多读取的字符数.

和 read() 函数一样，此函数成功读取文件数据的前提是，使用 open()
 函数指定打开文件的模式必须为 r（只读模式）或 r+（读写模式）。
"""

# a.txt中有两行内容，分别是：
# C语言中文网
# http://c.biancheng.net
f = open("a.txt", 'r', True,encoding="utf-8")

while True:
    # 每次读取一行
    line = f.readline()
    # 如果没有读到数据，跳出循环
    if not line: break
    # 输出line,去掉print的默认换行
    print(line,end="")
f.close()


"""
不仅如此,在逐行读取时,还可以限制每次最多读取的字符数,例如:

"""

f = open("a.txt", 'r', True,encoding="utf-8")
while True:
    # 每次读取一行
    line = f.readline(3)
    # 如果没有读到数据，跳出循环
    if not line: break
    # 输出line
    print(line)
f.close()


"""
readlines()函数

readlines()函数用于读取文件中的所有行,它和调用不指定size参数的read()类似,
只不过该函数返回时一个字符串列表,其中每个元素为文件中的一行内容.
和readline()函数一样,readlines()在读取每一行时,会连同行尾的换行符一块读取.

readlines() 函数的基本语法格式如下：
file.readlines()

其中，file 为打开的文件对象。和 read()、readline() 函数一样，
它要求打开文件的模式使用 r（只读）或者 r+（读写）。


例如如下程序：
"""
f = open("a.txt", 'r', True,encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line,end="")
