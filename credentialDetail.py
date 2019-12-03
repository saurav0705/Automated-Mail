import json


data = json.load(open(r'C:\\Users\\saurav.aggarwal\\Desktop\\credential.json'))

def getDetails(user):
    return data[user]
