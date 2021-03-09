from selenium import webdriver
from selenium.webdriver.support.select import Select
wd = webdriver.Chrome(r'd:\chromedriver.exe') #r代表转义符
#上传文件时也可以通过sendkeys传入文件路径+名称+后缀，直接上传，但该方法只适用input后缀
#单选复选框都通过click来实现，例如下拉列表框的元素为div，使用click来实现
Select.select_by_index()#通过下表 index的值
Select.select_by_value()#通过下表的value的值
Select.select_by_visible_text()#通过下表的text的值
#页面句柄的切换
 #页面跳转分两种类型：1.在当前页面直接跳转 2.启动新的标签页进行跳转
 #不同的标签页通过不同的句柄来实现

# 新网页的切换：
# for handle in wd.window_handles:
#     wd.switch_to.window(handle)#先切换到该窗口
#     if 'Bing' in wd.title：#如果是必应时这个窗口的标题，则推出循环
#         break
title = wd.title#获取句柄
handles = wd.window_handles
wd.switch_to.window(handle[1])

wd.close()#关闭当前页面
#通过下面语句改变数字来切换句柄，可不同页面切换 只适用在一个案例里
handles = wd.window_handles首先获取句柄
wd.switch_to.window(handle[1])
wd.switch_to.window(handle[0])

#iframe代表一个独特的窗体
#切换iframe，默认可以通过id和name进行切换，如果没有就用定位元素切换
wd.switch_to.frame()#括号内填id或name
wd.find_element_by_xpath()

wd.switch_to.frame(wd.find_element_by_xpath('//iframe[定位的元素]'))
#结束后需要切换出弹窗的iframe，
wd.switch_to.default_content()#从iframe中切换回原来的界面
wd.switch_to.window(handles[0])

#三类等待
time.sleep
隐式等待
对当前整个webdriver的生命周期都生效直到driver.quit之后
wd.implicitly_wait(10) #当定位元素定位不到时会开始等待，但无法对元素进行更为精准的操作并且较为浪费资源
#隐式等待会等页面上所有的操作都加载完成后才进行下一步的操作。
显式等待：唯一的一种专门针对特定的条件而设置的等待，针对特定的元素去执行
from selenium.webdriver.support.ui import WebDriverWait #显式等待模块调用
WebDriverWait(wd=wd,timeout=5,poll_frequency=0.5).until(lambda el:wd.find_element_by_xpath(''),message='元素定位失败')
#poll_frequency=0.5   查看频率，默认0.5s一次
until是直到什么条件为ture的时候，表示正确  unyil_not是知道什么时候为false的时候，表示正确
当显式等待执行时可以用于判断页面元素是存在的/不存在的
但只能针对单一的元素生效，每次使用时需要再次调用函数
显式等待会返回一个元素 需要return，可以基于显式等待进行页面内容展示的判断
lambda函数类似于做一个一次性函数的声明

页面滚动：
上下滚动
js = 'doucument.scrollingElement.scrollTop=500'
wd.excute_script(js)
左右滚动操作：x控制左右，y控制上下
js = 'document.scrollingElement.scrollTo(x,y)'
滚动到元素存在的位置
el = wd.find_element_by_xpath('')指定元素位置
js = 'arguments[0].scrollIntoView()'
wd.execute_script(js,el)

#弹窗处理
web_alert = wd.switch_to.alert
#确认
web_alert.accept()
#取消
web_alert.dismiss()
#输入文本，promt弹窗
web_alert.send_keys('123456')
#获取prompt弹窗文本内容
web_alert.text


#创建chromeOption对象
options = wd.ChromeOptions()
#窗体最大化
options.add_argument('start-maximized')
#无头模式：启动浏览器进程，但是不会显示出来
options.add_argument('--headless')
#去掉警告
options.add_argument('disable-infobars') 老版本的chrome浏览器去掉警告的形式
去掉开发者警告
options.add_experimental_option('useAutomationExtension',False)
去掉黄条
options.add_experimental_option('excludeSwitches', ['enable-automation'])

#启动隐身模式 无痕模式
options.add_argument('incognito')




创建chrom对象
wd = webdriver.Chrome(options=options)

#判断登录是否成功
wait.until(lambda el: wd.find_element_by_xpath('退出元素'))
handeles = wd.window_handles(handles[1])












































