#_*_ conding:utf-8 _*-
#@Time:2020/9/23 &{TIME}
# n=0
# for c in "http://www.baidu.com/":
#    n = n + 1
# print(n)
#
# # 什么是函数?
# # 函数是组织好的,可以重复使用的,用来实现单一或相关功能的代码段.
# # 自己创造的函数,叫自定义函数
# # 函数的定义
# # def 函数名(参数列表):
# #     //实现了特定功能的多行代码
# #     [return [返回值]]
#
# # 定义一个函数:用来比较两个数字大小的函数,然后将数值大的数字返回
# def bidaxiao(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else:
#         return a
#
# # 调用函数:
# # 返回值=函数名(值或者参数变量)
# jieguo=bidaxiao(12,15)
# print(jieguo)
#
# # 定义一个空函数,没有实际意义的
# def konghanshu():
#     pass
#
# # 参数的传递
# # 形式参数:在定义函数时,函数名后面括号中的参数就是形式参数
# # 实际参数:就是在调用函数时,函数名后面括号中的参数称为实际参数
#
# # 值传递,引用传递
# # 值传递适用于不可变类型字符串数字元祖
# # 通过函数体后不能修改函数外变量的值
# #
# # 引用传递适用可变类型列表字典
# # 通过函数体可以改变函数外参数的值
# list1=[1,2,3,4]
# def changelist(listn):
#     list1.append(listn)
#
# changelist([5,6,7,8])
# print(list1)
#
# # 参数类型
# # 必须参数,关键字参数,默认参数,不定长参数
# # (1)必须参数
# def hanshuming1(canshu1,canshu2):
#     print(canshu1,canshu2)
# # 调用它
# # hanshuming1("chuanru1")
# hanshuming1("chuanru1","chuanru2")
# # 必须参数:必须以正确的顺序传入参数,调用时参数数量必须和申明时一样
#
# # (2)关键字参数
# # 时一个特殊的必须参数,他可以通过关键字传值,
# # hanshuming1(canshu2="chuanzhi2")
# hanshuming1(canshu2="chuanzhi2",canshu1="chuanzhi1")

# (3)默认参数:在定义的过程中设置了默认值
# # 定义
# def hanshuming2(canshu1,canshu2="morenzhi"):
#     print(canshu1,canshu2)
#
# # 调用
# # hanshuming2("chuanzhi3")
# # 如果有默认值,我传入一个新值,新值会覆盖掉默认值
# hanshuming2("chuanzhi3","chuanzhi4")
# # 也可以用关键字去传入参数
# hanshuming2(canshu1="chuanzhi5")

# (4)不定长参数
# 在定义的过程中,不确定会有多少个参数,就设置成不定长参数
# 可以在参数前加一个*,或者**星表示不定长参数
# (1)参数前面带一个*,把不确定长度的参数存储在元祖里,可以通过元祖调用其中某一个参数
# 定义不定长参数
# def a(name,*canshuming):
#     print(name)
#     print(canshuming)
#
# # 调用不定长参数
# a("zhangsan","17","changsha")

# (2)参数前面带两个*,把不确定长度的参数存储在字典里面

# def a(name,**canshuming):
#     print(name)
#     print(canshuming)
# a("zhangsan",nianling="17",dizhi="changsha")

# *可以单独出现,在调用的时候必须通过关键字传值
# def a(num1,num2,*,num4):
#     return num1+num2+num4
# print(a(1,2,num4=4))

# 注意不定长参数可以单独存在,
# def a2(*yu):
#     print(yu)
#
# a2()
# # *和**的不定长参数也可以同时被定义
# def a3(*shizhisha1,**shizhisha2):
#     print(shizhisha1)
#     print(shizhisha2)
# a3(1,2,3,name="zhangsan",nianling=18)

# 函数的嵌套
# 函数与函数之间可以进行相互调用
# 调用嵌套:在定义的过程中调用另一个哈数
# def a6():
#     print("nihao a6")
# def b6():
#     print("nihao b6")
#     a6()
# b6()

# 定义嵌套:在函数里面定义函数
# def a7():
#     print("nihao a7")
#     def b7():
#         print("nihao b7")
#     b7()
# a7()

# 函数的递归
# 自己调用自己
# def a8():
#     print("nihao a8")
#     a8()
# a8()
# 调用出现死循环
#
# def a9():
#     print("nihao a9")
#     b9()
# def b9():
#     print("nihao b9")
#     a9()
#
# b9()

# 匿名函数lambda表达式
# 语法:lambda 参数1,参数2,....:表达式
# 注意一下,接的是表达式,而不是代码块,必须要用关键字lambda

# 比如现在想通过函数求和
# 通过普通函数求和
def sum(a,b):
    return a+b
print(sum(3,5))

# 通过匿名函数求和
sum1=lambda a,b:a+b

print(sum1(7,8))

# 匿名函数和函数的区别
# 匿名函数不可以使用其他变量,只能对内部参数做运算,函数里可以使用函数外的参数

# 模块
# 为什么要使用模块?
# 随着项目功能和需求增多,代码量也会加大,把全部代码放在一个文件会显得冗余,因此需要使用模块分区管理

# 什么是python模块?
# 是一个pytho文件,以.py结尾

# 导入模块
# 一般导入的内容放在文件的最开始
# import
import time
time.time()

# from...import从某个模块中导入一个指定的部分
from time import sleep

# 跨目录调用模块
from time import sleep

# 全部导入
from wenjian1.demo6 import *

# import 搜索路径
# 当你导入一个模块,python解释器对模块位置有一个搜索顺序
# 1.当前目录
# 2.如果不在当前目录,python会搜索总的下的每个目录
# 3.如果都找不到,python会查看安装默认路径