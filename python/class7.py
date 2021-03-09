#_*_ conding:utf-8 _*-
#@Time:2020/10/15 &{TIME}
# 回归:
# 文件处理和os模块2
# 1.txt文件的读写
# 2.csv文件的读写(类似于表格)
# 3.xml文件的读写

# 时间相关模块/异常处理函数
# (1)time模块

import time
# 时间戳:描述某个时间(格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒),到另一个时间相隔的秒数叫时间戳
# 时间元祖:用一个元祖组装起来的9组数字表示时间
t=(2020,10,13,20,16,22,0,0,0)

# 时间的表示方式,常用的是以下三种
# 1.如何获取当前时间的时间戳
print("当前时间的时间戳",time.time())

# 2.如何获取时间的时间元祖
print("获取当前时间的时间元祖",time.localtime())

# 3.通过英文的方式表示时间
print("以英文的方式表示时间",time.asctime())

# 如何获取元祖的部分信息
print("获取元祖部分的信息",time.localtime().tm_year
      ,time.localtime().tm_mon
      ,time.localtime().tm_mday)

# 三种方式的相互转换
# 1.元祖转化为时间戳
print("元祖转化为时间戳",time.mktime((2020,10,13,20,16,22,0,0,0)))
# 1.2当前系统时间元祖,转换成时间戳
print("当前系统时间元祖,转换成时间戳",time.mktime(time.localtime()))

# 2.时间戳转化为时间元祖
# time.localtime(时间戳)
print("时间戳转化为时间元祖",time.localtime(1501223444))
# 2.1现在的时间戳转化成时间元祖
print("现在的时间戳转化成时间元祖",time.localtime(time.time()))

# 3.元祖转换时间格式字符串
# time.strftime("时间格式的样式",时间元祖)
# 要把当前的时间转换成年月日时分秒
print("要把当前的时间转换成年月日时分秒",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 4.时间格式字符串转化为时间元祖
# time.strptime(时间字符串,时间格式的样式)
print(time.strptime("2020-10-13 20:36:17","%Y-%m-%d %H:%M:%S"))


# (2)datetime模块时间日期
import datetime
# 1.以时间元祖创建日期时间
# 前三个参数是必填的,后面的参数可以不写
print(datetime.datetime(2020,10,13,20,41,23))
print(datetime.datetime(2020,10,13))

# 如何获取当前的日期时间
print("如何获取当前的日期时间",datetime.datetime.now())
print("如何获取当前的日期时间2",datetime.datetime.today())

# 2.时间表示形式相互转换
# 如何把日期时间转化为时间戳timestamp
print("把日期时间转化为时间戳",datetime.datetime.now().timestamp())

# 时间戳转化为日期时间
print(datetime.datetime.fromtimestamp(1602593193.43386))

# 时间格式字符串与时间日期的相互转换
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 与之相反还有一个方法时间字符串转化为时间
print(datetime.datetime.strptime("2020_10_13 20:50:12","%Y_%m_%d %H:%M:%S"))

# (3)calendar日历模块
import calendar
# 年历
# print(calendar.calendar(2020))
# 月历
print(calendar.month(2020,10))

# 判断一个年份是否为闰年
print(calendar.isleap(2020))

# 给你一个日期判断是星期几
print(calendar.weekday(2020,10,13))

print(time.localtime().tm_wday)
print(datetime.datetime.now().weekday())


# 异常处理函数
# python异常

# 异常处理语句
# try...except...
# try...except...as
# try...except...else
# try...except...finally
# raise

# 1.try...except...
# 语法结构
# try:
#     执行的代码块1
# except:
#     出现异常执行代码块2

# num1=int(input("请输入数字:"))
# print(num1+10)

# try:
#     num1 = int(input("请输入数字:"))
#     print(num1 + 10)
# except ValueError:
#     print("输入的不是数字")

# 常见的错误类型:
# FileNotFoundError
# NameError
# BaseException所有异常的基类
# ValueError

# try:
#     file1=input("请输入要打开的文件名:")
#     open("%s.txt" %file1)
# except FileNotFoundError:
#     print("文件没有找到")

# stu="zhangsan"
# print(stu)

# try:
#     stu = "zhangsan"
#     print(stu)
# except NameError:
#     print("变量没有找到")


# try:
#     print(stu)
# except BaseException:
#     print("stu没有找到")

# 如何捕捉系统给的提示信息?

# print(stu)
# NameError: name 'stu' is not defined

# # 用try...except...as语句
# try:
#     print(stu)
# except BaseException as msg:
#     print(msg)

# try:
#     # stu="zhangsan"
#     print(stu)
# except BaseException as msg:
#     print(msg)
# else:
#     print("好像没什么问题")

# try...except...finally语句
# 不管try后的语句是否有异常都会向下执行
# try:
#     # stu="zhangsan"
#     print(stu)
# except BaseException as msg:
#     print(msg)
# finally:
#     print("好像没什么问题")


# 总结:
# try:
#     执行的代码块1
# except 错误类型 as 变量:
#     执行的代码块2:出现异常执行此代码块
# else:
#     执行的代码块3:代码没有异常会执行的代码块
# finally:
#     执行的代码块4:不管是否有异常都会执行的代码块

# 当你的代码没有异常的时候:1,3,4
# 有异常的时候:1,2,4

# raise 抛出异常(只能用于python中的标准异常类)
def division(x,y):
    if y==0:
        raise ZeroDivisionError("不能为0")
    return x/y
try:
    res1=division(12,0)
    print(res1)
except BaseException as msg:
    print(msg)
