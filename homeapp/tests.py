from django.shortcuts import render
from django.test import TestCase

# Create your tests here.



import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.header import Header
import random



# 向邮箱发送信息
my_sender = 'carry7123@163.com'
# 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = 'zhaolianxin1994@163.com'


# 收件人邮箱账号，为了后面易于维护，所以写成了变量


def mail():
    my_sender = 'carry7123@163.com'
    # 发件人邮箱账号，为了后面易于维护，所以写成了变量
    my_user = '25259808@qq.com'

    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt = ''.join(random.sample(s, 15))
    print(salt)

    # 代码替换开始行
    msg = MIMEText(salt, 'plain', 'utf-8')
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    msg['From'] = formataddr(["carry7123@163.com", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To'] = formataddr(['25259808@qq.com', my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "主题"  # 邮件的主题，也可以说是标题
    # 标准邮件需要三个头部信息： From, To, 和 Subject ，每个信息直接使用空行分割。
    print(33)
    # 代码替换结束行
    ret = True
    try:
        server = smtplib.SMTP("smtp.163.com", 25)
        # 发件人邮箱中的SMTP服务器，端口是25
        # POP3服务器: pop.163.com
        # SMTP服务器: smtp.163.com
        # IMAP服务器: imap.163.com
        print(42)
        server.login(my_sender, "q1w2e3r4")
        # 括号中对应的是发件人邮箱账号、邮箱密码
        print(52)
        #
        server.sendmail(my_sender, [my_user, ], msg.as_string(salt))
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号(字符串列表)、发送的邮件
        print(55)
        server.quit()  # 这句是关闭连接的意思
    except Exception:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret = False
    return ret


if mail():
    print("邮件发送成功")  # 发送成功
else:
    print("Error: 无法发送邮件")  # 发送失败


# 像手机发送


