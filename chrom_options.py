#_*_ conding:utf-8 _*-
#@Time:2020/11/23 &{TIME}
from selenium import webdriver
class Options:
    def options_conf(self):
        # 创建options对象:配置浏览器的设置
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化提示：不去掉一般不会有任何影响，但是在特殊情况下，黄条可能会遮挡到页面的内容显示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 窗体最大化
        options.add_argument('start-maximized')
        # 添加配置去掉密码管理弹窗
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        # 无头模式：Headless模式，无界面运行，会尽可能的降低GPU的使用率，整体机器的资源使用率会下降
        # options.add_argument('--headless')
        return options
