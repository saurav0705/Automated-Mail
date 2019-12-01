import smtplib
from mailBody import *
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
#from email.MIMEImage import MIMEImage
import json


data = json.load(open("credential.json"))
print(data)
def sendMail(**kwargs):
    

    sender = ""
    receivers = [['sauravaggarwal98@gmail.com',"python"],["singhbirvarinder@gmail.com","devops"]]


    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
        smtpObj.starttls()
        for i in sender:
            smtpObj.login(i,"championship")
            for j in receivers:
                msg = MIMEMultipart()
                mess = mail_body(str(j[1]))
                smtpObj.sendmail(sender, str(j[0]), mess)         
                print("Successfully sent email to " + str(j[0]))
    except Exception as e:
        print(e)


#sendMail()