# _*_ conding:utf-8 _*-
# @Time:2020/12/17 &{TIME}
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.base.key_pom import Basekey
class gouwu(Basekey):
    url = Basekey.url + '?s=/index/goods/index/id/2.html'
    suite=(By.XPATH,'//li[@data-value="套餐一"]')
    color=(By.XPATH,'//li[@data-value="银色"]')
    memory=(By.XPATH,'//li[@data-value="128G"]')
    tianjia=(By.XPATH,'//button[text()="加入购物车"]')
    def add(self):
        self.open()
        self.click(self.suite)
        sleep(1)
        self.click(self.color)
        sleep(1)
        self.click(self.memory)
        sleep(1)
        self.click(self.tianjia)
if __name__ == '__main__':
    wd=Basekey('Chrome')
    gou=gouwu()
    gou.add()
