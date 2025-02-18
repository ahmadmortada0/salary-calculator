salary_amount=int(input("Salary amount :"))
salary_month=input("The name of the month to store the salary :")
salary_taxs=[]
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
sum = 0 
for i in range (len(salary_taxs)):

    if i == 0 :
        print (f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the savings ")
    elif i ==1:
        print (f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the rent ")
    else :
        print(f"the amount for the month {salary_month} is {int(salary_amount*salary_taxs[i]/100)} for the electricty ")

