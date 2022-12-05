#Special allowances are 25% of basic, 70 percentage of basic as bonus and monthly tax saving investments.
# • The gross monthly salary is basic + special allowances.
# • Compute the annual salary. The gross annual salary also includes the bonus.
# • Compute the annual net salary, by deducting taxes as suggested.
# o Income up to 1 lac – exempted
# o Income from 1 to 1.5 lac – 20%
# o Income from 1.5 lac onwards – 30%
# o However, if there is any tax saving investment, then there is further exemption of up to 1 lac annually. This would mean that by having tax saving investments of about 1 lac an income of 2 lacs is non-taxable.
# • Display the annual gross, annual net, and tax payable.
basic=27083
special_allowances=0.25*basic
bonus=0.7*basic
monthly_tax_saving_investments=0

gross_monthly_salary=basic+special_allowances
print("Gross monthly salary is",gross_monthly_salary)
annual_salary=12*(gross_monthly_salary+bonus)

if monthly_tax_saving_investments>100000:
		monthly_tax_saving_investments=100000
		annual_tax_saving_investments=12*monthly_tax_saving_investments
else:
	annual_tax_saving_investments=12*monthly_tax_saving_investments


print("Annual tax saving investments is",annual_tax_saving_investments)
annual_salary=annual_salary+bonus-(annual_tax_saving_investments)
print("Annual salary is",annual_salary)


tax=0
if annual_salary<=100000:
		tax=0
elif annual_salary<=150000:
		tax=0.2*(annual_salary-100000)
else:
		tax=0.2*50000+0.3*(annual_salary-150000)
	

annual_net_salary=annual_salary-tax
print("Annual Gross Salary:",annual_salary)
print("Annual Net Salary:",annual_net_salary)
print("Tax Payable:",tax)



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

