#_*_ conding:utf-8 _*-
#@Time:2020/9/20 &{TIME}
# 12、如何创建一个空元组
tupa=()
print(tupa)
# 13、创建一个只包含元素1的元组，并打印出该变量的类型
tupb=(1,)
print(tupb,type(tupb))
# 14、元组中元素可以修改？如何更新元组中的元素？
# 不可以，通过拼接更新
# 15、对元组（1, 2, 3, 4, 5)做如下操作：
# 1）取倒数第二个元素
tupc=(1,2,3,4,5)
print(tupc[-2])
# 2）截取前三个元组元素
print(tupc[:3])
# 3）依次打印出元组中所有元素
for i in tupc:
    print(i)
# 16、把元组(1, 2, 3, 4, 5, 6)元素格式化成字符串
print(list(tupc))
# - ----------------------------------------------------可变数据类型
#
# 1、定义一个列表[1, 2, 3]，并将列表中的头尾两个元素对调。对调后为[3, 2, 1]
lista=[1,2,3]
lista.reverse()
print(lista)
def asd(listb):
    b=listb[0]
    listb[0]=listb[-1]
    listb[-1]=b
    return listb
listb=[1, 2, 3]
print(asd(listb))

# 2、定义一个列表，并将列表中的指定位置的两个元素对调。对调第一个和第三个元素,列表如下：[23, 65, 19, 90],对调后结果：[19, 65, 23, 90]
listc=[23, 65, 19, 90]
def aaa(listc,s1,s2):
    listc[s1],listc[s2]=listc[s2],listc[s1]
    return listc
listc=[23, 65, 19, 90]
s1=1
s2=3
print(aaa(listc,s1-1,s2-1))
# 3、对列表[10, 11, 12, 13, 14, 15],翻转，调整后为[15, 14, 13, 12, 11, 10]
listd=[10, 11, 12, 13, 14, 15]
listd.reverse()
print(listd)
# 4、判定6是否包含列表[1, 6, 3, 5, 3, 4]
liste=[1, 6, 3, 5, 3, 4]
if 6 in liste:
    print('yes')
else:
    print('no')
# 5、[1, 6, 3, 5, 3, 4],转换为元组
print(tuple(liste))
# 6、根据列表[1, 6, 3, 5, 3, 4],作为新字典的key, 对应key的初始值为0，并打印新字典对象
dicta={}
dicta=dicta.fromkeys(liste,'aaa')
print(dicta)
# 7、循环打印出字典,{'name': 'aming', 'age': 18, 'school': 'cema'},中的所有键和值，
dictb={'name': 'aming', 'age': 18, 'school': 'cema'}
for x,y in dictb.items():
    print(x,y)
# 8、{‘taobao’, 'jingdong', 'alibaba', 'baidu', 'taobao'}对元素去重复  （不做）

# 9、分别有两个集合,{1, 2, 1, 3, 4, 5, 6, 7}，{1, 2, 3, 8, 9, 7, 10}，求两个集合的差集、并集、交集（不做）

# 10、判断9题中两个集合如果存在相同元素，则打印重复，否则打印无重复
seta={1, 2, 1, 3, 4, 5, 6, 7}
setb={1, 2, 3, 8, 9, 7, 10}
a=seta&setb
print(a)
b=a.__len__()
print(b)
if b!=0:
    print('重复')
else:
    print('无重复')
# 11、list7 = [1, 2, 3, 4, 5],根据列表中的元素作为字典中的key, 及初始值为0，打印这个新的字典，不用fromkey方法实现
list7 = [1, 2, 3, 4, 5]
setc=set(list7)
print(setc,type(setc))
