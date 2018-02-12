import json

json_data=open('settings.json')

data = json.load(json_data)


json_data.close()

print(data['port1'])
