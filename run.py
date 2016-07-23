#!/usr/bin/python

import urllib2
import cookielib
import imaplib
import email
import datetime

fo = open("YourGmailID.txt","r")
YourGmailID= fo.read()
YourGmailID = YourGmailID.strip()
fo.close()

fo = open("YourGmailPassword.txt","r")
YourGmailPassword= fo.read()
YourGmailPassword = YourGmailPassword.strip()
fo.close()

fo = open("Way2SMSLogin.txt","r")
Way2SMSLogin= fo.read()
Way2SMSLogin = Way2SMSLogin.strip()
fo.close()

fo = open("Way2SMSPassword.txt","r")
Way2SMSPassword= fo.read()
Way2SMSPassword = Way2SMSPassword.strip()
fo.close()

fo = open("PhoneNumber.txt","r")
PhoneNumber= fo.read()
PhoneNumber = PhoneNumber.strip()
fo.close()

fo = open("EmailIdForNotifications.txt","r")
EmailIdForNotifications= fo.read()
EmailIdForNotifications = EmailIdForNotifications.strip()
fo.close()

#getting mails
M = imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login(YourGmailID,YourGmailPassword)
M.select('inbox')
result1 , msgnum = M.search(None,'FROM', ' %s '%(str(EmailIdForNotifications)))
msgnum = msgnum[0].split(' ')
date = str(datetime.date.today() - datetime.timedelta(10))

for m in msgnum:
	result, data = M.fetch(m,'(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	if email_message['date'] > date :
		username = Way2SMSLogin
		passwd = Way2SMSPassword
		number = PhoneNumber
		message ="An Email was sent by %s with subject : %s on %s .Please ask goru to show it to you. " % (EmailIdForNotifications,email_message['subject'],email_message['date'])

		#logging into the sms site
		url ='http://site24.way2sms.com/Login1.action?'
		data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

		#Remember, Cookies are to be handled
		cj= cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

		opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
		try:
			usock =opener.open(url, data)
		except IOError:
			print "error"

		jession_id =str(cj).split('~')[1].split(' ')[0]
		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
		send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
		opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
		try:
			sms_sent_page = opener.open(send_sms_url,send_sms_data)
		except IOError:
			print "error"

		print "success" 
