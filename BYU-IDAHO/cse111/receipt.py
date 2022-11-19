# ###################################### #
# ###################################### #
# File: receipt.py                       #
# Author: John Asada       #
# Purpose: A Milestone Assignment        #
# Course: CSE111                         #
# ###################################### #

import csv
from datetime import datetime
import sys, os
def main():
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    shop_name = "John's Groceries "
    time = datetime.now()
    time = f"{time:%A %I:%M %p}"
    tax = round(6/100, 4)

    products = read_products("products.csv", PRODUCT_INDEX)
    rec = process_request("request.csv", PRODUCT_INDEX)
    
    print(f"{shop_name}\n")
    ordered = get_ordered_items(products, rec)
    total_price = 0
    for (name, quantity, price) in ordered:
        total_price += price
        print(f"{name}: {quantity} @ {price}")
    total = round(total_price + (total_price * tax), 2)
    print()
    print(f"Number of items: {len(ordered)}")
    print(f"Subtotal: {total_price}")
    print(f"Sales tax: {tax}")
    print(f"Total: {total}")

    print()
    print(f"Thanks for shoping with {shop_name}")

    print()
    print(time)


def get_ordered_items(products, request):
    results = []
    for key in request.keys():
        product = products.get(key, False)
        if product is not False:
            name = product[0]
            price = float(product[1])
            item_amount = int(request[key][0])
            total_price = price*item_amount
            results.append((name, item_amount, total_price))
    return results

    pass

    
    
def read_products(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename,"rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row[key_column_index+1:]
    except FileNotFoundError:
        print("Product list not found --> Exiting...")
        sys.exit(0)
    except PermissionError:
        print("We are not allowed to access the product's catalogue. --> Exiting...")
        sys.exit(0)
            
    return dictionary

def process_request(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row[key_column_index+1:]
    except FileNotFoundError:
        print("Request list not found. --> Exiting...")
        sys.exit(0)
    except PermissionError:
        print("We are not allowed to access the request list. --> Exiting...")
        sys.exit(0)
    return dictionary

if __name__ == "__main__":
    main()
