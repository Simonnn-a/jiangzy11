# _*_ conding:utf-8 _*-
# @Time:2021/3/1 &{TIME}
import pytest
@pytest.mark.webui
def test_01():
    print('这是第一条测试用例')
@pytest.mark.interface
def test_02():
    print('这是第二条测试用例')

if __name__ == '__main__':
    pytest.main(['-sv' ,'-rA'])