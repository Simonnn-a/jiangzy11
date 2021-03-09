# _*_ conding:utf-8 _*-
# @Time:2020/12/15 &{TIME}
import unittest
from ddt import ddt, file_data
from vip.key_yaml import WebKeys
from vip.python.test_log import DemoLog
@ddt
class ya_shopping(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wd=WebKeys('Chrome')
    @classmethod
    def tearDownClass(cls) -> None:
        cls.wd.quit()
    @file_data('data.yaml')
    def test_a(self,**kwargs):
        u"""登录购物网站页面"""
        log = DemoLog().txt_log()
        log.info("现在开始登陆购物网站界面")
        self.wd.open(kwargs['url'])
        self.wd.input(**kwargs['username'])
        self.wd.input(**kwargs['password'])
        self.wd.click(**kwargs['button'])
        self.wd.wait(kwargs['sleep'])
        self.wd.assert_txt(**kwargs['assert'])
    @file_data('data2.yaml')
    def test_b(self,**kwargs):
        u"""搜索商品"""
        log = DemoLog().txt_log()
        log.info("现在开始搜索商品")
        self.wd.input(**kwargs['iph'])
        self.wd.click(**kwargs['button_sousuo'])
        self.wd.click(**kwargs['button_picture'])

    @file_data('data3.yaml')
    def test_c(self,**kwargs):
        u"""切换句柄并选择套餐"""
        log = DemoLog().txt_log()
        log.info("现在开始切换句柄并选择套餐")

        self.wd.sw_win_close()
        self.wd.click(**kwargs['button_service1'])
        self.wd.wait(kwargs['sleep'])
        self.wd.click(**kwargs['button_service2'])
        self.wd.wait(kwargs['sleep'])
        self.wd.click(**kwargs['button_service3'])
        self.wd.wait(kwargs['sleep'])
        self.wd.click(**kwargs['button_addto'])
    @file_data('data4.yaml')
    def test_d(self,**kwargs):
        u"""断言查看购物车"""
        log = DemoLog().txt_log()
        log.info("现在开始断言查看购物车是否添加成功")

        self.wd.assert_wait(**kwargs['assert_wai'])
        self.wd.click(**kwargs['button_check_addto'])
        self.wd.assert_txt(**kwargs['assert'])






