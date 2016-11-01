# coding:utf-8
'''
MUA：Mail User Agent——邮件用户代理, outlook等软件
MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪
MDA：新浪的MTA会把Email投递到邮件的最终目的地MDA：Mail Delivery Agent——邮件投递代理
Email到达MDA后，就静静地躺在新浪的某个服务器上
对方要取到邮件，必须通过MUA从MDA上把邮件取到自己的电脑上
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

要编写程序来发送和接收邮件，本质上就是：
    编写MUA把邮件发到MTA；
    编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# email_from = '539067032@qq.com'
# password = 'wpjtmtvwqhkmbdbe'
# smtp_server = 'smtp.qq.com'

email_from = '18064519110@163.com'
password = 'd1s1rt23xsx'
smtp_server = 'smtp.163.com'
email_to = 'xushaoxun1209@qq.com'


msg = MIMEText('你好，以下是会议内容', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % email_from)
msg['To'] = _format_addr('管理员 <%s>' % email_to)
msg['Subject'] = Header('关于会议记录...', 'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(email_from, password)
server.sendmail(email_from, [email_to], msg.as_string())
server.quit()
