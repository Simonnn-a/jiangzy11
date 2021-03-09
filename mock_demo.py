# _*_ conding:utf-8 _*-
# @Time:2021/1/10 &{TIME}
import unittest
from unittest import mock
#伪造一个接口
import requests



class momo:
    def plus(a,b):
        pass   #不输出任何值
    def math():
        b=plus(1,2)
        print('math:{0}'.format(b))
        return b

    #登录mock函数
    def login(data):
        # return requests.post(url='http://39.98.138.157:5000/api/login',json=data)
        pass

# print(plus(1,2))
# #伪造假接口
# """
# mock.Mock,定义函数的返回值，与函数本身传递的参数无关，直接返回伪造的mock
# """
# plus = mock.Mock(return_value=3)
# c=plus(2,2)
# print(c)