import json
import requests


def store_api(params):
    URL = 'http://127.0.0.1:5000/storeapi/output'
    r = requests.post(url=URL, json=params)
    res = json.loads(r.text)
    print("store_api response:- ", res)
    return res


params = {"data": [{
    "item": "Classical Songs Collection",
    "itemCategory": "Music",
    "quantity": 1,
    "price": 500
},
    {
        "item": "Pants",
        "itemCategory": "Clothes",
        "quantity": 2,
        "price": 1200
    }]}
# params = json.dumps(params)
output = store_api(params)
print(output)
