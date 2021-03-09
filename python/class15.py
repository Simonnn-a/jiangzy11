#_*_ conding:utf-8 _*-
#@Time:2020/11/30 &{TIME}
'''
    web端的关键字驱动类：
        结构中属于逻辑代码层，主要的目的是作为一个工具类的角色，在需要用到这些工具时，通过这个类来实现
        大型超市——自家工具箱——动用工具
        Selenium——关键字——web自动化
        工具箱一般包含有需要的常规操作行为：
            输入、点击、启动、、、、、、
        单独的工具类的存在是没有意义的，一定需要关联到实际应用，才能够产生价值
'''

# 开始去超市购物
from time import sleep

from selenium import webdriver

'''
    getattr(class,name)()函数，从class对象中获取名称为name的成员属性
    如果要获取class对象的函数，则需要在末尾添加一个()
    getattr(webdriver,'Chrome') = webdriver.Chrome
    getattr(webdriver,'Chrome')() = webdriver.Chrome()
    如果传入的type_不是被允许的或错误的格式，那么browser函数会报错
'''


# 生成一个浏览器（webdriver对象）:反射机制
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


# 定义工具类
class WebKeys:
    # 定义driver
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.implicitly_wait(10)

    # 访问URL
    def open(self, url):
        self.driver.get(url)

    # 退出
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 文本断言校验
    def assert_text(self, name, value, fact_text):
        assert self.locator(name, value).text == fact_text, '断言失败'

    # 强制等待
    def wait(self, time_):
        sleep(time_)


# 拿出工具箱
from class07.key_word_web.keyword_web import WebKeys

# 实例化类对象
wk = WebKeys('Chrome')
wk.open('http://39.98.138.157/shopxo/')
wk.click('link text', '登录')
wk.input('name', 'accounts', 'xuzhu666')
wk.input('name', 'pwd', '123456')
wk.click('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
wk.wait(3)
wk.quit()
