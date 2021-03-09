#_*_ conding:utf-8 _*-
#@Time:2020/10/21 &{TIME}
# 一、定义名为MyTime的类，其中应有三个实例变量
# 时hour
# 分minute
# 秒second
# 1）为了给对象初始化赋值，编写构造方法，对时分秒附初始值
class MyTime:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        neirong='调用构造方法,{}时,{}分,{}秒'.format(hour,minute,second)
        print(neirong)
shijian=MyTime('3','2','1')
# 2）为了保证数据的安全性，这三个成员变量应声明为私有、
class MyTime1:
    def __safetime(self):
        print('请输入时间')
    def safetime(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
        neirong1 = '调用构造方法,{}时,{}分,{}秒'.format(hour, minute, second)
        print(neirong1)
shijian2=MyTime1()
shijian2.safetime('3','2','1')
# 3）对三个属性分别定义封装get和set方法，定义一个main方法，创建一个MyTime类的对象并调用这六个方法。
class MyTime:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def gettime_hour(self):
        return self.__hour
    def gettime_minute(self):
        return self.__minute
    def gettime_second(self):
        return self.__second
    def settime_hour(self,hour):
        self.__hour = hour
    def settime_minute(self,minute):
        self.__minute = minute
    def settime_second(self,second):
        self.__second = second


if __name__ == '__main__':
    a=MyTime(1,2,3);
    print(a._MyTime__hour,a._MyTime__minute,a._MyTime__second);
    a.settime_hour(10)
    print(a.gettime_hour())
    a.settime_minute(11)
    print(a.gettime_minute())
    a.settime_second(20)
    print(a.gettime_second())

# 二、为 "无名的粉"写一个类WuMingFen，有三个属性 面码: String theMa 粉的分量(两) int quantity 是否带汤 boolean likeSoup
# 要求：
# 1）写一个构造方法
# 分别给三个属性赋值。构造出一个WuMingFen类的对象(酸辣面码、2两、带汤)，
# 2）写一个普通方法check()
# 打印对象的三个属性。通过对象调用此方法。
class WuMingFen:
    def __init__(self,lei,liang,soup):
        self.theMa=lei
        self.quantity=liang
        self.likeSoup=soup
    def check(self):
        print(self.theMa,self.likeSoup,self.quantity)
fen=WuMingFen('酸辣面码','2两','带汤')
fen.check()

# 三、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表
# 新房子没有任何的家具
# 2）家具有名字和占地面积，其中
# 床：占4平米
# 衣柜：占2平面
# 餐桌：占1.5平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出: 户型，总面积，剩余面积，家具名称列表
class house:
    def __init__(self,huxing,mianji):
        self.huxing=huxing
        self.mianji=mianji
        self.shengyumianji=mianji
        self.jiajutable=[]
    def jiajumianji(self,jiajuming,zhandi):
        self.jiajuming=jiajuming
        self.zhandi=zhandi
        return f'{self.jiajuming}占地面积为{self.zhandi}平米'
    def tianjia(self,jiaju):
        if jiaju.zhandi>self.shengyumianji:
            c='{}不能添加'.format(jiaju)
            print(c)
        else:
            self.jiajutable.append(jiaju)
            self.shengyumianji-=jiaju.zhandi
    def dayin(self):
        return f'户型{self.huxing}，总面积：{self.mianji},剩余面积:{self.shengyumianji},家具列表:{self.jiajutable}'
chuang=house('一室一厅',200)
chuang.jiajumianji('chuang',4)
print(chuang)
yigui=house('一室一厅',200)
yigui.jiajumianji('yigui',2)
print(yigui)
canzhuo=house('一室一厅',200)
canzhuo.jiajumianji('canzhuo',1.5)
print(canzhuo)
shuru=house('一室一厅',200)
shuru.tianjia(chuang)
shuru.tianjia(canzhuo)
shuru.tianjia(yigui)
print(shuru)




# 四、需求：
# 1）士兵瑞恩有一把AK47
# 2）士兵可以开火(士兵开火扣动的是扳机)
# 3）枪能够发射子弹(把子弹发射出去)
# 4）枪能够装填子弹 - -增加子弹的数量
class gun:
    def __init__(self,gun_name):
        self.gun_name=gun_name
        self.zidanshu=0
    def fashe(self):
        if self.zidanshu==0:
            print(f'{self.gun_name}no bullet')
            return
        self.zidanshu-=1
        print(f'{self.gun_name}shoot---')
    def zhuangzidan(self,b):
        self.zidanshu+=b
class shibin:
    def __init__(self,name,gun_name):
        self.name=name
        self.gun_name=gun_name
    def kahuo(self):
        if self.gun_name==[]:
            print('no gun')
            return
        print(f'{self.name}no gun')
        self.gun_name.zhuangzidan(10)
        self.gun_name.fashe()
qiang=gun('ak47')
ruien=shibin('ruien',qiang)
ruien.kahuo()
# 五、编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
# 实现思路及关键代码：
# 1)定义乐器类Instrument，包括makeSound()
# 方法，此方法中乐器声音："乐器发出美妙的声音！"
# 2)定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin
# 二胡Erhu声音："二胡拉响人生"
# 钢琴Piano声音："钢琴美妙无比"
# 小提琴Violin声音："小提琴来啦"
# 3）用main类，多态的方式对不同乐器进行切换
class Instrument:
    def makeSound(self):
        print('乐器发出美妙的声音！')
class Erhu(Instrument):
    def makeSound(self):
        print('二胡拉响人生')
class Piano(Instrument):
    def makeSound(self):
        print('钢琴美妙无比')
class Violin(Instrument):
    def makeSound(self):
        print('小提琴来啦')

def yueshou(yanzou):
    yanzou.makeSound()
if __name__ == '__main__':
    Erhu=Erhu()
    Piano=Piano()
    Violin=Violin()
    yueshou(Erhu)
    yueshou(Piano)
    yueshou(Violin)
