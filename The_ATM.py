"""
-----------------------------------------------------------------------
ASSIGNMENT 5B: The ATM
-----------------------------------------------------------------------
[ ] 1. Structure: Use match-case for the main menu.
[ ] 2. Input Validation: Use .isdigit() or similar logic to prevent crashes 
    if the user types text instead of numbers (since we are not using try-except yet)
[ ] 3. Math Safety: No overdrafts (withdrawing more than you have) and no negative deposits.
[ ] 4. Formatting: All currency must use :.2f.
-----------------------------------------------------------------------
"""
# I know we haven't learned functions yet, but it hurt to repeat the same lines of code so many times :(
# and I've been watching my coworkers write a python script to fix some bad data in our database
# and I wanted to try it :)


def error_Check(choice_type):
    while True: 
        try:
            amount = float(input(f"Enter an amount to {choice_type}: $"))
            if amount > 0: #input is a numerical value above 0
                break
        except ValueError:
            print("Please enter a valid numerical value.")

    return amount

print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
choice = input("Please choose an action (1-5): ")

balance = 1000
while True:
    match choice:
            case "1": #Balance
                print(f"Balance = ${balance:,.2f}")
                print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
                choice = input("Please choose an action (1-5): ") 

            case "2": #Deposit
                choice_type = "deposit"
                deposit = error_Check(choice_type)
                balance = balance + deposit
                print(f"Added ${deposit:,.2f} to balance. New balance is ${balance:,.2f}")
                print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
                choice = input("Please choose an action (1-5): ") 
            
            case "3": #Withdraw
                choice_type = "withdraw"
                withdraw = error_Check(choice_type)

                if (balance - withdraw) < 0:
                    print(f"Withdrawing ${withdraw:,.2f} will result in an overdraft.")
                    print(f"Please enter an amount less than ${balance:,.2f}")
                else:
                    balance = balance - withdraw
                    print(f"${withdraw:,.2f} was withdrawn from account. New balance is ${balance:,.2f}")
                    print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
                    choice = input("Please choose an action (1-5): ")

            case "4": #Transfer
                choice_type = "transfer"
                transfer = error_Check(choice_type)
                recipient = input(f"Who would you like to transfer ${transfer:,.2f} to? ")

                if recipient == "":
                    print(f"Please enter a valid name of the person you want to transfer ${transfer:,.2f} to.")
                    recipient = input(f"Who would you like to transfer ${transfer:,.2f} to? ")
                elif int(recipient.isdigit()) == True:
                    print(f"Hmmm.. I don't think that's a valid name. Please enter a valid name of the person you want to transfer ${transfer:,.2f} to.")
                    recipient = input(f"Who would you like to transfer ${transfer:,.2f} to? ")
                    
                if (balance - transfer) < 0:
                    print(f"transferring ${transfer:,.2f} will result in an overdraft.")
                    print(f"Please enter an amount less than ${balance:,.2f}")
                else:
                    balance = balance - transfer
                    print(f"${transfer:,.2f} was transferred from account to {recipient}. New balance is ${balance:,.2f}")
                    print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
                    choice = input("Please choose an action (1-5): ")
                    
            case "5": #Exit
                print("Goodbye")
                break
        
            case _: 
                print("Invalid Selection")
                print("Menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit")
                choice = input("Please choose an action (1-5): ")


