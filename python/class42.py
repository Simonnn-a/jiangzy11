# _*_ conding:utf-8 _*-
# @Time:2021/1/10 &{TIME}
'''
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法。
    主要实现常用的关键字内容，并定义好所有的参数的内容即可
    接口中的常用关键字无非就是：
        1. 各种模拟请求方法：post/get/put/delete/header/.....
        2. 设置入参的默认值时，设置的参数必须放在最后
'''
# 导包
import json

import jsonpath
import requests


class ApiKey:
    # get请求的封装：因为params可能会存在无值的情况，存放默认值None
    def do_get(self, url, params=None, **kwargs):
        # 因为请求会默认返回一个响应，所以函数定义时需要return一下
        return requests.get(url=url, params=params, **kwargs)

    # post请求的封装：data也可能存在无值的情况存,放默认值None
    def do_post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # 基于JsonPath获取数据的关键字：用于提取所有需要的内容
    def get_text(self, txt, key):
        # jsonpath获取数据的表达式：成功则返回list，失败则返回false
        '''
            对于json格式数据的获取，本身是存有目的性来获取的。
        '''
        try:
            txt = json.loads(txt)
            value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value


if __name__ == '__main__':
    ak = ApiKey()
    data = {
        'username': 'admin',
        'password': '123456'
    }
    res = ak.do_get(url='http://39.98.138.157:5000/api/getuserinfo', timeout=0.1)
    print(res.text)
    ak.do_post(url='http://39.98.138.157:5000/api/login', json=data)


import unittest
from ddt import ddt, file_data

from class42.api_keyword.api_key import ApiKey


@ddt
class ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()

    # def setUp(self) -> None:
    #     self.ak = ApiKey()
    @file_data('../data/user.yaml')
    def test_1(self, user, msg):
        # ak = ApiKey()
        url = 'http://39.98.138.157:5000/api/login'
        data = {
            'username': user['username'],
            'password': user['password']
        }
        res = self.ak.do_post(url=url, json=data)
        print(res.text)
        # 获取响应中的结果，用于校验是否成功
        msg1 = self.ak.get_text(res.text, 'msg')
        print(msg1)
        self.assertEqual(msg1, msg, msg='异常')


if __name__ == '__main__':
    unittest.main()


'''
    JsonPath模块，是一个专门用于处理Json字符串的模块。JsonPath相当于是Xpath
    部署JsonPath，通过pip install jsonpath来进行安装
    通过JsonPath获得的内容，会以list的形式进行返回，也就意味着你的jsonpath是可以有一个值或者多个值同时存在的。
    如果要基于JsonPath来处理json数据，就一定要同步去处理list
    JsonPath定义中，如果表达式出现错误，则会返回False（布尔类型的值）
    JsonPath要么返回False，要么返回list
'''
import jsonpath,json

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
# 基于JsonPath获取元素:通过jsonpath函数来进行获取(json数据,定位表达式)
'''
    jsonpath表达式的基本格式规范：
        $ 表示根节点，也是所有jsonpath的表达式的开始
        . 表示获取子节点
        .. 表示获取所有符合条件的内容
        * 表示所有的元素节点
        [] 表示迭代器的标示（可以用于处理下标等情况）
        [,] 表示多个结果的选择
        ?() 表示过滤操作
        @ 表示当前节点
'''
bicycle = jsonpath.jsonpath(data, '$.store.bicycle.color')
print(bicycle[0])
print(bicycle)
# book = jsonpath.jsonpath(data, '$.store.book')
# print(book)
# # 获取store下的所有price节点的值
# price = jsonpath.jsonpath(data, '$.store..price')
# print(price)
# # 获取指定book下的price节点
# book_price = jsonpath.jsonpath(data, '$.store.book[0,10].price')
# print(book_price)
# # 获取price大于10的所有book
# book_1 = jsonpath.jsonpath(data, '$..book[?(@.price>10)]')
# print(book_1)
# # 这是一条错误的JsonPath
# book_2 = jsonpath.jsonpath(data, '$..虚竹[?(@.price>10)]')
# print(type(book_2))

