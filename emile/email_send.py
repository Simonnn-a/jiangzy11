#_*_ conding:utf-8 _*-
#@Time:2020/11/10 &{TIME}
#封装了smtp协议
import smtplib
#文本方式
from email.mime.text import MIMEText
#设置头部内容
from email.header import Header
#创建邮箱服务器连接
#邮箱有多种类别，括号里写邮箱链接地址，端口号  ssl:465 无ssl：587
con=smtplib.SMTP_SSL('smtp.qq.com','465')
#登录 用户名和密码,163邮箱直接填 qq邮箱需要授权密
con.login(user='1067263257@qq.com',password='dwvdjephnjzkbejb')

#发送者帐号
sender='1067263257@qq.com'
# 接收者帐号
recevier=['1067263257@qq.com','1078284788@qq.com']

#准备发送邮件   _text邮件正文   _subtype=文本类型 plain默认纯文本 _charset=编码格式
message=MIMEText(_text='练习python发邮件，不用管',_subtype='plain',_charset='utf-8')
#设置头部内容
#设置头部标题
message['subject']=Header('文本标题','utf-8')
#发件人
message['From']=Header('jzy1067263257@qq.com','utf-8')
#收件人
message['To']=Header('jzy2','utf-8')

#发送邮件
con.sendmail(sender,recevier,message.as_string())
