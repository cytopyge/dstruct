import json

def getSettings():
    json_data=open('settings.json')
    json_data.close()
    return json.load(json_data)

data = getSettings();

print(data)
