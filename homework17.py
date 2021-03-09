# _*_ conding:utf-8 _*-
# @Time:2020/12/11 &{TIME}
import unittest
from key_words import WebKeys
from python.test_log import DemoLog

class all_shopping(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wd=WebKeys('Chrome')
        wd=cls.wd
        log=DemoLog().txt_log()
        log.info('现在开始自动化测试')
    @classmethod
    def tearDownClass(cls) -> None:
        cls.wd.quit()

    def test_a(self):
        u"""登录购物网站页面"""
        log = DemoLog().txt_log()
        log.info("现在开始登陆购物网站界面")
        self.wd.open('http://39.98.138.157/shopxo/')
        el = self.wd.locaters('xpath', '//a[text()="登录"]')
        el[2].click()
        self.wd.input('xpath', '//input[@data-validation-message="请填写登录账号"]', 'sdfsdghl')
        self.wd.input('xpath', '//input[@data-validation-message="密码格式 6~18 个字符之间"]', 'sdfsdghl')
        self.wd.click('xpath', '//button[text()="登录"]')
        self.wd.assert_txt('sdfsdghl', 'xpath', '//em[text()="sdfsdghl"]')

    def test_b(self):
        u"""搜索商品"""
        log = DemoLog().txt_log()
        log.info("现在开始搜索商品")

        self.wd.input('xpath', '//input[@id="search-input"]', 'iphone')
        self.wd.click('xpath', '//input[@id="ai-topsearch"]')
        self.wd.click('xpath','//img[@src="http://39.98.138.157/shopxo/public/static/upload/images/goods/2019/01/14/1547451274847894.jpg"]')

    def test_c(self):
        u"""切换句柄并选择套餐"""
        log = DemoLog().txt_log()
        log.info("现在开始切换句柄并选择套餐")

        self.wd.sw_win_close()
        self.wd.click('xpath', '//li[@data-value="套餐一"]')
        self.wd.wait(2)
        self.wd.click('xpath', '//li[@data-value="银色"]')
        self.wd.wait(2)
        self.wd.click('xpath', '//li[@data-value="128G"]')
        self.wd.wait(2)
        self.wd.click('xpath', '//button[text()="加入购物车"]')

    def test_d(self):
        u"""断言查看购物车"""
        log = DemoLog().txt_log()
        log.info("现在开始断言查看购物车是否添加成功")

        self.wd.assert_wait(2, 'xpath', '//*[@id="common-prompt"]')
        self.wd.click('xpath', '//span[text()="购物车"]')
        self.wd.assert_txt('苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G', 'xpath','//a[text()="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"]')
if __name__ == '__main__':
    unittest.main()