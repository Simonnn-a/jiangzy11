# _*_ conding:utf-8 _*-
# @Time:2020/12/15 &{TIME}
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

"""
设定webdrive
"""
def browser(type_):
    try:
        wd = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        wd = webdriver.Chrome()
    return wd
"""
定义工具
"""
class WebKeys:
    #定义构造函数：
    def __init__(self,type_) -> object:
        self.wd=browser(type_)
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()
    #打开网址：
    def open(self,url):
        self.wd.get(url)
    #退出网址：
    def quit(self):
        self.wd.quit()
    #元素定位(单个元素)：
    def locater(self,**kwargs):
        return self.wd.find_element(kwargs['name'],kwargs['value'])
    # 元素定位(多个元素)：
    def locaters(self, **kwargs):
        return self.wd.find_elements(kwargs['name'],kwargs['value'])
    #输入：
    def input(self,**kwargs):
        el=self.locater(**kwargs)
        el.clear()
        el.send_keys(kwargs['txt'])
    #点击：
    def click(self,**kwargs):
        self.locater(**kwargs).click()
    #强制等待：
    def wait(self,time_):
        sleep(time_)
    #显式等待：
    def assert_wait(self,**kwargs):
        try:
            el=WebDriverWait(self.wd, kwargs['time_'], 0.5).until(
                lambda el: self.locater(**kwargs), message='查找元素失败')
            return el
        except:
            return False

    #断言：
    # def assert_txt(self,**kwargs):
    #     assert_text1 = kwargs['txt']
    #     assert assert_text1 == self.locater(**kwargs).text, '失败'
    def assert_txt(self,**kwargs):
        try:
            assert self.locater(**kwargs).text ==kwargs['expect']
            return True
        except:
            return False
    #获取元素属性断言
    def assert_att(self,**kwargs):
        att = self.locater(**kwargs).get_attribute(kwargs['txt'])
        try:
            assert att == str[kwargs['expect']]
            return True
        except:
            return False
    #鼠标悬停
    def stop_element(self,name,value):
        el = self.locater(name,value)
        action = ActionChains(self.wd)
        action.move_to_element(el).perform()
    #切换到新的句柄,不关闭标签页
    def sw_win_noclose(self,**kwargs):
        handles = self.wd.window_handles
        self.wd.switch_to.window(handles[1])
    #切换到新的句柄，关必标签页
    def sw_win_close(self,**kwargs):
        handles = self.wd.window_handles
        self.wd.close()
        self.wd.switch_to.window(handles[1])
    #切换旧窗体
    def sw_win_old(self,**kwargs):
        handles = self.wd.window_handles
        self.wd.switch_to.window(handles[0])
