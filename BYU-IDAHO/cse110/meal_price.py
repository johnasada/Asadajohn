child_meal=(input(f"What is the price of a child's meal? "))
child_drinks=(input(f"What is the price for a child's drink? "))
adult_meal=(input(f"What is the price of an adult's meal? "))
adult_drinks=(input(f"What is the price for a adults drink? "))
children=int(input("How many children are there? "))
adults=int(input("How many adults are there? "))
tax=(input(f"What is the sales tax rate? "))
print()# This is to print a blank space
number_of_children=(2)
price_per_childs_meal=(2.25)
price_per_childs_drink=(1.25)
total_for_children=(float(number_of_children * price_per_childs_meal * price_per_childs_drink))
number_of_adult=(1)
price_per_adult_meal=(6.99)
price_per_adult_drink=(1.25)
total_for_adult=(float(number_of_adult * price_per_adult_meal * price_per_adult_drink))
subtotal=(float(total_for_children + total_for_adult))
print(f"Subtotal: {subtotal}")

