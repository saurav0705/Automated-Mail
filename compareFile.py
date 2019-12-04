from fileValidationCheck import fileValidation
from mailTemplate import sendMailToList


def compareFiles(**kwargs):
    #validating the weekend file for invalid email and duplication
    fileValidation(file=kwargs['weekend'])
    #checking if master exists or not if not creating master file in current working directory
    if kwargs['master']=="":
        masterData = open("master.txt","r")
        kwargs['master']='master.txt'
    #if master exist openning the file
    else:
        masterData = open(kwargs['master'],'r')
    masterDataList = []
    #creating a list of data in master file 
    with masterData as variable:
        for lines in variable:
            masterDataList.append(lines.replace("\n",""))
    masterData.close()
    #differ will contain the mails that are not present in master but in weekend
    differ=[]
    #opening weekend file
    weekendData = open(kwargs['weekend'],'r')
    with weekendData as variable:
        for lines in variable:
            #checking if weekend data present in master or not if not it is added into the list
            if lines.replace("\n","") not in masterDataList:
                differ.append(lines.replace("\n",""))
    weekendData.close()
    #getting input from the user about from which data email should be sent which will give details to send_mail file
    user = input("Enter User :: ")
    #sending mails to all the persons which are not present in master file but in weekend file
    sendMailToList(user,differ,kwargs['master'])
    


