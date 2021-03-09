# _*_ conding:utf-8 _*-
# @Time:2020/12/17 &{TIME}
import unittest
from ddt import ddt, file_data
from selenium import webdriver
from options import Options
from pom.page_object.denglu import loginpage
from pom.page_object.gouwuche import gouwu
@ddt
class liucheng(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wd=webdriver.Chrome(options=Options().options_conf())
        cls.dl=loginpage(cls.wd)
        cls.gou=gouwu(cls.wd)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.wd.quit()
    @file_data('../data/user.yaml')
    def test_01_login(self,**kwargs):
        u"""pom封装界面登录"""
        self.dl.login(kwargs['user'],kwargs['pwd'])
    def test_02_add(self):
        u"""pom封装添加购物车"""
        self.gou.add()
# if '__name__'=='__main__':
#     unittest.main()