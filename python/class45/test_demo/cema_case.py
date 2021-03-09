import pytest

'''
    Pytest默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
    Pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
    Pytest生成测试报告：pytest-html测试报告模块，如果要集成到邮件，就需要添加指令--self-contained-html
'''


# 测试用例
@pytest.mark.webui
def vip_02(xuzhu):
    assert xuzhu == 2, '失败'


def vip_01(xuzhu):
    print('test01')


# pytest运行主入口
if __name__ == '__main__':
    pytest.main(['-s'])
