"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""


# Global constant TOPPINGS defined as a Tuple in ALL_CAPS
TOPPINGS = ("Pepperoni", "Mushrooms", "Onions")

#Function 'make_pizza' defines 4 specific parameters.
#'make_pizza' uses a DEFAULT value for is_delivery
def make_pizza(customer, topping, pizza_size, is_delivery = False):
 
    print(f"PIZZA ORDER: {customer}")
    print(f"Pizza: {pizza_size} with {topping}")
    
    if is_delivery:
        print("Order Type: Delivery ")
    else:
        print("Order Type: Pickup")

def main():
    
    #Collect user input
    user = input("Customer Name: ").title()

    #Display the Global Pantry list to the user
    print(f"Options: {TOPPINGS}")
    choice = input("Select Topping: ").title()
    while choice not in TOPPINGS:
        print("Please choose a valid topping.")
        choice = input("Select Topping: ").title()
    size = input("Select Size (Small/Medium/Large): ").title()
    
    try:
        delivery_input = input("Delivery? (yes/no): ").lower()
        delivery = True if delivery_input == "yes" else False
    except:
        print("Invalid input. Defaulting to pickup.")
        delivery = False

    # Keyword Handoff
    make_pizza(customer = user, topping = choice, pizza_size = size, is_delivery = delivery)

main()
