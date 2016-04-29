#python内置对SMTP的支持,可以发送文本 HTML 附件等邮件
#email模块--负责构造邮件;smtplib--负责发送邮件
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText
import smtplib
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
#输入Email地址和口令:
from_addr = input('From:')
password = input('password:')
#输入收件人地址:
to_addr1 = input('To 1:')
#to_addr2 = input('To 2:')
#输入SMTP服务器地址:
smtp_server = input('SMTP server:')
msg = MIMEText('hello,send by python...','plain','utf-8')
#第一个参数就是邮件正文，第二个是MIME的subtype--’plain‘表示纯文本
#‘text/plain’   最后utf-8编码保证多语言兼容性
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr1)
msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)#SMTP协议默认端口25
server.set_debuglevel(1)
#打印出和SMTP服务器交互的所有信息，SMTP协议就是简单的文本命令和响应
server.login(from_addr,password)
#login()方法用来登录SMTP服务器
server.sendmail(from_addr,[to_addr1],msg.as_string())
#554 DT:SPM 发送的邮件内容包含了未被许可的信息
#或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；
#sendmail()发邮件，一次可以发送多个人，可传入一个list
#邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()