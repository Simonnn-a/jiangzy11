#_*_ conding:utf-8 _*-
#@Time:2020/11/22 &{TIME}
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
    断言机制：
        断言的使用不仅仅只是driver.title,断言一定是选择有指定意义的内容来进行断言。
        断言的对象可以是元素，可以是属性，可以是文本，可以是任何东西。只要是特定的即可。
        一般常用的断言就是通过text来进行，除此之外，如果需要流程继续执行，可以考虑用显式等待。
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://39.98.138.157/shopxo/')
# driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
# driver.find_element_by_name('accounts').send_keys('666666')
# driver.find_element_by_name('pwd').send_keys('111111')
# driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()

# text = driver.find_element_by_xpath(
#     '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text
#
# print(text)
# # 预期结果
# assert_text = '6666661'
# # 断言机制：预期结果与实际结果对比
# assert assert_text == driver.find_element_by_xpath(
#     '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text, '断言失败'

'''
断言的核心原理：
    if assert_text == driver.find_element_by_xpath(
    '/html/body/div[6]/div/div[1]/div[1]/em/span/em[2]').text:
        pass
    else:
        return AssertionError
'''

'''
    JS执行器：
        Document对象的应用：Document对象是JS中的一个模块
            1. 用于获取元素信息或者修改元素属性，以便于在实际自动化时可以更为便捷地执行操作
            2. 因为selenium本身是基于js来实现的。但是在实际web中，有一些特定的情况是通过selenium很难实现，就需要通过js去注入脚本
            3. JS执行器配合document对象，一般是用于自动化中的疑难杂症来进行处理的。
            4. 如果你需要通过js执行器来操作获取元素或者获取信息，进行赋值，就需要添加return
'''
# 通过Selenium获取元素属性
# el = driver.find_element_by_xpath('//*[@id="ai-topsearch"]')
# value = el.get_attribute('class')
# print(value)
# 通过Document对象来修改元素属性
js = "document.getElementById('ai-topsearch').setAttribute('value','asd')"
# 执行js语句函数：js执行器
driver.execute_script(js)
# 如何有效地运行js语句
el = driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/a[1]')
# 占位符的应用
js = "arguments[0].innerHTML"
# 灵活版js执行器操作：通过传递元素参数，来快速实现元素的识别与操作
driver.execute_script(js, el)
# 滚动条操作，一般都是在特定需要操作滚动条时应用即可。
# document.scrollingElement.scrollTop表示上下滚动，0-2000区间
# window.scrollTo(x,y) 左右滚动
# el = driver.find_element_by_xpath('/html/body/footer/div[1]/ul[1]/li[4]/div/p[5]/a')
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js, el)

'''
    网页弹窗：
        传统的弹窗交互形式：
            1. 确定弹窗 alert
            2. 确定、取消弹窗 confirm
            3. 输入文本，确定、取消弹窗 prompt文本窗
        这种弹窗的形式基本已经没有了。因为交互太老旧
        移动端叫做toast
        特殊弹窗（通知，不属于弹窗）：这一类型的内容，需要通过修改chrome属性来实现操作
            1. 记住密码和更新密码
            2. 禁用启用权限设置
            3. 弹窗允许与否
'''
from selenium import webdriver

driver = webdriver.Chrome()
# 切换到弹窗本体
web_alert = driver.switch_to.alert
# 确认弹窗
web_alert.accept()
# 取消弹窗
web_alert.dismiss()
# 输入文本
web_alert.send_keys('')
# 获取文本
text = web_alert.text
