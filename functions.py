import json

def openFile(file):
    with open(f'{file}.json') as file:
        data = json.load(file)
    
    if data: return data # return data if data found
    else: return None # if no data found return None

def writeToFile(file, data):
    with open(f'{file}.json', 'w') as file:
        json.dump(data, file)
    return True


def NewPatient(model_number, dcm_number, institution):
    device_details = openFile("global")

    device_details['ModelNumber'] = model_number
    device_details['DCMNumber'] = dcm_number
    device_details['Institution'] = institution

    return writeToFile("global", device_details)

def save(variable, value):
    variable = value


# # TEST CASES
# print(login("user7", "400316748")) # false user
# print(login("elmongya", "400316748")) # real user
# print(register("user8", "number8")) # new user
# print(login("user8", "number8")) # checking new user
print(NewPatient("1", "2", "3"))
