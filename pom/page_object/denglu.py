# _*_ conding:utf-8 _*-
# @Time:2020/12/17 &{TIME}
from selenium import webdriver
from selenium.webdriver.common.by import By

from options import Options
from pom.base.key_pom import Basekey
class loginpage(Basekey):
    url = Basekey.url + '?s=/index/user/logininfo.html'
    user=(By.NAME,'accounts')
    pwd=(By.NAME,'pwd')
    button=(By.XPATH,'//button[text()="登录"]')
    def login(self,username,password):

        self.open()
        self.input(self.user,username)
        self.input(self.pwd,password)
        self.click(self.button)
if __name__ == '__main__':

    wd=webdriver.Chrome(options=Options().options_conf())
    dl=loginpage(wd)
    user='sdfsdghl'
    pwd='sdfsdghl'
    dl.login(user,pwd)