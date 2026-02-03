"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f).
-----------------------------------------------------------------------
"""

#Collect info
income = float(input("Please enter your monthly income: $"))
print("Please enter 5 expenses: ")
expense1 = float(input("Expense 1: $"))
expense2 = float(input("Expense 2: $"))
expense3 = float(input("Expense 3: $"))
expense4 = float(input("Expense 4: $"))
expense5 = float(input("Expense 5: $"))

#Calculate total values
total_expenses = expense1 + expense2 + expense3 + expense4 + expense5
percent_spent = total_expenses / income
remaining_balance = income - total_expenses

#Print results
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Remaining Balance: ${remaining_balance:,.2f}")
print(f"Percentage of Income Spent: {percent_spent:,.2%}")