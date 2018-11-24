import json

def __load_json():
    array = None
    with open('db/rekening.json', 'r') as f:
        array = json.load(f)
    return array

def find_one_by_id(id):
    rekenings = __load_json()
    for rek in rekenings:
        if rek['id'] == id:
            return rek

def find_one_by_key(keyName, key):
    rekenings = __load_json()
    for rek in rekenings:
        if rek[keyName] == key:
            return rek