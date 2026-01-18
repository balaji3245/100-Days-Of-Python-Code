
# 🏧 Real-Life Task: ATM Withdrawal System

# Situation:
 # You go to an ATM to withdraw money.

# Rules:
   # If PIN is wrong → stop immediately
   # If balance is less than withdrawal amount → show insufficient balance
   # Else → allow withdrawal


# An ATM 
atm_balance = 50000    # available balance of ATM

pin=1234    # pin of card

person = float(input("Enter the Amount you want to Withdraw : "))    # A person comes and he enters the amount he want to withdraw





if atm_balance >= person :
    pin_card = float(input(" Enter your card PIN : "))

    if pin_card == pin :
        print(" withdraw succesful ")
    else:
        print("pin was WRONG try next time ")
else:
    print("Insufficient balance")




 



