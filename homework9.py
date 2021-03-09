#_*_ conding:utf-8 _*-
#@Time:2020/11/15 &{TIME}
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\chromedriver.exe')
wd.implicitly_wait(10)
"""登录网易云"""
wd.get('https://music.163.com/')
handles = wd.window_handles
print(handles)
wd.maximize_window()
wd.find_element_by_xpath('//*[@data-action="login"]').click()#点击登录
wd.find_element_by_xpath('//*[@data-action="switch"]').click()#点击其他登录方式
wd.find_element_by_xpath('//*[@id="j-official-terms"]').click()#点击同意协定
wd.find_element_by_xpath('//*[@class="u-alt"]/ul/li[2]/a').click()#点击qq登录
"""打开了一个新的页面 切换页面句柄"""
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '帐号安全登录' in wd.title:
        break
print(handle)
"""iframe切换  坑！！！！！！！！！！！"""
wd.switch_to.frame('ptlogin_iframe')
wd.find_element_by_xpath('//*[@id="nick_1067263257"]').click()#点击qq号


wd.switch_to.frame('ptlogin_iframe')  #切换iframe
wd.find_element_by_xpath('//a[@id="switcher_plogin"]').click() #点击账号密码登录
wd.find_element_by_xpath('//input[@id="u"]').send_keys('你的qq号')  #输入你的qq号
wd.find_element_by_xpath('//input[@id="p"]').send_keys('你的qq密码')   #输入你的qq密码
wd.find_element_by_xpath('//input[@id="login_button"]').click()     #点击登录
wd.switch_to.default_content()

