# _*_ conding:utf-8 _*-
# @Time:2021/1/11 &{TIME}
import configparser
def redini(path,section,option):
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(section,option)
    return value
