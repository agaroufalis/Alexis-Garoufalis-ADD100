"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

#Collect variables
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter a second integer: "))

#logic checks - both greater than x
if num1 > 100 and num2 > 100:
    print("Both integers are greater than 100")
elif num1 > 0 and num2 > 0:
    print("Both integers are greater than 0")

#logic checks - either even
if num1 % 2 == 0 and num2 % 2 == 0:
    print ("Both integers are even")
elif num1 % 2 == 0 or num2 % 2 == 0:
    if num1 % 2 == 0:
        print("Integer 1 is even and integer 2 is odd")
    else:
        print("Integer 2 is even and integer 1 is odd")
else:
    print("Both integers are odd")  

#logic checks - either greater that 100
if not (num1 >100 and num2 > 100):
    if num1 >100 or num2 > 100:
        if num1 > 100:
            print("Integer 1 is greater than 100 and integer 2 is less than 100")
        else:
            print("Integer 2 is greater than 100 and integer 1 is less than 100")

#logic checks - not equal
if not (num1 == num2): 
    print("Integer 1 is not equal to integer 2")

#logic checks - not 0
if num1 != 0 and num2 != 0:
    print("Both integers are not equal to 0")
elif num1 != 0 or num2 != 0:
    if num1 != 0:
        print("Integer 1 is not equal to 0")
    else:
        print("Integer 1 is not equal to 0")

#Categorize num1
category = ""
if num1 > 0:
    category = "a positive number"    
elif num1 == 0:
    category = "equal to 0"
else: 
    category = "a negative number"
print(f"Integer 1 is {category}")
