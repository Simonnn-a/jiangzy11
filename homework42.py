# _*_ conding:utf-8 _*-
# @Time:2021/1/10 &{TIME}
import unittest
from ddt import ddt, file_data
from api_keys import jiekouKey

@ddt
class Ceshi(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak=jiekouKey()
    # @file_data('user.yaml')
    def test_a(self):
        url='http://39.98.138.157:5000/api/login'
        data = {
            'username':'admin',
            'password':'123456',
        }
        msg='success'
        res=self.ak.do_post(url=url,json=data)
        print(res.text)
        msg1 = self.ak.get_text(res.text,'msg')
        print(msg1)
        self.assertEquals(msg1,msg,msg='异常')
    def test_b(self):
        url = 'http://39.98.138.157:5000/api/getweather'
        data = {
            'city': '1'
        }
        msg = 'success'
        res = self.ak.do_get(url=url, json=data)
        print(res.text)
        print(res.status_code)
        msg1 = self.ak.get_text(res.text, 'msg')
        print(msg1)
        # self.assertEquals(msg1, msg, msg='异常')

if __name__ == '__main__':
    unittest.main()
