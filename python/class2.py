#_*_ conding:utf-8 _*-
#@Time:2020/9/20 &{TIME}
# # 元组
# # 不可变数据类型，number、string
# # tuple 元组数据类型
# # （）通过它标识，元素是可以任意类型的，元素之间是通过，隔开的
# # 1、创建一个元组
# tup1=(1,2,3)
# print(tup1)
# # 2、创建空元组
# tup2=()
# print(tup2,type(tup2))
# # 3、创建只有一个元素的元组，最后需要加一个，去消除数学歧义
# tup3=(1,)
# print(type(tup3),tup3)
# # 4、可以创建任何数据类型的元组
# tup4=(1,2,3,"dahan",[1,2,3,4])
# print(tup4)
# # 5、访问元组种的元素，可以通过切片的方法去访问，根据索引来确定
# print(tup4[1])
# # 6、去头去尾访问
# print(tup4[1:-1])
# # 7、访问元组当中部分的元素
# print(tup4[1:4])
# # 8、更新元素
# # tup4[3]="xiaohan" 不能通过它更新，元组是不可变数据类型
# tup6=("xiaohan",)
# tup5=tup4[0:3]+tup6+tup4[4:]#tup4[-1:]
# print(tup5)
# # 9、复制元素
# print(tup4*3)
# # 10、元组还可以做判断
# if "dahan" in tup4:
#     print("cunzai")
# else:
#     print("bucunzai")
# # 删除元组的元素
# # 不可以删除元组里面的元素，只能通过拼接的方式去更新
# # del tup4[0]
# # print(tup4)
# # 但是可以删除整个元组对象，
# # del tup4
# # print(tup4)
# # 12、元组常用的其他函数
# print(len(tup4))
# # 把元组转换成列表
# print(list(tup4))

# 可变数据类型
# 列表
# 什么是列表:是一种有序集合，它可以随时添加和删除其中的元素
# 定义：通过[]表示，元素可以是任意类型，元素之间用逗号隔开
# 1、创建一个列表
list1=[1,2,3,4,5]
print(list1)
# 2、访问列表种元素的值，
# 2.1访问第一个元素的值
print(list1[0])
# 2.2访问最后一个元素的值
print(list1[-1])
# 2.3访问部分的值
list2=list1[1:-1]
print(list2)
# 2.4访问的超出了范围的值
# print(list1[9])
# 索引越界

# 3、修改list当中元素的值，
list1[0]=0
print(list1)

# 4、增加元素
# 我想要向list1里面去增加一个元素
# 4.1.append方式增加，在末尾追加元素
list1.append(6)
print(list1)
# 4.2.insert在指定的位置添加元素
list1.insert(1,"zhangsan")#位置通过索引确定
print(list1)
# 4.3、增加多个元素，.extend()方法
zengjiayuansu=[11,12,13,14]
list1.extend(zengjiayuansu)
print(list1)
# 4.4、通过append的方式增加多个元素
# append增加后是一个列表，一个列表就是一个元素
list1.append(zengjiayuansu)
print(list1)

# 5、删除元素
list4=[20,21,22,23,24,25]
# 5.1.pop的方式去删除,默认删除最后一个元素
list4.pop()
print(list4)
# 5.2指定删除，可以根据元素的索引指定删除
list4.pop(1)
print(list4)
# 5.3根据元素的值去删除
list4.remove(24)
print(list4)
# 5.4del方式删除
del list4[-1]
print(list4)
# 5.5如果列表里面有重复的元素怎么删除，只想删除其中的一个怎么删除
list5=[6,6,7,8,9,1,2,3]
# 首先可以找到某个值在列表中出现的次数
print(list5.count(6))
# print(list5.index(要查找的值,从第一个值索引0开始,到最后一个值)
print(list5.index(6,0,len(list5)))
# 在进行删除

# 6、list可以支持运算 + * in/not in
list6=[1,2,3,4,5]
list7=[6,7,8,9]
# 6.1+运算
list8=list6+list7
print(list8)
# 6.2*运算
print(list7*2)
# 6.3判断
if 1 in list6:
    print("cunzai")
else:
    print("bucunzai")

# 7、其他操作
# .sort列表默认升序排序
list7.sort()
print(list7)
# 降序排序
list7.sort(reverse=True)
print(list7)
# list翻转
list7.reverse()
print(list7)

