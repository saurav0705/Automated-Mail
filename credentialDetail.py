import json


data = json.load(open(r'credential.json'))

def getDetails(user):
    return data[user]

print(getDetails('username'))
