from credentialDetail import getDetails
from send_mail import sendMAil
from mergeFile import mergeFiles
from fileValidationCheck import divider

def sendMailToList(user,differ,master):
    #sending mail to all the mails present in differ list
    for diff in differ:
        sendMAil(getDetails(user),diff)
    divider()
    #updating the master file with the new data present in the weekend file
    mergeFiles(master=master,differ=differ)
    


