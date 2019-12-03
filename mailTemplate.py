from credentialDetail import getDetails
from send_mail import sendMAil

def sendMail(user,differ):
    for diff in differ:
        sendMAil(getDetails(user),diff)


