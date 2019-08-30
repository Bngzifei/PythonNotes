# Python read()函数：按字节（字符）读取文件

"""
Python read()函数：按字节（字符）读取文件

文件对象（open() 函数的返回值）提供了 read() 函数
可以按字节或字符读取文件内容，到底是读取字节还是字符，
取决于使用 open() 函数打开文件时，是否使用了 b 模式，如果使用了 b 模式，
则每次读取一个字节；反之，则每次读取一个字符。

read() 函数的基本语法格式如下：
file.read([size])

其中，file 表示打开的文件对象；size 作为一个可选参数，用于指定要读取的字符个数，
如果省略，则默认一次性读取所有内容。


【例 1】采用循环读取整个文件的内容。
"""

# a.txt 文件内容为：C语言中文网
f = open("a.txt","r",True,encoding="utf-8")

while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读到数据,跳出循环
    if not ch:
        break
    # 输出ch
    print(ch,end="")

f.close()
"""
运行结果为：
C语言中文网

上面程序采用循环依次读取每一个字符（因为程序没有使用 b 模式），每读取到一个字符，程序就输出该字符。
正如从上面程序所看到的，当程序读写完文件之后，推荐立即调用 close() 方法来关闭文件，
这样可以避免资源泄露（后续章节会详细介绍 close() 函数）。


注意:在调用read()函数读取文件内容时,成功读取的前提是在open()函数中使用r或者r+的
模式打开文件,否则(比如将上面程序中的open打开模式改为w),程序就会抛出io.UnsupportedOperation
异常:


【例 2】调用 read() 方法时不传入参数，该方法默认会读取全部文件内容。例如：
"""
f = open("a.txt","r",True,encoding="utf-8")

# 直接读取全部文件
print(f.read())
f.close()


"""
read()函数抛出UnicodeDecodeError异常的解决方法
当使用 open() 函数打开文本文件时，默认会使用当前操作系统的字符集，比如 Windows 平台，open() 函数默认使用 GBK 字符集。
因此，上面程序读取的 a.txt 也必须使用 GBK 字符集保存；否则，程序就会出现UnicodeDecodeError错误。

如果要读取的文件所使用的字符集和当前操作系统的字符集不匹配，则有两种解决方式：
使用二进制模式读取，然后用 bytes 的 decode() 方法恢复成字符串。
利用 codecs 模块的 open() 函数来打开文件，该函数在打开文件时允许指定字符集。


"""
# 指定使用二进制方式读取文件内容，a.txt 以 utf-8 编码存储
f = open("a.txt", 'rb', True)
# 直接读取全部文件，并调用bytes的decode将字节内容恢复成字符串
print(f.read().decode('utf-8'))
f.close()

"""
上面程序在调用 open() 函数时，传入了 rb 模式，这表明采用二进制模式读取文件，
此时文件对象的 read() 方法返回的是 bytes 对象，程序可调用 bytes 对象的 decode() 方法将它恢复成字符串。由于此时读取的 a.txt 文件是以 UTF-8 的格式保存的，因此程序需要使用 decode() 方法恢复字符串时显式指定使用 UTF-8 字符集。
"""

"""
下面程序使用 codes 模块的 open() 函数来打开文件，此时可以显式指定字符集：
"""

import codecs

# 指定使用utf-8字符集读取文件内容
f = codecs.open("a.txt","r","utf-8",buffering=True)
while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读取到数据,则跳出循环
    if not ch:break
    # 输出ch
    print(ch,end="")

f.close()

"""
上面程序在调用 open() 函数时显式指定使用 UTF-8 字符集，
这样程序在读取文件内容时就完全没有问题了.
"""















