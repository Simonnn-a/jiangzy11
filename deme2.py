# _*_ coding:utf-8 _*-
# 作者：大汉老师
# 微信：abc554400
# @Time：2020-09-15 20:06
# @Email：896096254@qq.com
# @File: deme2.py

# 常用的数据类型
# 什么是数据类型：一类数据的类型统称
# 特点：python是不需要申明数据类型的
# python中常见的数据类型有那些？
# number、string、tuple、不可变数据类型
# list、dict、set可变数据类型

# 一、number类型（数字类型、不可变类型）
# int float bool
# 运算符
# 算数运算+ — * / // % **
# 比较运算== != > >= <= <
# 赋值运算 =  +=  -=

# 1、整数
x=6
y=2
z=x+y
print(z)
print(x+y,x-y,x*y,x/y,x//y,x%y,y**x)

# 2、浮点数
x1=5.20
y2=5.30
z1=x1+y2
print(z1)

# //向下取整
# // 除取整数，当分子分母都为整数，向下取整
nub1=8
nub2=3.0
print(nub1/nub2)
print(nub1//nub2)

# 3、布尔值 T 1  f 0
t=True
f=False
print(2+3>4)
print(1==2)

# 4、赋值运算符
a=3
b=12

# b=b+a
b+=a
print(b)

# b=b-a
b-=a
print(b)

# 5、常用的函数
# int()
print(int(5/3))

# float（）
print(float(18))
print(float(True))
print(float(False))

# 返回绝对值
# abs(数字类型的变量)
nub3=-12
print("fanhuijueduizhi",abs(nub3))

# 向上取整 math.floor()
import math
num4=2.789
print(math.floor(num4))
# 向下取整math，ceil()
print(math.ceil(num4))

# round(数字变量，小数的位数)
print(round(num4,2))

# 返回某个区间的随机整数，random
import random
print(random.randint(0,20))

# 随机返回0到1的值
print(random.random())

# 二、string类型（字符串类型、不可变数据类型）
# 1、定义字符串类型的时候可以通过单引号、双引号、三引号
str='我是女神经'
print(str)
# 2、可以支持切片，类似数组的概念
# 切片：从字符串序列中截取一部分相应的元素重新组成一个串
# 格式：字符串变量名[kaishi:jieshu:step] step默认是1
# 定义两个字符串，
# kaishi：开始截取的位置，利用索引进行标注，索引是从0开始，
str1='abcdefg'
str2='abc'

# 切片
print(str1[0:4])
# 注意：取得值是左闭右开，左边的索引包含，右边的索引值不包含

# 3、如果要获取字符串str1最后一个字符
print(str1[-1])
print(str1[:-1])
print(str1[:])

# 4、隔一个字符取一个
print(str1[::2])
# 如果是整数就从左往右取，如果是负数就从右往左取

# 5、实现字符串的翻转
print(str1[::-1])

# 6、如何更新字符串
str5='abcdefg'
# print(str5[-1])
# str5[-1]=1
# print(str5)

# 如何通过拼接的方式修改
str5=str5[:-1]+'1'
print(str5)

# 7、字符串的运算（+ *）
name1="zhangsan"
name2="lisi"
name3=name1+name2
print(name3)

# *表示的是复制的意思
print(str5*2)

# in/not in
if 'a' in str5:
    print('cunzai')
else:
    print('bucunzai')

# 8、特殊字符
# 换行\n
str6="abc\ndefg"
print(str6)

str7=r"abc\ndefg"
print(str7)

# \\替代\ 通过r转义
str8=r"F:\1.cema\1.vip课程"
print(str8)

# wo shi "zhangsan" ranhou "nine"  \'  \'' \'''  \n  \t
print('wo shi \"zhangsan\" ranhou \'''nine\'''')

# 9、字符串的格式化
# 第一种表示方法
# 比如我要打印
print("XXX工作年限：？年")
# 这些都是可变的量，所以我们可以用变量替代他
print("%s工作年限：%d年"%('zhangsan',3))

# 第二种表示方法，format需要传入值的时候要用大括号
print("{}工作年限：{}年".format('lisi',4))
# format和%的区别？
# %需要顺序传值、format不需要顺序传值，可以指定传值的位置，以索引的方式去传值
print("{1}工作年限：{0}年".format(4,'lisi'))

# 第三种方式
# f-string 它指支持3.7版本以上的内容
name="sandishui"
age="18"
print(f'{name}帅小伙：{age}岁')

# 10、字符串常见的其他内置函数
# 通过某个分割符把字符串链接起来用
# ''.join,通过-把它链接起来
list1=["nihao","shijie"]
str9='-'.join(list1)
print(str9)

# 还原成list1的形式，用.split指定分隔符，从左边开始分隔
list2=str9.split("-")
print(list2)
# 从右边进行分割，.rsplit
list3=str9.rsplit("-")
print(list3)

# 还可以具体指定还原成几个部分
list4=["nihao","shijie","zhangsan"]
str10='-'.join(list4)
print(str10)

# 可以具体指定还原时分割几次
list5=str10.split('-',1)
print(list5)

# 11、替换某个字符串，replace,除了拼接意外的方法函数
str11="abcdefg"
str12=str11.replace("abc","123")
print(str12)

# 统计字符串的方法
# 统计字符串的长度，取最大值，最小值
print(len(str11),max(str11),min(str11))

# 查找字符串 find("a",kaishi(索引值),jieshu)，得出的结果表示查找的字符所在的索引位置
print(str11.find('a',0,len(str11)))

# 如果没有找到值，匹配不到，会返回-1
print(str11.find('z',0,len(str11)))

# 还可以用index，如果匹配不到会报错
# print(str11.index('z',0,len(str11)))

# 12、判断这种业务的时候，返回的时True 或这false
# str11.isalnum()判断字母或者数字
# str11.isdigit()判断是不是整型
# str11.isdecimal()判断是不是浮点型
# str11.isalpha()是不是字母
# str11.islower()判断是不是小写
# str11.isnumeric()判断是不是数字
print(str11.isalnum())
print(str11.isnumeric(),str11.islower())

# 常见的字符串大小写转换函数有哪些
# 转换小写、大写、首字母大写
print(str11.lower(),str11.upper(),str11.capitalize())

# 13、逻辑运算符：and or not
# and 同时为正确，就是正确
# or 其中一个正确，就是正确
# not 不是这个正确，就是另一个正确
c=100
d=200
print(d>c and d>c)
print(d and c)
print(d>c or d<c)
print(d<c or d<c)
print(d or c)

# 14 位运算：通过二进制来进行运算
# 成员运算符号：in、not in
str1="nihao dahan"
if 'h' in str1:
    print("cunzai")
else:
    print("bucunzai")
# 身份运算符 is 、is not
# is就是判断两个对象是否属于同一个对象，类似内存地址
# is not 判断他是否不是属于同意对象
a1=10
b1=10
print(a1 is not b1)
print(id(a1),id(b1))
# is 指的内存地址是否一致

# 运算符的优先级，（类似与加减乘除里面先做乘除在做加减）
# 规则：先运算优先级比较搞得，在运算优先级低的


# 今天讲了什么内容
# 1、number
# 2、string

# 3、元组下节课讲
#
# 作业课后会发：1、今天课堂的代码敲3遍
#             2、待会发
#             第二个作业发邮箱


