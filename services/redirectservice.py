import json


def redirect_service(key):
    data = open("./db.json")
    data_json = json.load(data)
    if key in data_json:
        return data_json[key]
    else:
        return "Error"

