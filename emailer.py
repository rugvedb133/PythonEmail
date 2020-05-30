import smtplib
from email.message import EmailMessage

sender=input("Sender name: ")
receiver=input("Receier email: ")

email  = EmailMessage()
email['from'] = sender
email['to'] = receiver
email['subject'] = 'Hello there'
email.set_content('Hello there!\nThis is an example email, sent using a Pyhton Script. ')

mail=input("Enter your email: ")
pswd=input("Enter your passsword: ")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(mail, pswd)
	smtp.send_message(email)
	print('sent')
