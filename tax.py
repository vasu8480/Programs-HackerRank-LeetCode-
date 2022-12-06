#Special allowances are 25% of basic, 70 percentage of basic as bonus and monthly tax saving investments.
# • The gross monthly salary is basic + special allowances.
# • Compute the annual salary. The gross annual salary also includes the bonus.
# • Compute the annual net salary, by deducting taxes as suggested.
# o Income up to 1 lac – exempted
# o Income from 1 to 1.5 lac – 20%
# o Income from 1.5 lac onwards – 30%
# o However, if there is any tax saving investment, then there is further exemption of up to 1 lac annually. This would mean that by having tax saving investments of about 1 lac an income of 2 lacs is non-taxable.
# • Display the annual gross, annual net, and tax payable.


#Algorithm
# Step 1: Start
# Step 2: Read name, employee Id,basic, tax_saving_investments
# Step 3: special_allowances = 25% of basic, bonus = 70% of basic
# Step 4: Calculate gross monthly salary= basic + special_allowances
# Step 5: calculate annual salary= 12* gross monthly salary
# Step 6: If Yearly_tax_saving_investments < 100000 then Yearly_tax_saving_investments=monthly_tax_saving_investments*12
# Step 7: Else Yearly_tax_saving_investments=100000
# Step 8: Calculate annual salary=annual_salary+bonus-annual_tax_saving_investments
# Step 9: If annual_salary<=100000 then tax=0
# Step 10: Else if annual_salary<=150000 then tax=0.2*annual_salary
# Step 11: Else tax=0.2*150000+0.3*(annual_salary-150000)
# Step 12: Calculate annual_net_salary=annual_salary-tax
# Step 13: Caculate annual_gross_salary=annual_salary+tax+annual_tax_saving_investments
# Step 14: Calculate annual_net_salary=annual_salary
# Step 15: Display name, employee Id, gross monthly salary, annual salary, annual net salary, tax payable
# Step 16: Stop



Basic_Salary=27083

special_allowances=0.25*Basic_Salary
bonus=0.7*Basic_Salary
monthly_tax_saving_investments=5000

gross_monthly_salary=Basic_Salary+special_allowances
annual_salary=12*(gross_monthly_salary+bonus)

Yearly_tax_saving_investments=monthly_tax_saving_investments*12

if Yearly_tax_saving_investments>=100000:
		Yearly_tax_saving_investments=100000
		annual_tax_saving_investments=Yearly_tax_saving_investments
else:
	annual_tax_saving_investments=Yearly_tax_saving_investments

annual_salary=annual_salary+bonus-(annual_tax_saving_investments)

#print("Annual Salary is",annual_salary)
tax=0
if annual_salary<=100000:
	tax=0
elif annual_salary<=150000:
	tax=0.2*(annual_salary-100000)
else:
	tax=0.2*(50000)+0.3*(annual_salary-150000)


annual_salary=annual_salary-tax
annual_gross_salary=annual_salary+tax+annual_tax_saving_investments
annual_net_salary=annual_salary

print("Annual Gross Salary is:",annual_gross_salary)
print("Annual Net Salary:",annual_net_salary)
print("Tax Payable:",tax)