from email import charset
import os
import smtplib
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

msg = MIMEMultipart()

msg["From"] = "my_email@naver.com"
msg["To"] = "my_email@naver.com"
msg["Date"] = formatdate(localtime=True)
msg["Subject"] = Header(s="파일 첨부 메일 송신 테스트", charset="utf-8")
body = MIMEText("첨부된 파일 2개를 확인해 주세요.", charset="utf-8")
msg.attach(body)

files = list()
files.append("c:/projects/pylib/test1.pdf")
files.append("c:/projects/pylib/test2.jpg")

for f in files:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)
    part.add_header(
        "Content-Disposition", "attachment; filename='%s'" % os.path.basename(f)
    )
    msg.attach(part)

mailServer = smtplib.SMTP_SSL("smtp.naver.com")
mailServer.login("my_email@naver.com", "my_passwd")
mailServer.send_message(msg)
mailServer.quit()
