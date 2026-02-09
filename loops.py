"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
there_yet = False
while there_yet == False:
    print(there_yet)
    answer = input("Are we there yet? (yes/no): ")
    if answer == "yes":
        there_yet = True


for i in range(99,0,-1):
    if i > 1:
        print(f"{i} bottles of beer on the wall!")
    else:
        print(f"{i} bottle of beer on the wall!")
    