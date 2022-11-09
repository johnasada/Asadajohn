# ###################################################################### #
# File: cart.py                                                          #
# Author: John Asada                                        #
# Course: CSE 110 Intro to Programming                                   #
# Due Date: Sunday 14th March 2021 by 7:59AM                             #
# Purpose: To fulfil requirments for the Prove Assignment of W09 and W10 #
# ###################################################################### #

# creating the constants

cart = []
option = ""
total = 0
price_of_items = []
price = []

# Creating the Menu

while option != "5":
    print()
    print("Please select one of the following: ")
    menu = ["1. Add a new item", "2. view Cart", "3. Remove item",\
            "4. compute total", "5. Quit"]
    for item in menu:
        print(item)
    print()

    option = input("Please enter an action: ")
    print()

    if option != ("5"):
        if option == ("1") or option == ("add an item"):
            item = input("What item would you like to add? ").title()
            price = float(input(f"What is the price of '{item}'? $"))
            print(f"{item} has been added to the cart.")
            total += price

            # making it my own:
            # If an item is already in the cart it won't be added again
            # but rather adds the price to the old item

            if item not in cart:
                cart.append(item)
                price_of_items.append(price)
            else:
                ind = cart.index(item)
                price_of_items[ind] += price

        elif option == ("2"):
            print("The contents of the shopping cart are: ")
            for i in range(len(cart)):
                cart_item = cart[i]
                item_price = price_of_items[i]
                print(f"{i + 1}. {cart_item} -- -- -- ${item_price:.2f}")

        elif option == ("3"):
            # choice = 0
            # while len(cart) < choice:
            #     print("There's no such item")

            print("Items: ")

            # This is to show the available items
            # that the user can delete from
            for i in range(len(cart)):
                cart_item = cart[i]
                print(f"{i + 1}. {cart_item}")

            print("Enter item number ")
            choice = int(input("what item do you want to remove? "))
            choice1 = (choice - 1)
            price_removed = price_of_items[choice1]
            cart.pop(choice1)
            price_of_items.pop(choice1)
            total -= price_removed
            print(f"Item number {choice} has been successfully removed!")

        elif option == ("4"):
            print(f"The total is price is: {total:.2f}")

print("Thank you. Goodbye!")
