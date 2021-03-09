#_*_ conding:utf-8 _*-
#@Time:2020/10/18 &{TIME}
# 定义类
# class 类名(object):
#     类体
#     多个>=0类属性
#     多个>=0类方法

class Student():
    '''这是给类定义的说明,相当于类的注释'''
    # 定义类属性(类变量)
    # name="yourname"
    # color="yellow"

    # 构造方法(构造函数)
    def __init__(self,name,city):
        # 有了init方法,就不能传入空参数了实例变量(实例属性)
        self.name=name
        self.city=city
        print("调用构造方法","我是%s,来自%s"%(name,city))

#     # 定义类方法
#     def listen(self,music):
#         # 定义一个实例变量(实例属性)
#         self.musicname1="演员"
#         print("学生会听")
#
# # 创建一个空类
# class none1:
#     pass
#
# class egg:
#     def cout(self,money):
#         sale=0.8*money
#         print("优惠后的价格为",sale)



# # 属性的初始化
#
# # 类的实例化
# # 类名(参数)
zhangsan=Student("张三","长沙")
# # lisi=Student("李四","北京")
#
# # 总结:面向对象的关键要素
# # 类class:类是描述具有相同属性和方法的对象的集合,它定义了该集合中每个对象所共有的属性和方法
# # 数据成员(属性):类的不同属性数据,所有的变量称为属性.
# # 对象:对象是类的实例(实例化对象)
# # 方法:类中定义的函数,实现相关的功能
#
# # 定义类和方法有什么用
# # print("我是zhangsan,来自长沙",)
# # print("我是lisi,来自北京",)
# # print("我是王五,来自上海",)
# # print("我是zhangsan,来自长沙",)
# # print("我是zhangsan,来自长沙",)
# # 如果开班来了200个学生,所有学生都改名了,要改代码信息要修改
# # 封装
# # 找到介绍的共同点
#
#
# # python中的类变量和实例变量有什么不同?
# # 1.类属性或类变量
# # 特点:所有类的实例化对象都同时共享类变量,作为公共资源存在
# # 类方法的调用方式有两种,既可以使用类型直接调用,也可以使用类的实例化对象调用
# # 使用类名直接调用
# # print(Student.name)
# # print(Student.color)
# # # 可以修改类变量的值
# # Student.name="nidename"
# # Student.color="pink"
# # print(Student.name)
# # print(Student.color)
# #
# # # 也可用类对象来调用楼所属类中的类变量
# # zhangsan=Student("张三","pink")
# # print(zhangsan.name)
# # print(zhangsan.color)
#
# # 2.实例变量或实例属性
# # 实例变量指的是在任意类方法内部,以"self.变量名"的方式定义的变量,
# # 实例变量只能通过对象吗访问,无法通过类名访问
# # 实例化对象
# # wangwu=Student("王五","北京")
# # print(wangwu.name)
# # print(wangwu.city)
#
# # 不可以调用,这个会报错
# # print(wangwu.musicname1)
# # 那应该怎么办?
# # 只用调用了listen(),才会有.musicname1的实例变量
# # wangwu.listen(1)
# # print(wangwu.musicname1)
#
# # 3.局部变量,不同"变量名=变量值"
# yaegg=egg()
# yaegg.cout(100)
#
# # 4.内置类属性
# # 内置属性:通过类来进行调用
# # 类名.__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# # 类名.__doc__ :类的文档字符串
# # 类名.__name__: 类名
# # 类名.__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# # 类名.__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
# print(Student.__doc__)
# print(Student.__name__)
# print(Student.__module__)
# print(Student.__bases__)
# print(Student.__dict__)
#
# # 类方法
# # python中的实例方法/静态方法/类方法
# # 1.@classmethod修饰的方法是类方法
# # 2.@staticmethod修饰的方法为静态方法
# # 3.不用任何修饰的方法称为实例方法
#
# # # 1.类实例方法(构造方法也属于实例方法,)
# # class Student:
# #     def __init__(self):
# #         self.name="yourname"
# #         self.color="yellow"
# #
# #     def say(self):
# #         print("说点什么呢")
# #
# #
# #
# # # 实例方法通常会用类对象直接调用
# # # zhangsan=Student()
# # # zhangsan.say()
# # # 类名调用实例方法,需要手动给self进行参数传递
# # zhangsan=Student()
# # # Student.say()
# # Student.say(zhangsan)
#
# # 2.类方法
# class Student:
#     def __init__(self):
#         self.name="yourname"
#         self.color="yellow"
#
#     @classmethod
#     def say(cls):
#         print("说点什么呢?",cls)
#
#     @staticmethod
#     def read(bookname,num):
#         print(bookname,num)
#
# # # 使用类名直接调用类方法
# # Student.say()
# # # 使用类对象调用类方法
# # zhangsan=Student()
# # zhangsan.say()
#
# # 3.静态方法(之前学过的函数)
# # 和函数的区别
#
# # 静态方法的调用,既可以使用类名,也可以使用类对象
# # 使用类名直接调用静态方法
# Student.read("安徒生",18)
# # 使用类对象调用静态方法
# dahan=Student()
# dahan.read("灰姑娘",99)