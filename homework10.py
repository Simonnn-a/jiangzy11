#_*_ conding:utf-8 _*-
#@Time:2020/11/16 &{TIME}
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\chromedriver.exe')
wd.implicitly_wait(10)
wd.maximize_window()
"""登陆商城"""
wd.get('http://39.98.138.157/shopxo/index.php')
"""注册"""
wd.find_element_by_xpath('//a[text()="注册" and @class="am-btn-primary btn am-fr"]').click()
wd.find_element_by_xpath('//input[@placeholder="请使用字母、数字、下划线 2~18 个字符" ]').send_keys('sdfsdghl')#输入用户名
wd.find_element_by_xpath('//*[@class="am-form form-validation-username" ]/div[2]/div/input').send_keys('sdfsdghl')#输入密码
wd.find_element_by_xpath('//*[@class="am-form form-validation-username" ] /div[3]/label').click()#点击勾选协议按钮
wd.find_element_by_xpath('//*[@class="am-form form-validation-username" ] /div[4]/button').click()#点击注册
"""关闭浏览器"""
wd.quit()


