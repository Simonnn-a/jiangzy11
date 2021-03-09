# _*_ conding:utf-8 _*-
# @Time:2021/1/11 &{TIME}
import unittest
from vip.homework43.config import read_ini
from vip.api_keys import jiekouKey
from ddt import ddt, file_data


@ddt
class car_new(unittest.TestCase):
    def fuzhi(self,kwargs):
        for key, value in kwargs.items():
            # 基于数据内容的格式来进行判断该用何种处理方式
            if type(value) is dict:
                self.fuzhi(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key] = getattr(self, key)
        return kwargs
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = jiekouKey()
        # cls.url = read_ini.redini('../config/server.ini', 'TEST_SERVER', 'url')
        cls.url = read_ini.redini('vip/homework43/config/server.ini', 'TEST_SERVER', 'url')#生成测试报告时的路径
        cls.token = None
        cls.userid = None
        cls.openid = None
        cls.cartid = None

    @file_data('../data/login.yaml')
    def test_a(self,path,data):
        """登录接口"""
        url = self.url + path
        res = self.ak.do_post(url=url, json=data)
        print(res.text)
        token = self.ak.get_text(res.text,'token')
        if token:
            car_new.token=token
    @file_data('../data/getuserinfo.yaml')
    def test_b(self,path,headers):
        """获取个人信息接口"""
        url = self.url + path
        headers['token']=self.token#将第一步登陆的全局变量token赋到getuserinfo.yaml中的token
        res = self.ak.do_get(url=url,headers=headers)
        print(res.text)
        userid=self.ak.get_text(res.text,'userid')
        if userid:
            car_new.userid=userid
        openid=self.ak.get_text(res.text,'openid')
        if openid:
            car_new.openid=openid
    @file_data('../data/addcar.yaml')
    def test_c(self,path,**kwargs):
        """添加购物车接口"""
        url=self.url + path
        value=self.fuzhi(kwargs)
        print(value)
        res = self.ak.do_post(url=url, headers=value['headers'], json=value['data'])
        print(res.text)
        cartid=self.ak.get_text(res.text,'cartid')
        if cartid:
            car_new.cartid=cartid
    @file_data('../data/pay.yaml')
    def test_d(self,path,**kwargs):
        """支付接口"""
        url=self.url+path
        value=self.fuzhi(kwargs)
        print(value)
        res = self.ak.do_post(url=url, headers=value['headers'], json=value['data'])
        print(res.text)

if __name__ == '__main__':
    unittest.main()