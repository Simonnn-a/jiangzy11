#_*_ conding:utf-8 _*-
#@Time:2020/11/22 &{TIME}
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

# wd = webdriver.Chrome(r'd:\chromedriver.exe')
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.maximize_window()
"""登陆商城"""
wd.get('http://39.98.138.157/shopxo/index.php')
el=wd.find_elements_by_xpath('//a[text()="登录"]')
el[2].click()
wd.find_element_by_xpath('//input[@data-validation-message="请填写登录账号"]').send_keys('sdfsdghl')#输入帐号
wd.find_element_by_xpath('//input[@data-validation-message="密码格式 6~18 个字符之间"]').send_keys('sdfsdghl')#输入密码
wd.find_element_by_xpath('//button[text()="登录"]').click()#点击登录
"""断言是否登陆成功"""
assert_text='sdfsdghl'#预期结果
assert assert_text==wd.find_element_by_xpath('//em[text()="sdfsdghl"]').text,'登陆失败'  #如果与预期结果不同，返回登陆失败
"""搜索商品"""
wd.find_element_by_xpath('//input[@id="search-input"]').send_keys('iphone')#查找iphone6
wd.find_element_by_xpath('//input[@id="ai-topsearch"]').click()#点击搜索
"""点击商品iphone6"""
wd.find_element_by_xpath('//img[@src="http://39.98.138.157/shopxo/public/static/upload/images/goods/2019/01/14/1547451274847894.jpg"]').click()#点击iphone6
"""打开新页面，切换句柄"""
handles=wd.window_handles
wd.switch_to.window(handles[1])
"""选择套餐"""
wd.find_element_by_xpath('//li[@data-value="套餐一"]').click()#选择套餐一
time.sleep(2)
wd.find_element_by_xpath('//li[@data-value="银色"]').click()#选择银色
time.sleep(2)
wd.find_element_by_xpath('//li[@data-value="128G"]').click()#选择128G
time.sleep(2)
wd.find_element_by_xpath('//button[text()="加入购物车"]').click()#加入购物车
"""添加显式等待"""
WebDriverWait(wd, 2, 0.5).until(
    lambda el:wd.find_element_by_xpath('//*[@id="common-prompt"]'),message='添加购物车失败')
"""进入购物车查看是否真的添加成功"""
el1=wd.find_element_by_xpath('//span[text()="购物车"]').click()#点击购物车
assert_text1='苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G'
assert assert_text1==wd.find_element_by_xpath('//a[text()="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"]').text,'添加购物车失败'
"""关必浏览器，释放内存"""
wd.quit()