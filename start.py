import sys

YourGmailID= raw_input("YourGmailID -----> ")
fo = open("YourGmailID.txt","w")
fo.write(YourGmailID)
fo.close()

YourGmailPassword= raw_input("YourGmailPassword -----> ")
fo = open("YourGmailPassword.txt","w")
fo.write(YourGmailPassword)
fo.close()

Way2SMSLogin= raw_input("Way2SMSLogin -----> ")
fo = open("Way2SMSLogin.txt","w")
fo.write(Way2SMSLogin)
fo.close()

Way2SMSPassword= raw_input("Way2SMSPassword -----> ")
fo = open("Way2SMSPassword.txt","w")
fo.write(Way2SMSPassword)
fo.close()

PhoneNumber= raw_input("PhoneNumber -----> ")
fo = open("PhoneNumber.txt","w")
fo.write(PhoneNumber)
fo.close()

EmailIdForNotifications= raw_input("EmailId For which you want to receive notifications -----> ")
fo = open("EmailIdForNotifications.txt","w")
fo.write(EmailIdForNotifications)
fo.close()
