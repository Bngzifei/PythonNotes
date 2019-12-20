# Python write()和writelines()：向文件中写入数据

"""
前面章节中学习了如何使用 read()、readline() 和 readlines() 这 3 个函数读取文件，
如果我们想把一些数据保存到文件中，又该如何实现呢？


Python 中的文件对象提供了 write() 函数，可以向文件中写入指定内容。该函数的语法格式如下：
file.write(string)

其中，file 表示已经打开的文件对象；string 表示要写入文件的字符串（或字节串，仅适用写入二进制文件中）。

注意，在使用 write() 向文件中写入数据，需保证使用 open() 函数是以 r+、w、w+、a 或 a+ 的模式打开文件，
否则执行 write() 函数会抛出 io.UnsupportedOperation 错误。


例如，创建一个 a.txt 文件，该文件内容如下：
C语言中文网
http://c.biancheng.net

然后，在和 a.txt 文件同级目录下，创建一个 Python 文件，编写如下代码：
"""
# windows下使用open最好是指定encoding="utf-8"参数,否则乱码
f = open("b.txt","w",encoding="utf-8")
f.write("写入一行三护具xxx")
f.close()

"""
前面已经讲过，如果打开文件模式中包含 w（写入），那么向文件中写入内容时，会先清空原文件中的内容，然后再写入新的内容。因此运行上面程序，再次打开 a.txt 文件，只会看到新写入的内容：
写入一行新数据

而如果打开文件模式中包含 a（追加），则不会清空原有内容，
而是将新写入的内容会添加到原内容后边。例如，还原 a.txt 文件中的内容，并修改上面代码为：
"""

f = open("b.txt", "a",encoding="utf-8")
f.write("\n再写入一行新数据")
f.close()

"""
再次打开 a.txt，可以看到如下内容：
C语言中文网
http://c.biancheng.net
写入一行新数据

因此，采用不同的文件打开模式，会直接影响 write() 函数向文件中写入数据的效果。


另外，在写入文件完成后，一定要调用 close() 函数将打开的文件关闭，否则写入的内容不会保存到文件中。例如，将上面程序中最后一行 f.close() 删掉，再次运行此程序并打开 a.txt，你会发现该文件是空的。这是因为，当我们在写入文件内容时，操作系统不会立刻把数据写入磁盘，而是先缓存起来，只有调用 close() 函数时，操作系统才会保证把没有写入的数据全部写入磁盘文件中。
"""

"""

除此之外，如果向文件写入数据后，不想马上关闭文件，也可以调用文件对象提供的 flush() 函数，它可以实现将缓冲区的数据写入文件中。例如：

"""

f = open("c.txt","w",encoding="utf-8")
f.write("写入一行新数据")
f.flush()


"""
打开 a.txt 文件，可以看到写入的新内容：
写入一行新数据

有读者可能会想到，通过设置 open() 函数的 buffering 参数可以关闭缓冲区，这样数据不就可以直接写入文件中了？对于以二进制格式打开的文件，可以不使用缓冲区，写入的数据会直接进入磁盘文件；但对于以文本格式打开的文件，必须使用缓冲区，否则 Python 解释器会 ValueError 错误。例如：


"""
# f = open("a.txt", 'w',buffering = 0)
# f.write("写入一行新数据")

"""
Traceback (most recent call last):
  File ".py", line 1, in <module>
    f = open("a.txt", 'w',buffering = 0)
ValueError: can't have unbuffered text I/O

"""


"""
Python writelines()函数


Python 的文件对象中，不仅提供了 write() 函数，还提供了 writelines() 函数，可以实现将字符串列表写入文件中。
注意，写入函数只有 write() 和 writelines() 函数，而没有名为 writeline 的函数。

例如，还是以 a.txt 文件为例，通过使用 writelines() 函数，
可以轻松实现将 a.txt 文件中的数据复制到其它文件中，实现代码如下：
"""

f = open("a.txt","r",encoding="utf-8")
n = open("x.txt","w+",encoding="utf-8")
n.writelines(f.readlines())
n.close()
f.close()






















