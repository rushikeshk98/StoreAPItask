from task1 import store_api
# params = [{
#     "item": "Classical Songs Collection",
#     "itemCategory": "Music",
#     "quantity": 1,
#     "price": 500
# },
#     {
#         "item": "Pants",
#         "itemCategory": "Clothes",
#         "quantity": 2,
#         "price": 1200
#     }
# ]

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

result = store_api(params)
print(result)