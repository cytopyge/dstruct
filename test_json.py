import json
setName = 'settings.json';

def getSettings():
    json_data = open(setName)
    datOut = json.load(json_data)
    json_data.close()
    return datOut

def saveSettings():
    a_dict = {'new_key': 'new_value'}
    with open(setName) as f:
        data = json.load(f)
    data.update(a_dict)
    with open(setName, 'w') as f:
        json.dump(data, f)

# --> saving settings
saveSettings()


# --> getting settings
# data = getSettings()
# print(data["port1"])
