"""
Time    : 2019/4/1 10:58
Author  : wang xin
Email   : 452427904@qq.com
File    : send_mail.py
"""

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# 生成第三方授权码
_user = '452427904@qq.com'
_pwd = 'chrytljxpdhjbjae'

now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

class SendEmail:

    def send_email(self, email_to, filepath):
        msg = MIMEMultipart()
        msg['Subject'] = now + 'alex的测试报告'
        msg['From'] = _user
        msg['To'] = email_to

        # 邮件正文
        part = MIMEText('这是邮件的正文内容')
        msg.attach(part)

        # 邮件附件
        part = MIMEApplication(open(filepath, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(part)

        # 连接smtp服务器，端口默认25
        s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
        s.login(_user, _pwd)
        s.sendmail(_user, email_to, msg.as_string())
        s.close()

if __name__ == '__main__':
    SendEmail().send_email('452427904@qq.com',r'E:\workspace\wxPythonCode\wxPythonCode\m7\Lemon_Tree\FurureLoan\test_result\result.html')