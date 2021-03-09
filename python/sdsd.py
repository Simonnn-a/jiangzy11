# _*_ conding:utf-8 _*-
# @Time:2020/12/6 &{TIME}
from selenium import webdriver
import time
wd = webdriver.Chrome(r'd:\chromedriver.exe')
wd.implicitly_wait(10)
"""登录网易云"""
wd.get('https://music.163.com/')
handles = wd.window_handles
print(handles)
el=wd.find_elements_by_xpath('//a[@title="冬日限定丨静谧与欢乐"]')
print(el)
