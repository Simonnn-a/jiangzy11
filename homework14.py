#_*_ conding:utf-8 _*-
#@Time:2020/11/30 &{TIME}
from key_words import WebKeys

wd = WebKeys('Chrome')
"""登陆商城"""
wd.open('http://39.98.138.157/shopxo/')
el = wd.locaters('xpath','//a[text()="登录"]')
el[2].click()
wd.input('xpath','//input[@data-validation-message="请填写登录账号"]','sdfsdghl')
wd.input('xpath','//input[@data-validation-message="密码格式 6~18 个字符之间"]','sdfsdghl')
wd.click('xpath','//button[text()="登录"]')
"""断言是否登陆成功"""
wd.assert_txt('sdfsdghl','xpath','//em[text()="sdfsdghl"]')
"""搜索商品"""
wd.input('xpath','//input[@id="search-input"]','iphone')
wd.click('xpath','//input[@id="ai-topsearch"]')
wd.click('xpath','//img[@src="http://39.98.138.157/shopxo/public/static/upload/images/goods/2019/01/14/1547451274847894.jpg"]')
"""切换句柄"""
wd.sw_win(1)
"""选择套餐"""
wd.click('xpath','//li[@data-value="套餐一"]')
wd.wait(2)
wd.click('xpath','//li[@data-value="银色"]')
wd.wait(2)
wd.click('xpath','//li[@data-value="128G"]')
wd.wait(2)
wd.click('xpath','//button[text()="加入购物车"]')
"""显式等待"""
wd.visit_wait(2,'xpath','//*[@id="common-prompt"]')
"""断言查看是否添加成功"""
wd.click('xpath','//span[text()="购物车"]')
wd.assert_txt('苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G','xpath','//a[text()="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"]')
"""关必浏览器，释放内存"""
wd.quit()