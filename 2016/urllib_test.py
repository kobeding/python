from urllib import request
import json,random,smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText
mail_host="smtp.163.com"     #设置服务器
mail_user="15625068086@163.com"    #用户名
mail_pass="kobeDING2008"        #密码
mailto_list=['15625068086@139.com']     #邮件接受者
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

def send_mail(to_list,name,sub,content):                
	#to_list：收件人；sub：主题；content：邮件内容;
	me=name+"<"+mail_user+">" 
	msg = MIMEText(content,'plain','utf-8')#创建一个实例，这里设置为纯文字格式邮件编码utf8
	msg['Subject'] = Header(sub,'utf-8').encode()    #设置主题
	msg['From'] = _format_addr('name <%s>' % mail_user)       #设置发件人
	msg['To'] = ";".join(to_list)  
	#msg['To'] = _format_addr('管理员 <%s>' % to_list)
	try:  
		server = smtplib.SMTP(mail_host,25)             #实例化 
		server.set_debuglevel(1)      
		server.connect(mail_host)           #连接smtp服务器
		server.login(mail_user,mail_pass)   #登陆服务器
		server.sendmail(me,to_list,msg.as_string()) #发送邮件
		server.close()  
		return True  
	except Exception as e:  
		print (str(e))  
		return False
#appkey = "198fe9800deca7f123beff5489fdd069"
appkey = "13dc980e9286ff2da40d9abc2214d98a"
url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'
req = request.Request(url)
req.add_header("apikey", appkey)
with request.urlopen(req) as f:
	content = f.read()
	if(content):
		print(content)
		json_result = json.loads(content.decode('utf-8'))
		content_list = json_result['showapi_res_body']['contentlist']
		first_title = content_list[random.randint(0,20)]['title']
		first_text = content_list[random.randint(0,20)]['text']
		print('标题：'+first_title)
		print('内容：'+first_text)
		#length = len(first_text)
		#part1 = first_text[0:10]
		#part2 = first_text[10:22]
		#part3 = first_text[22:length]
		#print (part1,"+",part2,"+",part3)
		"""
		minlen = 10000
		for item in content_list:
			if len(item['text'])<minlen:
				first_title = item['title']
				first_text = item['text']
				minlen = len(item['text'])
		print ('title：'+first_title)
		print ('content：'+first_text)
		"""
		if send_mail(mailto_list,'kding_81','开心一笑',first_title+":"+first_text):  
			print ("send msg succeed")
		else:  
			print ("send msg failed")  
			
	else:
		print("get joke error")
	