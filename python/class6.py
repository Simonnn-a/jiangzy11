#_*_ conding:utf-8 _*-
#@Time:2020/10/12 &{TIME}
# _*_ coding:utf-8 _*-
# 作者：大汉老师
# 微信：abc554400
# @Time：2020-10-11 20:08
# @Email：896096254@qq.com
# @File: demo10.py

# # 文件处理
# 主要讲了文件的读写等操作/权限
# # os模块
# 相关的函数/应用

# 文件处理具体的应用
# 1.txt
# 2.csv(类似于表格)
# 3.xml文件的读写
# excel将在web端的时候实践的时候来讲解


# # 1.txt的文件读取
# # 现在有一个txt文件,我想要去读取文件中的数据应该如何读取
# file1=open("123.txt","r",encoding="utf-8")
# # 读取文件中所有的行
# lines=file1.readlines()
# print(lines)
#
# # 如果只想获得学生的姓名
# for line in lines:
#     print(line.split(",")[0])

# with open("123.txt","r",encoding="utf-8") as file2:
#     lines=file2.readlines()
#     print(lines)
#
# for line in lines:
#     print(line.split(",")[0])

# 2.csv(类似于表格)
# 表格的后缀名是.excel,csv文件的后缀名是.csv
# 逗号分隔值,以纯文本形式存储表格数据(数字和文本)

# 读取excel常用的模块(web端实践会给大家讲)
# openyxl
# xlrd
# pandas

# csv文件读取
import csv
# file3=csv.reader(open("234.csv","r",encoding="utf-8"))
# for stu in file3:
#     print(stu)

# with open("234.csv","r",encoding="utf-8") as file4:
#     lines=file4.readlines()
#     print(lines)
#
# for line in lines:
#     print(line.split(",")[0])

# # csv文件如何写入
# # 我想对234.csv文件新增两条学生的信息
# import csv
# stu1=["dahan",18,"xinjiang"]
# stu2=["yuyan",18,"changde"]
#
# # 打开文件
# out=open("234.csv","a+",newline='')
# # 设定写入模式
# writer1=csv.writer(out,dialect='excel')
# # 写入具体的内筒
# writer1.writerow(stu1)
# writer1.writerow(stu2)

# xml文件的读写
# xml实际上有点类似于html
# xml用来传输和存储数据的
# html他是用来显示数据的

# 创建xml
# <?xml version="1.0" encoding="UTF-8"?>
# <note>根元素:根节点
# 	<Dahan id="kw">zhangsan</Dahan>子元素:子节点
# 	<to>lisi</to>
# 	<from>23</from>
# </note>

# 特点:
# 它是由标签对组成,并且区分大小写
# 标签里面可以有属性<Dahan id="kw">zhangsan</Dahan>里面的id="kw"
# 标签对里面可以存储数据<to>lisi</to>
# 标签里面可以存放子标签

# 注意:
# xml文档是必须包含根元素(父元素/根节点),这个根节点是所有元素的父元素

# dom文档对象模型
# html和xml之间的api接口,每一个对象都是一个节点

# 创建xml存储学生数据(姓名/年龄/城市),存储一些账号和密码

# xml节点3种
# 1.元素节点
# 2.文本节点
# 3.属性节点

# 每个节点里面包含了一些信息
# 节点的名称:nodeName
# 节点值:nodeValue
# 节点类型:nodeType

# # 1.读取一下元素节点(节点名称/节点值/节点类型)根节点
#
# from xml.dom import minidom
#
# # 加载xml文件
# dom=minidom.parse('qwe.xml')
# # 读取对象元素(读取的一般是根节点元素documentElement)文档元素
# root=dom.documentElement
# # 打印节点信息
# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)

# nodeType有两个值
# 1如果是元素节点返回1
# 2如果是属性节点返回2

# # 2.读取文本节点的值
# from xml.dom import minidom
#
# # 打开文件
# dom=minidom.parse('qwe.xml')
#
# root=dom.documentElement
#
# # 根据标签名称获取标签对象.getElementByTagName
# name1=root.getElementsByTagName('name')
# age1=root.getElementsByTagName('age')
# city1=root.getElementsByTagName('city')
#
# # print(name1[1].firstChild.data)
# # print(age1[1].firstChild.data)
# # print(city1[1].firstChild.data)
#
# for i in range(4):
#     print(name1[i].firstChild.data)
#     print(age1[i].firstChild.data)
#     print(city1[i].firstChild.data)
#
# # firstChild找到对应标签里面的值


# # 3.读取属性节点的值
# # 读取学生和老师的账号密码
# from xml.dom import minidom
#
# # 打开文件
# dom=minidom.parse('qwe.xml')
#
# root=dom.documentElement
#
# login1=root.getElementsByTagName('login')
#
# for i in range(2):
#     username1=login1[i].getAttribute('username')
#     print(username1)
#     password1 = login1[i].getAttribute('password')
#     print(password1)
# # .getAttribute获取属性

# 4.读取子节点信息(节点名称/节点值/节点类型)
from xml.dom import minidom

# 打开文件
dom=minidom.parse('qwe.xml')

root=dom.documentElement

root1=root.getElementsByTagName('student')

print(root1[0].nodeName)
print(root1[0].nodeValue)
print(root1[0].nodeType)