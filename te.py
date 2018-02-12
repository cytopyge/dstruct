import json

def saveValue(a_dict):
    with open('test.json') as f:
        data = json.load(f)
    data.update(a_dict)
    with open('test.json', 'w') as f:
        json.dump(data, f)

def giveAll():
    with open('test.json') as f:
        data = json.load(f)
    return data

def getValue(val):
    with open('test.json') as f:
        data = json.load(f)
    return data[val]

saveValue({'port1': 'ccccc'})
# print(giveAll())

print(getValue("ouwe_key"))
