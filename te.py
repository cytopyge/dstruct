import json

def saveValue():
    a_dict = {'ouwe_key': 'bbbbbbbbbbbbb'}
    with open('test.json') as f:
        data = json.load(f)
    data.update(a_dict)
    with open('test.json', 'w') as f:
        json.dump(data, f)

def giveAll():
    a_dict = {'ouwe_key': 'bbbbbbbbbbbbb'}
    data = ""
    with open('test.json') as f:
        data = json.load(f)
    return data


saveValue()
print(giveAll())
