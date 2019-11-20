"""smtp_mail.py file and config.py file needs to be in the same directory 
	can add extra commands to automate the process of sending email to desired email address
"""

import smtplib
import config

def send_email(subject, msg):
	try:
		#different email providers have different port numbers
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.SENDER_EMAIL, config.PASSWORD)
		message = 'Subject: {}\n\n{}'.format(subject,msg)#final message that will will sent
		server.sendmail(config.SENDER_EMAIL, config.RECEIVER_EMAIL, message)
		server.quit()
		print("\nSuccess, Email sent\n")#just a message not really required
	except:
		print("\nEmail failed to send\n")

#can directly accept from the user
subject = "TEST SUBJECT"
msg = "Hello there"

send_email(subject, msg)