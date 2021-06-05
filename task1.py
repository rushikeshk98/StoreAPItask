from datetime import date, datetime
import json
def store_api(params):
    print(params)
    params = params["data"]
    total_price = []
    commodities = []
    receipt = {}
    commodities_details = []
    for i in params:
        temp = {}
        if i["itemCategory"] == "Medicine":
            tax = (5 / 100) * i["price"]
            total_amount = i["price"] + tax
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            temp["aplicable rate"] = "5%"
            temp["tax amount"] = total_amount
            commodities_details.append(temp)

        elif i["itemCategory"] == "Food":
            tax = (5 / 100) * i["price"]
            total_amount = i["price"] + tax
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            temp["aplicable rate"] = "5%"
            temp["tax amount"] = total_amount
            commodities_details.append(temp)

        elif i["itemCategory"] == "Imported":
            tax = (18 / 100) * i["price"]
            total_amount = i["price"] + tax
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            temp["aplicable rate"] = "18%"
            temp["tax amount"] = total_amount
            commodities_details.append(temp)

        elif i["itemCategory"] == "Book":
            total_amount = i["price"]
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            commodities_details.append(temp)

        elif i["itemCategory"] == "Music":
            tax = (3 / 100) * i["price"]
            total_amount = i["price"] + tax
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            temp["aplicable rate"] = "3%"
            temp["tax amount"] = total_amount
            commodities_details.append(temp)

        elif i["itemCategory"] == "Clothes":
            if i["price"] > 1000:
                tax = (12 / 100) * i["price"]
                total_amount = i["price"] + tax
                commodities.append(i["item"])
            else:
                tax = (5 / 100) * i["price"]
                total_amount = i["price"] + tax
            total_price.append(total_amount)
            commodities.append(i["item"])
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            temp["aplicable rate"] = "5%"
            temp["tax amount"] = total_amount
            commodities_details.append(temp)

        else:
            print("unknown item category for ", i['item'])
            total_amount = i["price"]
            temp["item"] = i["item"]
            temp["final price"] = i["price"]
            commodities_details.append(temp)
            total_price.append(total_amount)
            commodities.append(i["item"])

    bill_amount = sum(total_price)
    sorted_commodities_details = sorted(commodities_details, key=lambda i: i["item"], reverse=False)
    if bill_amount > 2000:
        discount = (5 / 100) * bill_amount
        total_paybale_amount = bill_amount - discount
    else:
        total_paybale_amount = bill_amount

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    receipt["Datetime"] = dt_string
    receipt["list of commodities"] = sorted_commodities_details
    receipt["total payble amount"] = total_paybale_amount
    output = json.dumps(receipt, indent=4)
    return output