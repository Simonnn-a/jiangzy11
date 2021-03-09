from selenium import webdriver
from selenium.webdriver.common.by import By
from vip.options import Options
from time import sleep


from vip.log import log#需要源码


"""设计webui的关键字驱动类对象：
   对常用的关键字进行二次封装，以便于后续的调用
"""

class webuikeys:
    #构造函数
    wd = webdriver.Chrome(r'd:\chromedriver.exe')

    def __init__(self,browser_type):
        self.wd = self.open_browser(browser_type)

    #创建浏览器对象:必须判断，不然其他人 不清楚
    # def open_browser(self, browser_type):
    #     if browser_type is 'Chrome':
    #         wd = webdriver.Chrome(r'd:\chromedriver.exe')
    #     elif browser_type is 'Firefox':
    #         wd = webdriver.firefox()
    #     else:
    #         wd = webdriver.Chrome()
    #     return wd
    #创建浏览器对象 2.0 通过反射机制实现
    def open_browser(browser_type):
        #添加异常处理机制
        try:
            if browser_type == 'Chrome':
                logger().get_logger().info('chrome浏览器正在启动中')
                wd =webdriver.Chrome(options=Options().options_conf())
            else:

         -       logger().get_logger().info('非chrome浏览器正在启动中')
                wd = getattr(webdriver, browser_type)()
        except Exception as e:
            logger().get_logger().info('出现异常，默认调用chrome浏览器，异常信息\n{0}'.format(e))
            wd = webdriver.Chrome()
        return wd





    #
    # #元素定位
    # def locator(self,loc_type,value):
    #     if loc_type is 'xpath':
    #         return self.wd.find_element_by_xpath(value)
    #     elif loc_type is 'id':
    #         return self.wd.find_element_by_id(value)
    #
    # #元素定位， 2.0 基于元组形式实现元素定位 ex：(By.ID,'kw')
    # #传入的By对象要视确定是对象，而非str类型
    # def locator(self,loc):
    #     demo = 'ID'
    #  #错误太多 不推荐

    #元素定位 3.0 基于字符串实现元素定位，调用python反射机制
    def locator(self,name,value):
        #反射机制中，有一个函数
        #upper()将字符串转为大写格式
        self.wd.find_element(getattr(By,name.upper()), value)
        #name = 'id' , value = 'kw'
        self.wd.find_element(By.ID, 'kw')

    #元素的输入操作
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    #元素的点击操作
    def click(self,name,value):
        self.locator(name,value).click()

    #浏览器关闭
    def quit(self):
        self.wd.quit()

    #访问指定URL
    def visit(self,url):
        self.wd.get(url)

    #强制等待
    def sleep(self,time):
        sleep(time)

    #隐式等待
    def wait(self,time):
        self.wd.implicitly_wait(time)

    #断言机制:获取文本信息进行校验
    def assert_text(self,functiob_name,value,expect):
        reality = self.locator(functiob_name, value).text
        try
            assert reality == expect
            logger().get_logger().info('断言成功 流程正确')
        except Exception as e:
            logger().get_logger().info('出现异常。异常信息：\n{0}'.format(e))








