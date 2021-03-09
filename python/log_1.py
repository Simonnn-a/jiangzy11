#_*_ conding:utf-8 _*-
#@Time:2020/11/3 &{TIME}
import logging
#格式的设置
fmt='%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
#日志级别设置
logging.basicConfig(level=logging.INFO,format=fmt,filename='log_1.log')#BUG常量
logging.debug('debug模式')#debug方法
logging.info('info模式')
logging.warning('warning模式')
logging.error('error模式')
logging.critical('critical模式')
