"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00

# TODO: Define blend(size, base, fruit, scoops)

def blend(size, base, fruit, scoops):
    print("\n--- Blending Order ---")
    print(f"Size: {size}")
    print(f"Base: Smoothie with {base} base.")
    print(f"Fruits: {scoops} scoops of {fruit}.")

def check_errors(variable, user_input):
    if variable == "choice_size":
        if user_input not in SIZES:
            choice_size = input("Size (Small/Medium/Large): ").title().strip()
    elif variable == "choice_base":
        if user_input not in BASES:
            print("Please choose from the bases listed")
            choice_base = input("Select Base (Water/Apple Juice/Orange Juice/Milk): ").title().strip()
    elif variable =="choice_fruit":
        if user_input not in FRUITS:
            print("Please choose from the fruits listed")
            choice_fruit = input("Select Fruit (Strawberry/Banana/Mango/Blueberry): ").title().strip()


# TODO: Define main() to collect input and call your logic

# Really this needs a loop to check for user error when they answer their choices 
# but that doesn't appear to be a part of this assignment
 
def main():
    print("Welcome to Smoothie Station")
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input("Select Base (Water/Apple Juice/Orange Juice/Milk): ")
    choice_fruit = input("Select Fruit (Strawberry/Banana/Mango/Blueberry): ")
    try:
        scoops= int(input("How many scoops? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        scoops = 1

    # Store the result from the return statement
    cost = get_price(choice_size)
    
    # Call the blend function
    blend(choice_size, choice_base, choice_fruit, scoops)
    
    print(f"Total Bill: ${cost:.2f}")

# Run the system
main()