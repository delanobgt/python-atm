import json

with open('db/rekening.json', 'r') as file:
    obj = json.load(file)
    print (obj)
