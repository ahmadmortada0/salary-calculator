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


detail =-1
while detail !=0:
    display = int(input("If you want to display all the infos now please press 1 :"))
    if display==1:
        print(f"the details for {salary_month} ")
        print("1 for salary before taxs")
        print("2 for salary after taxs")
        print("3 for savings amount")
        print("4 for electricity amount ")
        print ("5 for rent amount")
        print ("6 for taxs amount")
        print ("7 for rent and electricty for a year")
        print ("8 for salary power 2")
        print ("9  for saving before additional")
        print ("10 for all")
        print ("0 for quit")
        detail=int(input("choose a number to display :"))
        if detail ==1:
            print (f"the salary before tax is = {salary_amount}")
        elif detail==2:
            print (f"the salary after tax is = {remainder} and without the additional saving is = {remainder+extra}")
        elif detail==3:
            print (f"the savings is = {savings_amount}")
        elif detail==4:
            print (f"the electricty is = {electricty_amount}")
        elif detail==5:
            print (f"the rent is = {rent_amount}")
        elif detail==6:
            print (f"the tax total is = {total}")
        elif detail==7:
            print (f"the annualy for rent  is = {yearly_rent} and for electricity is = {yearly_elec}")
        elif detail==8:
            print (f"the salary power 2  is = {salary_dream}")
        elif detail==9:
            print (f"the savings before additional saves  is = {savings_amount-extra}")
        elif  detail==10:
            print (f"the salary before tax is = {salary_amount}")
            print (f"the salary after tax is = {remainder} and without the additional saving is = {remainder+extra}")
            print (f"the savings is = {savings_amount}")
            print (f"the electricty is = {electricty_amount}")
            print (f"the rent is = {rent_amount}")
            print (f"the tax total is = {total}")
            print (f"the annualy for rent  is = {yearly_rent} and for electricity is = {yearly_elec}")
            print (f"the salary power 2  is = {salary_dream}")
            print (f"the savings before additional saves  is = {savings_amount-extra}")
        else :
            print ("we are finished here ")
            detail=0
    
        
      
        





