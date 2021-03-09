# _*_ conding:utf-8 _*-
# @Time:2020/12/17 &{TIME}
from selenium import  webdriver

class Basekey:
    url='http://39.98.138.157/shopxo/index.php'
    def __init__(self,wd):
        self.wd = wd
    def open(self):
        self.wd.get(self.url)
    def locater(self,loc):
        return self.wd.find_element(*loc)
    def input(self,loc,txt):
        self.locater(loc).send_keys(txt)
    def click(self, loc):
        self.locater(loc).click()