# 字典
# d={key1:value1,key2:value2,key3:value3.....}
# key是键，value是值，key1:value1是键值对，键与值用：隔开，键值对之间用逗号隔开
# key必须是唯一的，并且数据不可变
# 1、如何创建一个字典
dict1={"xingming":"zhangsan","mima":"123456"}
print(dict1)
# 2、创建空字典
dict2={}
print(dict2)
# 3、访问字典里面的元素,通过键去访问
print(dict1["xingming"],dict1["mima"])
# 4、修改字典
dict1["mima"]="abcdefg"
print(dict1)
# 5、增加一个键值对
dict1["dizhi"]="changsha"
print(dict1)
# 6、删除键值对
del dict1["dizhi"]
print(dict1)
# 6.1通过函数删除
dict1.pop("xingming")
print(dict1)
# 6.2删除最后一个键值对
dict1.popitem()
print(dict1)
# 6.3删除整个字典
# del dict2
# print(dict2)

# 7字典常见的内置函数
# 返回某个数据类型的长度
print(len(dict1))

# 8类型转换
# 想把字典转换成字符串类型
zhuanhuan=str(dict1)
print(zhuanhuan,type(zhuanhuan))

# 9依次获取字典中key和value的值
dict11={"xingming":"zhangsan","mima":"123456"}
for x,y in dict11.items():
    print(x,y)

# 10把以下内容作为字典里面的键
list100=["xingming","mima","dizhi","xingbie"]
dict3={}
dict3=dict3.fromkeys(list100,"none")
print(dict3)

# 11字典的成员判断,通过键去判断
if "xingming" in dict3:
    print("存在")
else:
    print("bucunzai")

# 12多个元素进行更新,如何更新字典
dict4={"xingming":"zhangsan","mima":"123456"}
dict5={"xingming":"zhangsan","dizhi":"changsha","xingbie":"nv"}
# 把dict5更新到dict4中,会按照不同的key去更新
dict4.update(dict5)
print(dict4)
# 如果是同一个key,但是值不同,更新以后会怎么杨?
# 把dict5里面的zhangsan改成zhangsan1就可以看到结果,自己运行

# 集合数据类型,集合中的数据是无序的
# 集合也是通过{}来表示,几个中的元素可以是任意各种形态
# 元素可以是任意类型,每个元素之间可以用逗号隔开
# 1创建一个举几个,集合是自动去重的
set1={1,2,3,4,5,2,3,5,"dahan"}
print(set1,type(set1))
# 2.创建一个空集合
set2={}
print(set2,type(set2))
# 上面创建的不是集合而是字典,要用下面这个
set21=set()
print(set21,type(set21))
# 3.创建集合的另外一种方式
set3=set([1,2,3,4,3,2,5])
print(set3,type(set3))
# 4.访问集合
# print(set1[0])
# 集合是无序的,所以不能访问

# 5.集合支持那些运算,集合只能求合集并集交集
# a&b交集:公共的部分
# a|b并集:全部的元素去重
# a-b差集:返回a中所有的元素,除去b中有的元素
# a^b非交集:返回的是a,b中没有重复的元素
set4={1,2,3,4,5,6,7}
set5={5,6,7,8,9,"dahan"}
a=set4&set5
b=set4|set5
c=set4-set5
d=set4^set5
print("a",a)
print("b",b)
print("c",c)
print("d",d)

# 6.set常见的内置函数
# 集合运算函数

# 此方法类似上面讲的交集
print(set4.intersection(set5))

# 相当于上面的并集
print(set4.union(set5))

# 相当于上面讲的差集
print(set4.difference(set5))

# 相当于上面讲的非交集
print(set4.symmetric_difference(set5))

# 7.元素操作的相关函数
# 7.1增加元素,
set4.add(20)
print(set4)

# 7.2删除元素.pop随机删除元素,没有办法指定删除某个位置元素,
set4.pop()
print(set4)

# 7.3remove/discard也是删除,区别是discard删除没有的元素不会报错
set4.remove(20)
print(set4)
set4.discard(100)
print(set4)

# 8常用的判断函数
# 判断返回有没有重复元素集合
# 判断有没有重复的元素。没有重复的元素返回True，有重复返回False
print(set4.isdisjoint(set5))

# 判断某个集合是不是另一个集合的子集
# 是返回T，不是返回F
set6={1,2,3,4,5,6}
set7={1,2,3,"dahan"}
print(set6.issubset(set7))

# 判断某个集合是不是另一个集合的父级
# 是返回T，不是返回F
print(set6.issuperset(set7))

# 9、更新
set6.update(set7)
print(set6)