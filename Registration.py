"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Validate First and Last Name (Cannot be blank)

name = input("Please enter a first and last name: ")
while name == "":
        print("❌ Error: Answer cannot be blank.")
        name = input("Please enter a first and last name: ")

print(f"✅ Thank you {name}.")

# Validate chaperone (must be y or n)

chaperone = input("Do you have a chaperone? (y/n): ").upper() 
while chaperone != "Y" and chaperone != "N":
        if chaperone == "":
             print("❌ Error: Answer cannot be blank.")
             chaperone = input("Do you have a chaperone? (y/n): ").upper() 
        else: 
              print("❌ Error: Answer must be Y or N.")
              chaperone = input("Do you have a chaperone? (y/n): ").upper() 

if chaperone =="Y":
    print(f"✅ Confirmed, you have a chaperone.")
else:
     print(f"✅ Confirmed, you don't have a chaperone.")

#Validate phone number (cannot be blank)

phone = input("Please enter your phone number: ")
while phone == "":
        print("❌ Error: Answer cannot be blank.")
        phone = input("Please enter your phone number: ")

print(f"✅ Thank you, your phone number is confirmed as: {phone}.")

# Validate Ticket Count (Must be an Integer)

ticket_count = 0
while True:
    try:
        ticket_count = int(input("How many tickets? "))
        if ticket_count > 0:
            break 
        print("❌ Error: Must be at least 1 ticket.")
    except ValueError:
        print("❌ Error: Please enter a NUMBER (e.g., 5, not 'five').")

print(f"✅ Ordered {ticket_count} tickets.")