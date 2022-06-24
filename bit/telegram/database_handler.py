import json

def get():
    with open('database.json', 'r') as ur:
        return json.load(ur)

def set(data: dict):
    with open('database.json', 'w') as uw:
        json.dump(data, uw)