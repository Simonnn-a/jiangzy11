# _*_ conding:utf-8 _*-
# @Time:2021/1/10 &{TIME}
# 导入md5加密的库
import hashlib


# arg = '守护世界上最好的虚竹'
# print(arg)
# # md5加密的实现形式
# se = hashlib.md5(arg.encode('utf-8'))
# # 获取变量的内存地址
# print(se)
# # 获取值
# print(se.hexdigest())

# md5加密的封装函数
def hashmd5(string):
    return hashlib.md5(str(string).encode('utf-8')).hexdigest()




# 实现Mock的数据生成与调用
from unittest import mock


# 伪造一个接口数据
def plus(a, b):
    # return a + b
    '''
    :param a: int
    :param b: int
    :return: a+b
    '''
    pass


def math():
    b = plus(1, 2)
    print('math:{0}'.format(b))
    return b


# 登录专用mock函数
def login(data):
    return requests.post(url='http://39.98.138.157:5000/api/login', json=data)

# print(plus(1, 2))
# # 对指定的接口进行mock值的生成
# '''
#     mock.Mock，定义函数的返回值，无关乎函数本身内容，直接写入最终的返回结果
# '''
#
# plus = mock.Mock(return_value=2)
# c = plus(1, 2)
# print(c)


import unittest
from unittest import mock, TestCase
import requests

from class41.mock_server import mock_demo


class Demo(TestCase):
    # 常规形态下的mock实现
    # def test_1(self):
    #     mock_demo.plus = mock.Mock(return_value=5)
    #     c = mock_demo.math()
    #     print(c)

    # 基于装饰器的形态来实现的mock：定义哪个接口需要进行mock
    @mock.patch('mock_demo.login')
    def test_2(self, mock_login):
        # 已经完成了Mock数据的生成：mock的操作相当于自主定义生成测试数据，快速提供至测试行为之中
        # a = mock_login.return_value = {'password': '123456',
        #                                'username': 'admin'}
        a = mock_demo.login()
        res = requests.post(url='http://39.98.138.157:5000/api/login', json=a)
        print(res.text)

    # mock实现形式3：如果要实现多次调用，每次有不同的值
    @mock.patch.object(mock_demo, 'plus')
    def test_3(self, mock_plus):
        mock_plus.side_effect = [
            'plus1',
            'plus2',
            'plus3'
        ]
        for i in range(0, 3):
            mock_demo.math()


if __name__ == '__main__':
    unittest.main()


