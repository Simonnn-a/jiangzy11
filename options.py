from selenium import webdriver
class Options:
    def options_conf(self):
        # wd = webdriver.Chrome()
        # 创建chromeOption对象
        options = webdriver.ChromeOptions()
        # 窗体最大化
        options.add_argument('start-maximized')
        # 无头模式：启动浏览器进程，但是不会显示出来
        #options.add_argument('--headless')
        # 去掉警告
        # options.add_argument('disable-infobars')
        #老版本的chrome浏览器去掉警告的形式
        #去掉开发者警告
        # options.add_experimental_option('useAutomationExtension', False)
        #去掉黄条
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 启动隐身模式 无痕模式
        # options.add_argument('incognito')
        return options
# if __name__ == '__main__':
#
#     wd=webdriver.Chrome(options=Options().options_conf)

