#_*_ conding:utf-8 _*-
#@Time:2020/9/22 &{TIME}
# 顺序结构
# 选择结构
# 循环结构

# 条件判断
# if语句
# if 判断条件(表达式):
#     代码块

# if else语句
# if 判断条件(表达式):
#     代码块
# else:

# if elif else语句
# if 判断条件(表达式):
#     代码块
# elif 判断条件(表达式):
#     代码块
# else:

# if else语句
# 成绩为80分以上就是优秀,否则就是一般
# chengji=int(input("请输入成绩:"))
# if chengji>=80:
#     print("优秀")
# else:
#     print("一般")

# 成绩80分以上评级优秀,60/79成绩一般,60分以下不及格
# chengji=int(input("请输入成绩:"))
# if chengji>=80:
#     print("优秀")
# elif chengji>=60:
#     print("一般")
# else:
#     print("不及格")
# elif相当于是else if的缩写,完全可以有多个else if

# if的嵌套
# if 判断条件(表达式):
#     if 判断条件(表达式):
#         代码块
#     elif 判断条件(表达式):
#         代码块
#     else:
# elif 判断条件(表达式):
#     代码块
# else:
# 判断成绩的等级(优秀/中等/一般/不及格)
# chengji=int(input("请输入成绩:"))
# if chengji>=60:
#     print("及格")
#     if chengji>90:
#         print("优秀")
#     elif chengji>75:
#         print("中等")
#     else:
#         print("一般")
# else:
#     print("不及格")

# 循环语句
# while
# for
# do while 是没有这个的

# while 循环

# while 条件表达式(循环变量的判断):
#     代码块(又被称为循环体)
# 条件为真执行循环体,条件为假跳出循环
# n=10
# while n>0:
#     n=n-1
#     print(n)
#
# print("结束")
# 实现1+2+3+4...+100?
# i=0
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
#     print(i,sum)
# print(sum)

# while循环与else语句同时使用
# i=0
# sum=0
# while i<=100:
#     sum=sum+i
#     i=i+1
#     print(i,sum)
# else:
#     print(sum)

# str1="http://www.baidu.com/"
# i=0
# while i<len(str1):
#     print(str1[i],end="")
#     i=i+1

# for循环
# 经常用来遍历字符串/列表/元祖/字典/集合等序列类型,逐个获取序列中的各个元素
# for 迭代变量 in 字符串/列表/元祖/字典/集合:
#     代码块
# list1=['zhangsan','lisi','wangwu','zhaoliu']
# for x in list1:
#     print(x)

# str1="http://www.baidu.com/"
# for x1 in str1:
#     print(x1,end="")

# str1="http://www.baidu.com/"
# for x1 in str1:
#     print(x1,end="")
# else:
#     print("哈哈")

# 计算一下1+2+3+4...+10的值
# range(x)函数提供了一个整数序列x生成从0开始到小于x的值
# sum=0
# for i in range(11):
#     sum=sum+i
# print(sum)

# 什么时候用while什么时候用for
# 一般需要遍历某个序列的时候用for
# 一般能用for的时候一定可以用while,反过来就不一定
# 当知道循环次数的时候用for,不知道循环次数的时候用while

# 循环嵌套
# i=0
# while i<10:
#     for j in range(10):
#         print("i=",i,"j=",j)
#     i=i+1

# 打印一个图案
# *
# **
# ***
# ****
# *****

# for x in range(1,6):
#     for y in range(0,x):
#         print("*",end="")
#     print()
for y in range(1,6):
    for x in range(0,y):
        print("*",end="")
    print()



# break:跳出整个循环
# continue:跳出本次循环
# pass:空语句,占位语句
# 除去H字母不打印
# str="nihaodahan"
# for i in str:
#     if i=='h':
#         pass
#     print(i)
