import smtplib

host = 'smtp-mail.outlook.com'
port = 587

user = "raspberrypi1234_420@outlook.com"
password= "Tigrou007"
receiver = "raspberrypi1234_420@outlook.com"

message = """From: rasp
To: raspberrypi1234_420@outlook.com
Subject: Demo email test
This is a test e-mail.
"""

conn = smtplib.SMTP(host, port)

conn.ehlo()

conn.starttls()
conn.ehlo()

conn.login(user, password)

conn.sendmail(user, receiver, message)

conn.quit()