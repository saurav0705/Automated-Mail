# Automated-Mail
Automated mail system in which a mail can be send to multiple users all you need is to provide a document conatining mail id's of respective persons whom do you want to send the mail.


#fileValidationCheck.py
This file validats the file provided by the user for any non mail value which is the early check to prevent address not found error in future. 



workflow:::

open driverFile.py
just give the path of master document and the weekend document
give the credentials in credential.json
it will ask for user from which mail is to be sent
give it the user
and mails will be send and master file will be updated
NOTE:: 1. if running for first time just leave master="" this will create a master file if no master file exist
       2. change the path of json file in credentialDetail.py



driverFile.py -> compareFile.py -> fileValidationCheck.py -> mailTemplate.py(calls credentialDetail.py) -> send_mail.py(calls mailBody.py) -> mergeFile.py