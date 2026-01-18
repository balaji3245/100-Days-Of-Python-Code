# persons monthly salary

person = float(input("Enter your monthly salary : "))

# he's monthly expenses
rent = float(input("Enter your home Rent : "))
emi = float(input("Enter your total EMI : "))
daily_expenses = float(input("Enter your daily expences : "))

# Total expences (calculation)
Total_expenses = rent + emi + daily_expenses

# persons savaing 
saving = person - Total_expenses

# Total output
print("Person's monthly salary : ",person)   # monthly salary

print("persons Home Rent :",rent,
      "persons monthly EMI : ",emi,
      "persons Daily expenses : ",daily_expenses,            #persons expenses
        sep="\n"
        )

print("persons daily expenses : ",Total_expenses)    #persons Total expenses 

print("persons monthly saving : ",saving)     #persons monthly saving 