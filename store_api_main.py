from datetime import date, datetime
import json


# API to compute the taxes and the final bill amount
def store_api(params):
    try:
        if type(params) == dict:  # To check the type of input params
            params = params["data"]
        total_price_with_tax = []  # total price including tax of each items
        commodities = []  # List of items purchased
        receipt = {}
        commodities_details = []  # it contains each item with it's final price, applicable rate and taxable amount
        for i in params:
            temp = {}
            # conditions for various item categories
            if i["itemCategory"] == "Medicine":
                tax = (5 / 100) * i["price"]
                total_amount = i["price"] + tax
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                temp["applicable rate"] = "5%"
                temp["tax amount"] = total_amount
                commodities_details.append(temp)

            elif i["itemCategory"] == "Food":
                tax = (5 / 100) * i["price"]
                total_amount = i["price"] + tax
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                temp["applicable rate"] = "5%"
                temp["tax amount"] = total_amount
                commodities_details.append(temp)

            elif i["itemCategory"] == "Imported":
                tax = (18 / 100) * i["price"]
                total_amount = i["price"] + tax
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                temp["applicable rate"] = "18%"
                temp["tax amount"] = total_amount
                commodities_details.append(temp)

            elif i["itemCategory"] == "Book":
                total_amount = i["price"]
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                commodities_details.append(temp)

            elif i["itemCategory"] == "Music":
                tax = (3 / 100) * i["price"]
                total_amount = i["price"] + tax
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                temp["applicable rate"] = "3%"
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
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                temp["applicable rate"] = "5%"
                temp["tax amount"] = total_amount
                commodities_details.append(temp)

            else:
                print("unknown item category for ", i['item'])
                total_amount = i["price"]
                temp["item"] = i["item"]
                temp["final price"] = i["price"]
                commodities_details.append(temp)
                total_price_with_tax.append(total_amount)
                commodities.append(i["item"])

        bill_amount = sum(total_price_with_tax)  # total bill amount of all items
        # sorted receipt by items names
        sorted_commodities_details = sorted(commodities_details, key=lambda i: i["item"], reverse=False)
        if bill_amount > 2000:  # condition for discount
            discount = (5 / 100) * bill_amount
            total_payable_amount = bill_amount - discount
        else:
            total_payable_amount = bill_amount

        # time of receipt issued
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        receipt["Datetime"] = dt_string
        receipt["list of commodities"] = sorted_commodities_details
        receipt["total payable amount"] = total_payable_amount
        output = json.dumps(receipt, indent=4)
        return output
    except Exception as e:
        print(e)
        return {"success": False, "error": e}
