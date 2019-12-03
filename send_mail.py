import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from mailBody import mail_body
from credentialDetail import getDetails

def sendMAil(data,hr):
    # instance of MIMEMultipart 
    try:
        msg = MIMEMultipart() 

        # storing the senders email address 
        msg['From'] = data['email']

        # storing the receivers email address 
        msg['To'] = hr

        # storing the subject 
        msg['Subject'] = "Application regarding open post as " + data['post']

        # string to store the body of the mail 
        body = mail_body(data['post'])

        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 

        # open the file to be sent 
        filename = "resume.pdf"
        attachment = open(data['resume_path'], "rb") 

        # instance of MIMEBase and named as mimeObj 
        mimeObj = MIMEBase('application', 'octet-stream') 

        # To change the payload into encoded form 
        mimeObj.set_payload((attachment).read()) 

        # encode into base64 
        encoders.encode_base64(mimeObj) 

        mimeObj.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        # attach the instance 'mimeObj' to instance 'msg' 
        msg.attach(mimeObj) 

        # creates SMTP session 
        mailObj = smtplib.SMTP_SSL('smtp.gmail.com', 465) 

        # start TLS for security 
        #mailObj.starttls() 

        # Authentication 
        mailObj.login(data['email'], data['password']) 

        # Converts the Multipart msg into a string 
        text = msg.as_string() 

        # sending the mail 
        mailObj.sendmail(data['email'], hr, text) 

        # terminating the session 
        mailObj.quit() 
        print("Successfully sent to "+hr)
    except Exception as e:
        print("error:  "+str(e))

sendMAil(getDetails('saurav'),"sauravaggarwal98@gmail.com")
