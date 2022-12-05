#Accept the item code, description, qty and price of an item. Compute the total for the item.
# • Accept the user’s choice. If the choice is ‘y’ then accept the next set of inputs for a new item and compute the total.
# • In this manner, compute the grand total for all the items purchased by the customer.
# o If the grand total is more than Rs. 10,000/- then, the customer is allowed a discount of 10%.
# o If the grand total is less than Rs. 1,000/- and the customer chooses to pay by card, then a surcharge of 2.5% is levied on the grand total.
# • Display the grand total for the customer.


def main():
		total = 0
		while True:
				code = input("Enter the item code: ")
				desc = input("Enter the item description: ")
				qty = int(input("Enter the quantity: "))
				price = float(input("Enter the price: "))
				item_total = qty * price
				total += item_total
				print("The total for the item is: ", item_total)
				choice = input("Do you want to continue? (y/n): ")
				if choice == 'n':
						break
		if total > 10000:
				total = total - (total * 0.1)
		elif total < 1000:
				total = total + (total * 0.025)
		print("The grand total is: ", total)
main()