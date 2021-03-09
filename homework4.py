#_*_ conding:utf-8 _*-
#@Time:2020/9/23 &{TIME}
# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
def bidaxiao(a,b):
     if a>b:
         return a
     elif a<b:
         return b
     else:
         return a
jieuo1=bidaxiao(10,20)
print(jieuo1)
# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
def huoqu(list):
    list1=[]
    for i in range(len(list)):
        if i%2 ==1:
            list1.append(list[i])
    return list1
chuanru=[34,23,52,352,352,3523,5]
jieguo2=huoqu(chuanru)
print(jieguo2)

# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     				返回2：[34,23,52]
def guolv (shuru):
    shuchu=[]
    a=len(shuru)
    if a >5:
        shuchu.append(shuru[:5])
        print(shuchu)
    else:
        print(shuru)
chuanru1=guolv([34,23,52,352,666,3523,5])
chuanru2=guolv([34,23,52])
# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
def jianchakong(shuru1):
    zhuangtai=True
    for i in shuru1:
        if ' ' in shuru1:
            zhuangtai=True
        else:
            zhuangtai=False
    return zhuangtai
chuanru3=jianchakong("hello world")
print(chuanru3)
# 5.写函数，接收n个数字，求这些数字的和
def qiuhe(*shuru2):
    shuchu2=0
    for i in range(len(shuru2)):
        shuchu2+=shuru2[i]
    return shuchu2
chuanru4=qiuhe(1,2,3,4,5,6,7,8,9)
print(chuanru4)
# 6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
# 例如：
# 传入：10,*,20
# 返回：200
def jisuan(a,met,b):
    if met=='+':
        shuchu=a+b
    elif met=='-':
        shuchu=a-b
    elif met=='*':
        shuchu=a*b
    else:
        shuchu=a/b
    return shuchu
chuanru5=jisuan(10,'*',20)
print(chuanru5)

# 7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
# 系统界面如下：
# -----------------------欢迎进入T666班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
# (0)输入0后效果如下：
# 	0
# 	["郭易","汤碗珍"..]
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：张三
# 	["郭易","汤碗珍",'张三'..]
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：张三
# 	["郭易","汤碗珍"..]
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：张三
# 	请输入需要修改后的姓名：李四
# 	["郭易","汤碗珍",'李四'..]
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
# 	请输入查询人的姓名：张三
# 	郭易在座位号(3<下标>)的位置。
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用T666的学生管理系统，下次再见。
mingdan=list(["郭易","汤碗珍"])
def jiemian():
    print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
    print('请选择系统功能：')
    print('0:显示所有学员信息')
    print('1:添加一个学员信息')
    print('2:删除一个学员信息')
    print('3:修改一个学员信息')
    print('4:查询一个学员信息')
def xueshengmingdan():
    print(mingdan)
def addstu():
    mingdan.append(input('请输入增加人的姓名：'))
    print(mingdan)
def delstu():
    deln=input('请输入删除人的姓名：')
    if deln in mingdan:
        mingdan.remove(deln)
        print(mingdan)
    else:
        print('T666班没有这个学3 员')
def updatastu():
    stu=input('请输入需要修改人的姓名：')
    ustu=input('请输入需要修改后的姓名：')
    if stu in mingdan:
        mingdan[mingdan.index(stu)]=ustu
        print(mingdan)
    else:
        print('T666班没有这个学员')
def chaxunstu():
    sel=input('请输入查询人的姓名：')
    if sel in mingdan:
        print(sel,'在座位号'+str(mingdan.index(sel))+'的位置')
    else:
        print('T666班没有这个学员')
def startup(n,mingdan):
    if n=='0':
        xueshengmingdan()
    elif n=='1':
        addstu()
    elif n=='2':
        delstu()
    elif n=='3':
        updatastu()
    elif n=='4':
        chaxunstu()
    elif n=='exit':
        print('欢迎使用T666的学生管理系统，下次再见。')
    else:
        print('错误')
        startup(input(n1),mingdan)
jiemian()
for n1 in range(0,6):
    if n1 != 5:
        n1=input()
        shuru=startup(n1,mingdan)
    elif n1=='5':
        print('错误')
    else:

        break





