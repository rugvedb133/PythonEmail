import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

sender=input("Enter the sender name: ")
receiver=input("Enter the receiver name: ")
receiver_add=input("Enter the receiver's email address: ")

email_add=input("Login to your email address: ")
pswd=input("Enter your password: ")

html = Template(Path('original.html').read_text())
email = EmailMessage()
email['from'] = sender
email['to'] = receiver_add
email['subject'] = "Hello there"

email.set_content(html.substitute({'name': receiver}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(email_add, pswd)
  smtp.send_message(email)
  print('sent')