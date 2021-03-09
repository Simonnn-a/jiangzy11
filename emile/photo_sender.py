#_*_ conding:utf-8 _*-
#@Time:2020/11/10 &{TIME}
# 发送附件邮件 txt,excel.pdf
import smtplib
# 发送附件包
from email.mime.multipart import MIMEMultipart
# 文本方式
from email.mime.text import MIMEText
# 设置头部内容
from email.header import Header
#图片附件
from email.mime.image import MIMEImage

con = smtplib.SMTP_SSL('smtp.qq.com', '465')
con.login(user='1067263257@qq.com', password='dwvdjephnjzkbejb')
sender = '1067263257@qq.com'
recevier = ['1067263257@qq.com', '1078284788@qq.com']
# 发送附件
# 实例化附件 创建一个信封
message = MIMEMultipart()
# 文件路径
image = open('zhaopian.jpg', 'rb').read()
# 把读取出来的内容放在文本中 信纸
file1 = MIMEImage(image)
# 给图片取名字
file1['Content-Disposition'] = "attachment;filename='情书'"
# 把信纸放到信封中
message.attach(file1)
# 发送正文
msg = MIMEText('我是附件正文', 'plain', 'utf-8')
message.attach(msg)
# 设置头部内容
# 设置头部标题
message['subject'] = Header('附件标题', 'utf-8')
# 发件人
message['From'] = Header('jzy1067263257@qq.com', 'utf-8')
# 收件人
message['To'] = Header('jzy2', 'utf-8')
con.sendmail(sender, recevier, message.as_string())