"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
------
"""

#Collect Data
age = int(input("Please enter your age: ")) 

#Determine Price
if age < 1:
    price = 0.00
elif 1 <= age <= 11:
    price = float(age) * 1.00
elif 12 <= age <= 64:
    price = 16.95
else:  # age 65 and older
    price = 12.95       

#Output Result
print(f"The price for your buffet is: ${price:,.2f}")   