通过python发送邮件

```python
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 生成第三方授权码
_user = ''
_pwd = ''

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


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
    part.add_header('Content-Disposition', 'attachment', filename = filepath)
    msg.attach(part)

    # 连接smtp服务器，端口默认25
    s = smtplib.SMTP_SSL('smtp.qq.com', timeout=30)
    s.login(_user,_pwd)
    s.sendmail(_user, email_to, msg.as_string())
    s.close()
```



验证余额