#_*_ conding:utf-8 _*-
#@Time:2020/9/16 &{TIME}

# 1、用print函数打印多个值
a=1
b=2311
c=65533
print(a,b,c)
# 2、用print函数不换行打印
print('111',end='')
print('222')
# 3、导入模块的方式有哪些
import
from xxxx import xxxx
# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
Python中的数据类型包括：number(int,float,bool,complex)、string、tuple、list、dict、set
不可变类型:number、string、tuple
可变类型:list、dict、set
# 5、python3中可以支持哪些数值类型？
字符串，数字，列表，字典，元组，集合
# 6、判断变量类型有哪些方式，分别可以用哪些函数？
a1=12321
b1=type(a)
print(b1)
# 7、分别对49.698作如下打印
# 1）四舍五入，保留两位小数
from decimal import Decimal
a2=49.698
b2=Decimal(a2).quantize(Decimal('0.00'))
print(b2)
# 2）向上入取整
import math
a3=2.56
print(math.ceil(a3))
# 3）向下舍取整
print(math.floor(a3))
# 4）计算8除以5返回整型
print(8//5)
# 5）求4的2次幂
print(4**2)
# 6）返回一个（1, 100）随机整数
import random
print(random.randint(1,100))
# 8、依次对变量a, b, c赋值为1, 2, 3
print('a4={},b4={},c4={}'.format(1,2,3))
# 9、截取某字符串中从2索引位置到最后的字符子串
a5='serfadvcs'
print(a5[2:])
# 10、对字符串“testcode”做如下处理：
# 1）翻转字符串
a6='testcode'
print(a6[::-1])
# 2）首字母大写
print(a6.capitalize())
# 3）查找是否包含code子串，并返回索引值
print(a6.find('code',0,len(a6)))
# 4）判断字符串的长度
print(len(a6))
# 5）从头部截取4个长度字符串
print(a6[:4])
# 6）把code替换为123
a7=a6.replace('code','123')
print(a7)
# 7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理
b3='test code'
c3=b3.split(' ')
print(c3)
# 8）把['test', 'code']把list变量中的元素连接起来
a8=['test', 'code']
a9='-'.join(a8)
print(a9)
# 11、如何打印出字符串“test\ncode”
print(r'test\ncode')
# --------------------------下面先不做
#
# 12、如何创建一个空元组
#
# 13、创建一个只包含元素1的元组，并打印出该变量的类型
#
# 14、元组中元素可以修改？如何更新元组中的元素？
#
# 15、对元组（1, 2, 3, 4, 5)做如下操作：
#
# 1）取倒数第二个元素
#
# 2）截取前三个元组元素
#
# 3）依次打印出元组中所有元素
#
# 16、把元组(1, 2, 3, 4, 5, 6)
# 元素格式化成字符串




