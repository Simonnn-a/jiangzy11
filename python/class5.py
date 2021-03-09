#_*_ conding:utf-8 _*-
#@Time:2020/10/9 &{TIME}
# _*_ coding:utf-8 _*-
# 作者：大汉老师
# 微信：abc554400
# @Time：2020-10-08 20:11
# @Email：896096254@qq.com
# @File: demo9.py

# 课前回归
# 1.python基础
# 2.python的常见数据类型(不可变数据类型/可变数据类型)
# 3.条件判断语句和循环判断语句
# 4.函数模块的应用模块的导入

# 文件及os模块
# 打开文件open()
# file=open(file_name路径,访问模式)
# r :以只读的方式打开
# rb:以二进制格式打开一个文件用于只读
# w:打开一个文件只用于写入
# a:追加
# Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要
# 使用到这个函数
# 格式：open(file_name[,access_mode][, buffering])
# 	file_name:文件路径。
# 	access_mode:打开文件的模式。只读,写入,追加等,默认文件访问模式为只读(r)。
# 	buffering:为0表示不会寄存行。为1会寄存行。如果大于1的整数，表明了是寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
# access_mode参数有：
#  r		以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#
# 注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# access_mode参数有：
#  r		以只读方式打开文件。文件的指针将在文件开头。这是默认模式。
#  rb		以二进制格式打开一个文件用于只读。一般用于非文本文件如图片等
#  r+		打开一个文件用于读写(文件的指针将在文件开头)
#  w		打开一个文件只用于写入,如果文件存在，删除重新编辑，否则新建
#  wb	以二进制格式打开一个文件只用于写入
#  w+	打开一个文件用于读写。如果文件存在，删除重新编辑，否则新建写入
#  a 		 打开文件追加内容，存在文件，在文件原内容后增加，否则新建写入
#  a+	打开一个文件用于读写。存在文件，在文件原内容后增加，否则新建用于读写
#  ab	以二进制格式打开一个文件用于追加，存在文件，在文件原内容后增加，否则新建写入
#  ab+ 	以二进制格式打开一个文件用于读写。存在文件，在文件原内容后增加，否则新建用于读写




# 在当前路径下创建一个文本文件
# file1=open("1.txt","w+")
# 注意:对文件操作完后,一定要记得关闭文件,否则会占用服务器的内存
# file1.close()

# 往文件中写入内容
# file1.write('''zhangsan1
# zhangsan2
# zhangsan3
# zhangsan4
# zhangsan5
# zhangsan6
# ''')

# read():每次读取整个文件,
# readline():每次读取一行内容
# readlines():一次性读取文件所有行,自动将文件内容分析成一个行的列表,for  in结构进行处理

# file2=open("1.txt","r+")
# 用read的方式读取文件内容
# print(file2.read())
# file2.close()

# 读取一行内容
# print(file2.readline())

# 循环读取所有行的内容
# for x in file2.readlines():
#     print(x)

# 读取指定某一行的数据,返回到一个列表中
# print(file2.readlines()[1])

# 如何获取指针当前的位置tell
# file3=open("1.txt","r+")
# file3.readline()
# file3.readline()
# print(file3.tell())

# 想要往文件中增加一行内容
# a+:做追加,指针放在文件末尾去追加
# w+:先找到文件,然后把指针放在开头,把源文件清空,最后才去加入内容
# file4=open("1.txt","w+")
# file4.write("dahan1\ndahan2")

# seek(偏移数,参数数)
# 参数数 : 0 文件开头进行读取
# 1表示从当前位置进行读取
# 2从文件末尾开始读取
# file5=open("1.txt","r+")
# # seek(x,y)从文件y位开始,读取x个字符
# # 从文件的开头开始读取偏移2个字符
# file5.seek(2,0)
# print(file5.readlines())
#
# # 读取6个字符
# file5.seek(0,0)
# print(file5.read(6))


# with...as可以自动关闭文件的,不需要另外调用close去关闭文件
# with open(路径,模式) as 变量:
#     代码块
# with open("1.txt","r") as file1:
#     # 对文件进行其他操作
#     print(file1.read())

# os模块:提供了很多方法来处理文件及目录
# Python的os模块提供了帮你执行文件处理操作的方法:
# 创建文件夹 mkdir(path)
# 创建多级目录os.makedirs(path)
# 删除空目录os.rmdir(path)
# 删除非空目录shutil.rmtree(path)
# 重命名os.rename(oldname,newname)
# 获取当前目录os. getcwd()
# 获取文件权限os. access(path,mode)
# Mode:os. F_OK(是否存在)、os.R_OK（可读 ）、os.W_OK（可写）、os.X_OK（可执行）
# 获取文件权限os. access(path,mode)
# 检验给出的路径是否是一个目录os.path.isdir()、 os.path.isfile()
# 更改文件目录权限os.chmod(path, mode)
# 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限

import os

# file6=r"C:\Users\m1877\Desktop\dahan"
# 创建一个目录
# os.mkdir(file6)

# 删除目录
# 删除空目录
# os.rmdir(file6)

# 删除非空目录
# import shutil
# shutil.rmtree(file6)

# 如何重命名目录
# os.rename(原文件名,新文件名)
# os.rename(r"C:\Users\m1877\Desktop\dahan1",r"C:\Users\m1877\Desktop\dahan2")

# 如何获取当前文件项目的路径os.getcwd
# print(os.getcwd())

# 获取上级(父级)路径
# path1=os.getcwd()
# print(path1)
# parent1=os.path.join(path1,os.pardir)
# # os.pardir获取当前目录的父目录(上一级目录)
# # os.path.join连接两个或更多路径的一个组件
# print("爸爸1:",parent1)
# print("父级路径:",os.path.abspath(parent1))
# os.path.abspath(__file__)他的作用:获取当前脚本的完整路径

# 获取文件权限os. access(path,mode)
# Mode:os. F_OK(是否存在)、os.R_OK（可读 ）、os.W_OK（可写）、os.X_OK（可执行）
# os.access(路径,模式)它的作用是检验文件或目录的权限
# 比如我要访问一个路径下是否存在1.txt这个文件
# file7=r"C:\Users\m1877\Desktop\dahan2\1.txt"
# print(os.access(file7,os.F_OK))
# print("判断文件是否可写",os.access(file7,os.W_OK))
#
# # 判断路径是否是文件或者目录
# # 判断是否为文件
# print(os.path.isfile(file7))
# # 判断是否为目录(文件夹)
# print(os.path.isdir(file7))
#
# # 目录和文件拼接成路径
# print("拼成:",os.path.join(r"C:\Users\m1877\Desktop\dahan2","1.txt"))
#
# # 可以把路径分割成目录和文件,存放在元祖里
# print(os.path.split(file7))


#如何更改文件的权限os.chmod(path,mode),mode可读r/可写w/可执行x
# 所有者USR
# 其他用户OTH
# 用户所在组的权限GRP
# 想要修改某个文件的权限
import stat
file8=r"C:\Users\m1877\Desktop\dahan2\1.txt"
# windows下取消只读
os.chmod(file8,stat.S_IWRITE)