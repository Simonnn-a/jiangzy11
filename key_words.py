#_*_ conding:utf-8 _*-
#@Time:2020/11/30 &{TIME}
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
    def __init__(self,type_):
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
    def locater(self,name,value):
        return self.wd.find_element(name,value)
    # 元素定位(多个元素)：
    def locaters(self, name, value):
        return self.wd.find_elements(name, value)
    #输入：
    def input(self,name,value,txt):
        self.locater(name,value).send_keys(txt)
    #点击：
    def click(self,name,value):
        self.locater(name,value).click()
    #强制等待：
    def wait(self,time_):
        sleep(time_)
    #显式等待：
    def assert_wait(self,time_,name,value):
        WebDriverWait(self.wd, time_, 0.5).until(
            lambda el: self.locater(name,value), message='查找元素失败')
    #断言：
    def assert_txt(self,element_right,name,value):
        assert_text1 = element_right
        assert assert_text1 == self.locater(name,value).text, '失败'
    #鼠标悬停
    def stop_element(self,name,value):
        el = self.locater(name,value)
        action = ActionChains(self.wd)
        action.move_to_element(el).perform()
    # #日志器
    # def loG(self,name,log_level,path):
    #     # 创建日志器
    #     logger = logging.getLogger(name)
    #     # 设置日志级别
    #     logger.setLevel(log_level)
    #     # 创建一个格式器
    #     formator = logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s')
    #     # 创建一个处理器  输出文件中
    #     fh = logging.FileHandler(path, encoding='utf-8')
    #     # 创建一个处理器 输出到控制台
    #     sh = logging.StreamHandler()
    #     # 把文本处理器加载到日志器中
    #     logger.addHandler(fh)
    #     # 把控制台加载到日志器
    #     logger.addHandler(sh)
    #     # 把格式器放入控制台
    #     sh.setFormatter(formator)
    #     # 把格式器放入到文本控制器
    #     fh.setFormatter(formator)
    #     return logger
    # #切换到新的句柄
    # def sw_win(self,value):
    #     handles = self.wd.window_handles
    #     self.wd.switch_to.window(handles[value])
    # 切换到新的句柄,不关闭标签页
    def sw_win_noclose(self):
        handles = self.wd.window_handles
        self.wd.switch_to.window(handles[1])

    # 切换到新的句柄，关必标签页
    def sw_win_close(self):
        handles = self.wd.window_handles
        self.wd.close()
        self.wd.switch_to.window(handles[1])

    # 切换旧窗体
    def sw_win_old(self):
        handles = self.wd.window_handles
        self.wd.switch_to.window(handles[0])

# if __name__ == '__main__':
#     wd=WebKeys('Chrome')