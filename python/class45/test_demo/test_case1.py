import pytest

'''
    Pytest默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
    Pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
    多条指令一同运行时，需要通过空格进行区分，在main函数中，是通过,进行分割
    -v 用于详细显示日志信息
    -rA 测试结果的简单统计
    -q 忽略
    pytest中的setup和teardown：一般可以通过一个配置文件直接进行管理：配置文件命名一定要是conftest.py
'''


# 前置与后置条件
def setup_function():
    print('function')


def teardown_function():
    print('tfunction')


def setup_module():
    print('module')


def teardown_module():
    print('tmodule')


# 测试用例
def test_02():
    print('test102')


def test_01():
    print('test101')


# pytest中class对象的定义：建议以test开头
'''
    在class中前置后置函数的运行顺序：
        setup class
        setup method
        setup
        teardown
        teardown method
        teardown class
'''


class CemaDemo:
    def setup(self):
        print('inside setup')

    def teardown(self):
        print('inside teardown')

    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_d1(self):
        print('testd1')

    def test_d2(self):
        print('testd2')


# pytest运行主入口
if __name__ == '__main__':
    pytest.main(['-s', 'test_case1.py'])
