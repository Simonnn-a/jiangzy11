import pytest
import allure


@allure.feature('用于描述测试需求的情况')
@allure.story('用户访问首页情况下')
@allure.title('测试01用例名称')
@pytest.mark.test
def test_01():
    with allure.step('用例01的第一个测试步骤'):
        print('------------')
        print('test01')
        with open('../img/1.jpg', 'rb') as f:
            img = f.read()
        allure.attach(img, '这是虚竹的自拍')
    assert 1 == 2


@allure.feature('用于描述测试需求的情况')
@allure.story('用户访问个人中心情况下')
@allure.title('测试02用例名称')
def test_02():
    print('------------')
    print('test02')


@allure.story('用户下单失败的情况')
@allure.title('测试03用例名称')
def test_03():
    print('------------')
    print('test03')
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_case03.py', '--alluredir', './result/'])
    # pytest.main(['-s', '--ff', 'test_case03.py'])
