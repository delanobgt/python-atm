import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def __load_json():
    array = None
    with open('db/rekening.json', 'r') as f:
        array = json.load(f)
    return array

def __save_json(data):
    with open('db/rekening.json', 'w') as f:
        json.dump(data, f, indent=4)

def find_one_by_id(id):
    rekenings = __load_json()
    for rek in rekenings:
        if rek['id'] == id:
            return rek

def update_one_by_id(id, updated_rek):
    old_rekenings = __load_json()
    new_rekenings = []
    for rek in old_rekenings:
        if id == rek['id']: new_rekenings.append(updated_rek)
        else: new_rekenings.append(rek)
    __save_json(new_rekenings)
