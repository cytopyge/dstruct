import json

class Store:
    #def __init__(self):
    def saveValue(self, a_dict):
        with open('test.json') as f:
            data = json.load(f)
        data.update(a_dict)
        with open('test.json', 'w') as f:
            json.dump(data, f)

    def giveAll(self):
        with open('test.json') as f:
            data = json.load(f)
        return data

    def getValue(self, val):
        with open('test.json') as f:
            data = json.load(f)
        return data[val]
