#Accept the item code, description, qty and price of an item. Compute the total for the item.
# • Accept the user’s choice. If the choice is ‘y’ then accept the next set of inputs for a new item and compute the total.
# • In this manner, compute the grand total for all the items purchased by the customer.
# o If the grand total is more than Rs. 10,000/- then, the customer is allowed a discount of 10%.
# o If the grand total is less than Rs. 1,000/- and the customer chooses to pay by card, then a surcharge of 2.5% is levied on the grand total.
# • Display the grand total for the customer.

# Step 1: Start
# Step 2: Accept the item code, description, qty and price of an item.
# Step 3: Compute the total for the item.
# Step 4: Accept the user’s choice.
# Step 5: If the choice is ‘y’ then accept the next set of inputs for a new item and compute the total.
# Step 6: In this manner, compute the grand total for all the items purchased by the customer.
# Step 7: If the grand total is more than Rs. 10,000/- then, the customer is allowed a discount of 10%.
# Step 8: If the grand total is less than Rs. 1,000/- and the customer chooses to pay by card, then a surcharge of 2.5% is levied on the grand total.
# Step 9: Display the grand total for the customer.
# Step 10: Stop

def Customer():
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
		card_payment=input("Do you want to pay by card? (y/n): ")
		if total > 10000:
				total = total - (total * 0.1)
		elif total < 1000 and card_payment == 'y':
				total = total + (total * 0.025)
		else :
			total = total
		print("The grand total is: ", total)
Customer()