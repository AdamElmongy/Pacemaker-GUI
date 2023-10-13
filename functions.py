import json

def openFile(file):
    with open(f'{file}.json', 'r') as file:
        data = json.load(file)
    
    if data or data == []: return data # return data if data found
    else: return None # if no data found return None

def writeToFile(file, data):
    with open(f'{file}.json', 'w') as file:
        json.dump(data, file)
    return True

def getCurrentUser():
    return openFile("global")['CurrentUser']

def setCurrentUser(user):
    data = openFile("global")
    data['CurrentUser'] = user
    return writeToFile("global", data)







# # TEST CASES
# print(login("user7", "400316748")) # false user
# print(login("elmongya", "400316748")) # real user
# print(register("user8", "number8")) # new user
# print(login("user8", "number8")) # checking new user
