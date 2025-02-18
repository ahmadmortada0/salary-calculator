salary_amount=int(input("Salary amount :"))
salary_month=input("The name of the month to store the salary :")
salary_taxs=[]
sum = 0 
for tax in range (3):
    if tax ==0:
        savings = int(input("Savings percentage :"))
        salary_taxs.append(savings)
    elif tax ==1:
        rent = int(input("Rent percentage :"))
        salary_taxs.append(rent)

    else :
        electricty = int(input("Electricity percentage :"))
        salary_taxs.append(electricty)
for i in range (len(salary_taxs)):

    if i == 0 :
        print (f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the savings ")
    elif i ==1:
        print (f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the rent ")
    else :
        print(f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the electricty ")
rent_amount=int(salary_amount*rent/100)
electricty_amount=int(salary_amount*electricty/100)
savings_amount=int(salary_amount*savings/100)
for i in salary_taxs:
    sum = sum +i 
total=int(salary_amount*sum/100)
print(f"the total of the taxs from the salary= {total}")
remainder=int(salary_amount-total)
print(f"the remainder  from the salary after taxs= {remainder}")
yearly_rent=rent_amount*12
yearly_elec=electricty_amount*12
for i in range(2):
    if i == 0:
         print (f"the anual amount of rent is {yearly_rent}")
    else:
         print (f"the anual amount of electricty is {yearly_elec}")
salary_dream=pow(salary_amount,2)
print(f"the salary would be = {salary_dream} ;)")
choose=int(input("do you want to save extra money if yes choose 1 :"))
if choose == 1:
    extra = int(input("how much would you like to save :"))
    if extra<=remainder:
        remainder=remainder-extra
    savings_amount=savings_amount+extra
    print(f"the remainder is = {remainder} and the savings is = {savings_amount} ")
    if extra>remainder:
        print("You dont have enough money for savings ")




