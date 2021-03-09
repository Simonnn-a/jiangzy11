# -*- coding:utf-8 -*-
# 1、任意的输入10个数字，按从大到小排序
aaa=list(input('输入10个数字：'))
aaa.sort(reverse=True)
print(aaa)
# 2、"在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，通过键盘输入小男孩回答的鲜花的束数，数量不一样小女生的反应也不一样。如果鲜花数大于等于9999，打印："小女生直接晕了过去",如果在1000(包含)-9999(不包含)，打印："明天就结婚",如果在100(包含)-1000(不包含)，打印："拉拉手意思意思，有空再约！",否则：打印："你是个好人"
flo=int(input('这花多少束：'))
if flo>9999:
    print('小女生直接晕了过去')
elif 1000<=flo<9999:
    print('明天就结婚')
elif 100<=flo<1000:
    print('拉拉手意思意思，有空再约！')
else:
    print('你是个好人')
# 3、输入三角形的三条边长，判断三角形的类型。根据实际情况分别打印：不能构成三角形，一般三角形，等腰三角形，等边三角形，只要能构成三角形，则还需要计算出：周长。
a=int(input('输入边长a=:'))
b=int(input('输入边长b=:'))
c=int(input('输入边长c=:'))
d=a+b+c
if a+b>c or a+c>b or b+c>a:
    if a==b or b==c or c==a:
        print('三角形为等腰三角形')
        print('三角形的周长为:',d)
    elif a==b==c:
        print('三角形为等边三角形')
        print('三角形的周长为:',d)
    else:
        print('三角形为一般三角形')
        print('三角形的周长为:', d)
else:
    print('不能构成三角形')
# 4、如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
if x<y:
    if y<z:
        print(x<y<z)
    elif x<z:
        print(x<z<y)
    else:
        print(z<x<y)
elif y<z:
    print(y<z<x)
elif x<z:
    print(y<x<z)
else:
    print(z<y<x)
# 5、判断输入的用户名为admin及密码为admin则打印登录成功，否则打印用户名或密码错误，登录失败
username=str(input('请输入用户名：'))
pwd=str(input("请输入密码："))
if username=='admin':
    if pwd=='admin':
        print('登陆成功')
else:
    print('用户名或密码错误，登录失败')

# # 6、判断输入的数是奇数还是偶数
num=int(input('请输入：'))
if num%2==0:
    print(num,'为偶数')
else:
    print(num,'为奇数')
# # 7、用户输入的年份是否为闰年
num1=int(input('请输入：'))
if num1%400 ==0 or num1%4==0 or num1%100!=0:
    print(num1,'年为闰年')
else:
    print(num1,'年为平年')
#
# # 8、输入两个整型变量，分别使用if结构两个中的最小值
a11=int(input("请输入a11："))
a22=int(input('请输入a22：'))
if a11>a22:
    print(a22)
elif a11<a22:
    print(a11)
else:
    print("a11=a22")
# 9、打印如下结果：
# 1*5=5
# 2*10=20
# 3*15=45
# ...
# 10*50=500
i=1
j=5
for i in range(1,11):
    print(i,'*',i*j,'=',i*i*j)
#
# # 10、本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
i=0
j=10000
for i in range(1,6):
    i+=1
    j=j+j*0.003
    print(j)
# # 11、计算1900年1月1日到今天(如：2019年12月20日)相距多少天。
ping=0
run=0
for year in range(1990,2021):
    if year%400 ==0 or year%4==0 or year%100!=0:
        ping+=1
    else:
        run+=1
tian=ping*336+run*365-31+(20-1)
print(tian)

# 12、打印如下图案：
# *
# **
# ***
# ****
# *****
for y in range(1,6):
    for x in range(0,y):
        print("*",end="")
    print()
# 13、打印如下图案：
# *
# ***
# *****
# *******
# *********
for y in range(1,6):
    for x in range(0,2*y-1):
        print("*",end="")
    print()
# 14、打印如下图案：
# #####*
# ####***
# ###*****
# ##*******
# #*********
for y in range(1,6):
    for x in range(0,6-y):
        print('#',end='')
    for z in range(0,2*y-1):
        print('*',end='')
    print()

# 15、打印如下图案：
#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *
for y in range(1,6):
    for x in range(0,6-y):
        print(' ',end='')
    for z in range(0,2*y-1):
        print('*',end='')
    print()
for i in range(1,5):
    for j in range(0,i+1):
        print(' ',end='')
    for k in range(0,2*(5-i)-1):
        print('*',end='')
    print()


# 16、打印99乘法表
x=0
y=0
for x in range(1,10):
    for y in range(1,x+1):
        print(x,'*',y,'=',x*y,end='\t')
    print(' ')