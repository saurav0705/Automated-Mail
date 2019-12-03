<<<<<<< HEAD
import json


data = json.load(open(r'C:\\Users\\saurav.aggarwal\\Desktop\\credential.json'))

def getDetails(user):
    return data[user]
=======
import json


data = json.load(open(r'credential.json'))

def getDetails(user):
    return data[user]

print(getDetails('username'))
>>>>>>> 57e068d9124c93f77bc9e25bd639d1e7b2fdd179
