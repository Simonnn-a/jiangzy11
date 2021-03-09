#_*_ conding:utf-8 _*-
#@Time:2020/10/21 &{TIME}
# 类与对象
# 定义类
# 类属性和类方法
# 创建空类
# 属性初始化__init__
# 构造函数
# 类的实例化
# 类变量和实例变量和局部变量
# 类的内置属性
# python的是实例方法/静态方法和类方法的使用




# 封装/继承/多态
# 上节课遗留内容
# 内置方法
# 私有方法和私有属性


# 内置方法
# __init__(self,....)：构造方法，在生成对象时调用，可以用来进行一些初始化操作，不需要显示去调用，系统会默认去执行。
# __del__(self)：析构方法，在释放对象时调用，支持重载，可以在里面进行一些释放资源的操作，不需要显示调用。
# __str__(self,…)：自定义实例输出方法，写好该方法后，替换实例默认的输出操作。
# __getattribute__(...)：获取实例属性的值，可直接结合对象使用。


# class Student():
#     '''这是学习创建的第一个类的注释'''
#     #定义类属性(类变量)
#     name="youname"
#     color="yellow"
#     __weight=48
#
#     #构造方法(构造函数)
#     def __init__(self,name,city,weight):
#         self.name=name
#         self.city=city
#         self.__weight=weight
#         print("调用构造方法:","我是%s,来自%s" % (name, city))
#
#     def __del__(self):
#         print("释放对象会调用__del__方法函数")
#
#     def __mimi(self):
#         print("这是一个私有方法")
#
# # 实例化一个对象
# # zhangsan=Student("张三","长沙")
# # print(zhangsan)
# #
# # print(zhangsan.color)
# # print(zhangsan.name)
#
#
# # 私有方法和私有属性
# # __开头去定义私有方法,私有方法不能再类的外部使用,只能在内部使用
# # __不能再累的外部访问,不能直接访问,使用时候实用self.类的私有属性表示
#
# # 初始化一个对象
# zhangsan=Student("张三","长沙",100)
# # 可不可以调用私有属性,不可以调用私有属性
# # zhangsan.__
#
# # 私有属性如何进行外部访问?(不建议)
# # 对象._类名+私有属性名
# # print(zhangsan._Student__weight)
#
# # print(zhangsan.listen("好运来"))
#
# # 私有方法不可以系通过对象去调用
# # zhangsan.__
# zhangsan._Student__mimi()

# 私有方法的实际应用

class Test:
    def __send_msg(self):
        print("正在发送信息")

    def send_msg(self,new_money):
        if new_money>100:
            self.__send_msg()
        else:
            print("抱歉余额不足")

zhangsan=Test()
zhangsan.send_msg(20)

# 封装/继承/多态
# name="张三"
# city="长沙"
# age=18
# aihao="打篮球"
# print("大家好,很高兴和大家成为同学")
# print("我叫%s,我的家乡是%s,今年%d岁了"%(name,city,age))
#
#
# name="李四"
# city="上海"
# age=17
# print("大家好,很高兴和大家成为同学")
# print("我叫%s,我的家乡是%s,今年%d岁了"%(name,city,age))
#
#
# name="李四"
# city="上海"
# age=17
# print("大家好,很高兴和大家成为同学")
# print("今年%d岁了,我叫%s,我的家乡是%s,"%(name,city,age))
#
# name="李四"
# city="上海"
# age=17
# print("大家好,很高兴和大家成为同学")
# print("我叫%s,我的家乡是%s,今年%d岁了"%(name,city,age))

# class Student():
#     def __init__(self,name,city,age):
#         self.name=name
#         self.city=city
#         self.age=age
#         print("大家好,很高兴和大家成为同学")
#         print("今年%d岁了,我叫%s,我的家乡是%s"%(age,name,city))
#
# Student("张三","长沙",18)
# Student("李四","长沙",18)
# Student("王五","长沙",18)
#
# # 需求：小明爱跑步
# # 	1.小明体重75.0公斤
# # 	2.每次跑步会减肥0.5公斤
# # 	3.每次吃东西体重会增加1公斤
# # 	4.小美的体重是45.0公斤
#
#
# # 人类:
# # 属性:姓名/体重
# # 功能:跑步/吃东西
# # 具体的对象:小明/小美
#
# class People:
#     def __init__(self,tz,name):
#         self.tz=tz
#         self.name=name
#
#     def running(self):
#         self.tz-=0.5
#         print(f"因为跑步,所以我瘦了0.5公斤,现在的体重是{self.tz}")
#
#     def eatting(self):
#         self.tz+=1
#         print(f"因为嘴馋,所以增加了1公斤,现在的体重是{self.tz}")
#
# # 创建实例
# xiaoming=People(75.5,"小明")
# xiaoming.running()
# xiaoming.eatting()
# xiaoming=People(45,"小美")
# xiaoming.running()
# xiaoming.eatting()

# # (2)继承
# # 子类拥有和父类以及父类中封装的所有属性和方法
#
# class People:#父类,也可以理解为基类
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def speak(self):
#         print("会说话")
#
#     def sleep(self):
#         print("会睡觉")
#
# # 继承分为单继承和多继承
#
#
# # 单继承
# # class 类名(父类名):
# #     类体
#
# class Student(People):
#
#     def speak(self):
#         People.speak(self)
#         print("子类里面的会说话")
#
#
# # zhangsan=Student("张三",18)
# # zhangsan.speak()
# # zhangsan.sleep()
#
# # 就近原则:先找自己,再找爸爸,再找爸爸的爸爸....
#
# # 继承有什么作用
# # 1.子类可以重写父类的方法
# # 2.扩展父类的方法
# # 我想同时调用子类和父类的同一个方法怎么办?
# zhangsan=Student("张三",18)
# zhangsan.speak()

# (2)多继承
# class 类名(父类名,父类名1,....):
#     类体
class People:#父类,也可以理解为基类

    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    def speak(self):
        print("会说话")

    def sleep(self):
        print("会睡觉")

class pythonstudent(People):
    def speak(self):
        People.speak(self)
        print("pythonstudent会说话")

class Javastudent(People):
    def speak(self):
        People.speak(self)
        print("Javastudent的会说话")


class Student(pythonstudent,Javastudent):
    def __init__(self,name):
        self.name=name
    def speak(self):
        People.speak(self)
        Javastudent.speak(self)
        print("Student的会说话")


lisi=Student("李四")
lisi.speak()

# # 多态:不同的子类调用相同的方法它会执行不同的代码(多态)
# class wx:
#     def pay(self):
#         print("采用微信支付")
# class zfb:
#     def pay(self):
#         print("采用支付宝支付")
# class yl:
#     def pay(self):
#         print("采用银行卡方式支付")
#
# def start_pay(object):
#     object.pay()
#
# wx1=wx()
# start_pay(wx1)
#
# zfb1=zfb()
# start_pay(zfb1)
#
# yl1=yl()
# start_pay(yl1)