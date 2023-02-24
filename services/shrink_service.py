import json
import string
import random

url_len = 7


def shrink_url(url):
    res = ''.join(random.choices(string.ascii_letters, k=url_len))

    file_data = open("./db.json")
    data = json.load(file_data)
    if res in data:
        while res not in data:
            res = ''.join(random.choices(string.ascii_letters, k=url_len))

    data[res] = url
    new_data = json.dumps(data, indent=4)
    # print(data)

    with open("db.json", 'w') as db:
        db.write(new_data)
    return "https://cho-ti.onrender.com/" + res
