# _*_ conding:utf-8 _*-
# @Time:2021/1/6 &{TIME}
import unittest
from unittest import mock

import requests
from mock_demo import momo


class MMmo(unittest.TestCase):

    @mock.patch.object(momo, 'login')
    def test_a(self,mock_login):
        # a = mock_demo.login()
        b=mock_login.return_value = "{'username':'admin','password':'123456'}"
        print(b)
        res = requests.post(url='http://39.98.138.157:5000/api/login', json=b)
        print(res.text)

    @mock.patch.object(momo, 'plus')
    def test_b(self,mock_plus):
        mock_plus.side_effect = [
            'a'
            'b'
            'c'
        ]
        for i in range(0,2):
            momo.math()



if __name__ == '__main__':
    unittest.main()