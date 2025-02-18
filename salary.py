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

