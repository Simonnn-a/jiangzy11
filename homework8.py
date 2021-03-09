#_*_ conding:utf-8 _*-
#@Time:2020/11/12 &{TIME}
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

wd = WebDriver(executable_path=r'd:\chromedriver.exe')
u"""打开百度网址"""
wd.execute('get',{'url': 'http://www.baidu.com'})
u"""定位到搜索框"""
sou=wd.execute('findElement', {'using': By.XPATH,'value': '//input[@id="kw"]'})['value']
u"""输入虚竹"""
sou._execute('sendKeysToElement',{'text': '虚竹', 'value': ''})
u"""定位到百度一下按钮并点击"""
sou1=wd.execute('findElement', {'using': By.XPATH,'value': '//input[@id="su"]'})['value']
sou1._execute('clickElement')
