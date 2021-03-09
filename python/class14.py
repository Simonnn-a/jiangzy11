#_*_ conding:utf-8 _*-
#@Time:2020/11/23 &{TIME}
from time import sleep

from selenium import webdriver

'''
配置ChromeOptions：一般作为一个专门的配置类进行存放
特殊场景下的浏览器配置是需要自行去查找资料的。但是查找的时候要记得看代码：
    新版本：driver = webdriver.Chrome(options=options)
    老版本：driver = webdriver.Chrome(chrome_options=options)
    因为老版本的options配置，配置参数是chrome_options，而新版本的参数是options
常用的浏览器配置项：
    1. 去掉黄条警告
    2. 窗体最大化
    3. 读取本地缓存
    4. 无头模式
    5. 禁用密码管理窗体
'''


class Options:
    def options_conf(self):
        # 创建options对象:配置浏览器的设置
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化提示：不去掉一般不会有任何影响，但是在特殊情况下，黄条可能会遮挡到页面的内容显示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 老版本的去掉提示
        # options.add_argument('disable-infobars')
        # 窗体最大化
        options.add_argument('start-maximized')
        # 加载本地缓存，让浏览器变成一个有缓存的模式
        '''
            1. 通过指令查找本地的浏览器缓存，chrome://version
            2. 通过传入本地缓存，来实现缓存的获取：参数 --user-data-dir=
            3. 在调用本地缓存时，要先关闭所有正在应用的浏览器窗体
            4. 因为需要加载本地缓存，所以在启动浏览器之后，运行脚本的第一条指令，速度会非常缓慢，
                如果要提速，就手动输入随便一个url进行访问，就可以提速了。
            5. 一般不推荐使用，如果你非要绕过登录来实现后续的操作行为，则再添加
            6. 最廉价的验证码机制处理手段，仅限登录部分
        '''
        # options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')
        # 添加配置去掉密码管理弹窗
        prefs = {}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        # 无头模式：Headless模式，无界面运行，会尽可能的降低GPU的使用率，整体机器的资源使用率会下降
        options.add_argument('--headless')
        # 隐身模式：没啥用，就是好玩而已
        # options.add_argument('incognito')
        # 指定窗口大小：待验证
        # options.add_argument('-windows-size=720,1080')

        return options


# if __name__ == '__main__':
#     # 生成浏览器配置
#     options = Options().options_conf()
#     # 配置webdriver
#     driver = webdriver.Chrome(options=options)
#     print('1')
#     driver.implicitly_wait(10)
#     print('2')
#     # driver.maximize_window()
#     # driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
#     # print(driver.title)
#     # print('3')
#     # driver.find_element('name', 'accounts').send_keys('sdfsdghl')
#     # print('4')
#     # driver.find_element('name', 'pwd').send_keys('sdfsdghl')
#     # print('5')
#     # driver.find_element('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
#     # print('6')
#     # sleep(3)
#     # print(driver.title)
#     driver.get('http://www.baidu.com')



'''
    补课： 元素悬停
        from selenium.webdriver import ActionChains
        通过ActionChains模块来实现
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

from class06.chrome_options import Options

# driver = webdriver.Chrome(options=Options().options_conf())
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
# 悬停操作：在执行过程中鼠标不能动
el = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
action = ActionChains(driver)
action.move_to_element(el).perform()
# driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()


'''
    1. 从注册到用户信息的修改
    2. 从登陆到商品添加购物车
    PS: 在定位元素过程中，如果出现一闪即逝的元素需要定位，可以先启动chrome开发者工具——Source
        然后运行浏览器流程，需要抓取元素时，通过F8让页面暂停
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#from class06.chrome_options import Options

driver = webdriver.Chrome(options=Options().options_conf())
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/')
# 实现注册操作
# driver.find_element_by_link_text('注册').click()
# driver.find_element_by_name('accounts').send_keys('xuzhu666')
# driver.find_element_by_name('pwd').send_keys('123456')
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
# WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'), message='登陆失败')

# 实现登录操作
driver.find_element_by_link_text('登录').click()
driver.find_element_by_name('accounts').send_keys('xuzhu666')
driver.find_element_by_name('pwd').send_keys('123456')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_link_text('退出'), message='登陆失败')

# 个人信息修改：文件上传时，需要有一个小的上传时间，通过强制等待，让元素可以正常被操作
driver.find_element_by_link_text('个人中心').click()
driver.find_element_by_link_text('修改头像').click()
driver.find_element_by_name('file').send_keys(r'D:\头像\1.jpg')
sleep(2)
driver.find_element_by_xpath('//*[@id="user-avatar-popup"]/div/div[2]/form/button').click()
# 截图：需要先创建路径，再进行截图
WebDriverWait(driver, 5, 0.5).until(lambda el: driver.find_element_by_xpath('//*[@id="common-prompt"]/p'),
                                    message='登陆失败')
driver.save_screenshot('./img/test02.png')
sleep(3)
driver.quit()
