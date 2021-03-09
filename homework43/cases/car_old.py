# _*_ conding:utf-8 _*-
# @Time:2021/1/11 &{TIME}
import unittest
import requests
class carold(unittest.TestCase):
    def test_1(self):
        """登录"""
        url='http://39.98.138.157:5000/api/login'
        data = {
            'username':'admin',
            'password':'123456'
        }
        res = requests.post(url=url,json=data)
        """获取个人信息"""
        url = 'http://39.98.138.157:5000/api/getuserinfo'
        headers = {
            'token':res.json()['token']
        }
        res1=requests.get(url=url,headers=headers)
        print(res1.text)
        """"添加购物车"""
        url='http://39.98.138.157:5000/api/addcart'
        headers = {
            'token':res.json()['token']
        }
        data = {
            'userid':res1.json()['data'][0]['userid'],
            'openid':res1.json()['data'][0]['openid'],
            'productid':8888
        }
        res2=requests.post(url=url,headers=headers,json=data)
        print(res2.text)
        """购物车下单"""
        url='http://39.98.138.157:5000/api/createorder'
        headers={
            'token':res.json()['token']
        }
        data={
            'userid': res1.json()['data'][0]['userid'],
            'openid': res1.json()['data'][0]['openid'],
            'productid': 8888,
            'cartid':res2.json()['data'][0]['cartid']
        }
        res3=requests.post(url=url,headers=headers,json=data)
        print(res3.text)
        self.assertEqual('success',res3.json()['result'],msg='error')

if __name__ == '__main__':
    unittest.main()

