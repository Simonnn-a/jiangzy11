import pytest
from class46.data_driver import yaml_driver
import requests

token = None


# 需要数据的测试用例: 数据驱动可以直接传递数值，也可以通过函数的形式将结果生成并返回。
@pytest.mark.parametrize('data', yaml_driver.load_yaml('../data/user.yaml'))
def test_login(data):
    # print('-----------------------')
    # print(data)
    url = 'http://39.98.138.157:5000/api/login'
    res = requests.post(url=url, json=data)
    # print(res.text)
    global token
    token = res.json()['token']
    # print(token)


def test_02(xuzhu01):
    print('test02')
    print(xuzhu01)


if __name__ == '__main__':
    pytest.main(['-s'])
