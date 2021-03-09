#_*_ conding:utf-8 _*-
#@Time:2020/11/18 &{TIME}
# 强制等待
from time import sleep
from selenium import webdriver
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
'''
    隐式等待：偷偷摸摸的等待，是由WebDriver提供的一种等待模式，是以类似于全局变量的形式存在，对当下
        整个driver的生命周期都有效果，说白了就是对driver的一个等待设置
        当元素未找到时，达到最大等待时间后，程序继续运行
        好处：只需要设置一次，全局皆可生效
        缺陷：比较浪费资源，没有办法对精准度的元素进行定位，会影响到实际的运行效率
'''
# 在整个driver周期中，默认最大等待10秒时间
# driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('虚竹')
driver.find_element_by_id('su').click()
'''
    强制等待：无所谓任何的情况，只要运行到强制等待这一行，就一定要等待指定的时间
    实现的形式是通过：time.sleep(秒)
        好处：简单上手，直接粗暴，一般都是在新手阶段和学习阶段以及特定的场景下来使用，平时不推荐使用
        劣势：因为太粗暴了，所以对于实际的执行会带来很费时间的影响
            经常写等待，代码中有非常多的sleep，显得冗余度会非常高
'''
sleep(2)
'''
    显式等待：是唯一的一种专门针对特定的元素（条件）而设置的等待，基本上都是应用在对指定元素来执行的
    until函数，用于判断，当条件为真的时候，返回结果。等待为真时，返回被等待的元素对象，为假时抛出超时异常
    untl_not函数，与until函数相反
'''
# element = WebDriverWait(driver, 10, 0.5).until(
#     lambda el: driver.find_element_by_xpath('//*[@id="1"]/h3/a1'), message='查找元素失败')
element = WebDriverWait(driver, 5, 0.5).until_not(
    lambda el: driver.find_element_by_xpath('//*[@id="1"]/h3/a1'), message='查找元素失败')
# driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
print(element)
# driver.quit()

'''
    三类等待的场景应用：
        1. 强制等待：需要的时候调用即可
        2. 隐式等待：创建driver的时候调用
        3. 显式等待：除去关键性元素以外，还可以将显示等待的调用方式作为断言的机制
            until:用于在关键性元素进行定位时，调用
                在为了确保整个流程可以正常执行的目的的情况下，可以选择显式等待来进行元素的查找和定位
            until_not:用于在校验流程时，调用
    在系统中，弹窗分为两种：
        1、 需要进行操作之后，才可以消失的弹窗
        2、 一定时间后，自动消失
    当显示与隐示同时存在的情况下：
        1. 如果出现元素找不到，则爆出超时异常
        2. 在等待机制下，默认会遵循时间更长的等待方式

    显示等待机制：作为断言的时候，可以通过显示等待来判定元素的是否显示，从而判定到流程是否执行成功
        如果成功，会返回一个元素对象，如果失败会返回一个异常，基于显示等待返回的结果，可以判定本次流程是否成功

'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 隐式等待添加，以便于后续整个driver中，都可以尽量减少强制等待调用
driver.implicitly_wait(5)

driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
# 登录
# 在关键性的元素上，进行显示等待。
WebDriverWait(driver, 2, 0.5).until(
    lambda el: driver.find_element_by_name('accounts1'), message='登录失败')
driver.find_element_by_name('accounts').send_keys('666666')
driver.find_element_by_name('pwd').send_keys('111111')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

sleep(3)
driver.quit()