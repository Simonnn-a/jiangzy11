# _*_ conding:utf-8 _*-
# @Time:2021/1/12 &{TIME}
import unittest
from vip.homework43.config import read_ini
from vip.api_keys import jiekouKey
from ddt import ddt, file_data
@ddt
class test_all(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak=jiekouKey()
        # cls.url = read_ini.redini('../config/server.ini', 'TEST_SERVER', 'url')
        cls.url = read_ini.redini('vip/homework43/config/server.ini', 'TEST_SERVER', 'url')#生成测试报告时的路径
        cls.token = None
        cls.userid = None
        cls.openid = None
        cls.cartid = None
    @file_data('../data/danapi_data/addcart.yaml')
    def test_a(self,path,headers,data):
        """电商购物车接口"""
        url=self.url+path
        res=self.ak.do_post(url=url,headers=headers,json=data)
        print(res.text)
        msg=self.ak.get_text(res.text,'result')
        self.assertEqual('success',msg,msg='失败')
    @file_data('../data/danapi_data/pay.yaml')
    def test_b(self,path,headers,data):
        """购物车下单接口"""
        url=self.url+path
        res = self.ak.do_post(url=url, headers=headers, json=data)
        print(res.text)
        msg = self.ak.get_text(res.text, 'result')
        self.assertEqual('success', msg, msg='失败')
    @file_data('../data/danapi_data/demo.yaml')
    def test_c(self,path,data):
        """获取用户数据接口"""
        url = self.url + path
        res = self.ak.do_get(url=url,json=data)
        print(res.text)
    @file_data('../data/danapi_data/patient.yaml')
    def test_d(self,path,data):
        """查询病人信息接口"""
        url = self.url + path
        res = self.ak.do_get(url=url, json=data)
        print(res.text)
    @file_data('../data/danapi_data/getproductinfo.yaml')
    def test_e(self,path,data):
        """获取商品信息接口"""
        url = self.url + path
        res = self.ak.do_get(url=url, json=data)
        print(res.text)
    @file_data('../data/danapi_data/tomweather.yaml')
    def test_f(self,path,data):
        """查看明天天气接口"""
        url = self.url + path
        res = self.ak.do_get(url=url, json=data)
        print(res.text)
    @file_data('../data/danapi_data/getuserinfo.yaml')
    def test_g(self,path,headers):
        """获取个人信息接口"""
        url = self.url + path
        res = self.ak.do_get(url=url, headers=headers)
        print(res.text)
    @file_data('../data/danapi_data/weather.yaml')
    def test_h(self,path,data):
        """获取今日天气接口"""
        url = self.url + path
        res = self.ak.do_get(url=url, json=data)
        print(res.text)
    @file_data('../data/danapi_data/login.yaml')
    def test_i(self,path,data):
        url = self.url + path
        res = self.ak.do_post(url=url, json=data)
        print(res.text)
        # msg = self.ak.get_text(res.text, 'result')
        # self.assertEqual('success', msg, msg='失败')
    @file_data('../data/danapi_data/del.yaml')
    def test_j(self,path):
        url = self.url+path
        res=self.ak.do_delete(url=url)
        print(res.text)
    @file_data('../data/danapi_data/list.yaml')
    def test_k(self,path,headers):
        url = self.url + path
        res = self.ak.do_get(url=url, headers=headers)
        print(res.text)
    @file_data('../data/danapi_data/viplist.yaml')
    def test_l(self,path,headers):
        url = self.url + path
        res = self.ak.do_get(url=url, headers=headers)
        print(res.text)
if __name__ == '__main__':
    unittest.main()