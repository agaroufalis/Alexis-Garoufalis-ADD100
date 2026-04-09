"""
ASSIGNMENT 10B: SPRINT 3 - FUNCTIONAL STUBS
Project: Soup-O-Ramen POS (V1.0)
Developer: Alexis Garoufalis
"""

import datetime

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"
ORDER_TYPE = ("New", "Edit", "Cancel")
ORDER_CATEGORY = ("Drinks", "Apps", "Ramen")

class Orders:
    def __init__(order, place, drinks=None, apps=None, ramen=None):
        order.place = place
        order.drinks = drinks
        order.apps = apps
        order.ramen = ramen

    def __str__(order):
        return (f"Place: {order.place} \nDrinks: {order.drinks} \nApps: {order.apps} \nRamen: {order.ramen}")

    def calculate_total(order, prices):
        total = 0
        if order.drinks in prices:
            drinks_subtotal += prices[order.drinks]
        if order.drinks in prices:
            apps_subtotal += prices[order.apps]
        if order.drinks in prices:
            ramen_subtotal += prices[order.ramen]
        total = drinks_subtotal + apps_subtotal + ramen_subtotal
        return total
    

def process_expenses(item_name, price, quantity):

    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    final_total = subtotal + tax

    summary = (
        f"\n--- Expense Summary ---\n"
        f"Item: {item_name}\n"
        f"Price: ${price:.2f}\n"
        f"Quantity: {quantity}\n"
        f"Subtotal: ${subtotal:.2f}\n"
        f"Tax (5%): ${tax:.2f}\n"
        f"Total: ${final_total:.2f}\n"
    )

    return final_total, summary

# Select the order type to determine the operation to be preformed
def get_order_type():
    
    order_type = input("Order Type (New/Edit/Cancel): ").title()
    while order_type not in ORDER_TYPE:
        print("Please choose a valid option.")
        order_type = input("Order Type (New/Edit/Cancel): ").title()
    return order_type


def get_customer_info(orders):
    order_number = 100
    if order_number in orders:
        last_order = list(orders)[-1]
        order_number = last_order + 1
    else:
        order_number = 100

    place = input("Is this order for (1)here or (2)to-go? ")

    if place == "1":
        table = input("Please enter table number: ")
        seat = input("Please enter seat number: ")
        setting = (f"t{table}s{seat} ")
        # TODO: add error checking
        orders[order_number]=Orders(setting)
        return order_number
    
    if place =="2":
        name = input("Please enter customer name: ")
        orders[order_number]=Orders(name)
        return order_number

def take_order(order_number, orders):
    cat = input("Order Category (Drinks/Apps/Ramen): ")

    orders[order_number].drinks= input("Drinks (Ramune/Sake/Sapporo/None): ").title

    orders[order_number].apps = input("Appetizers (Karrage/Edamame/Tempura/Takoyaki): ").title

    size = input("1. Size (Small/Large): ").title
    base = input("2. Base (White/Red/Shoyu): ").title
    spice = input("3. Spice (Mild/Medium/Hot): ").title
    add_ons = input("4. Add-ons (Bean Sprouts/Naruto/Soft-Boiled Egg/Sweet Corn): ").title
    orders[order_number].ramen = (size, base, spice, add_ons)
     # TODO: add error checking

def edit_order(order_number, orders):
    
    print(f"Editing order: {order_number}")
    print(f"Current order: \n{orders[order_number]}")      
    """call take_orders"""
    # TODO append edits to existing order
    

def load_prices(MENU_FILE):
    prices = {}
    return total
    # TODO: load prices into dictionary


def save_data_and_label(order, order_number,total, prices):
    """Appends to order_history.txt and prints the human-readable label."""
    # TODO: Write raw data for computer 
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n--- RECEIPT ---")
    print(f"Order #: {order_number}")
    print(f"Drinks: {order.drinks}")
    print(f"Apps: {order.apps}")
    print(f"Ramen: {order.ramen}")
    print(f"Total: ${total:.2f}")

    with open("store_receipts.txt", "a") as file:
        file.write(f"\n[{current_time}] ORDER: {order_number}\n")
        
        for item, in order.items():
            file.write(f" - {item}:\n")
            
        file.write("----------------------\n")
    
    print("Receipt successfully logged to system!")
    

def main():
    orders = {}
    # 1. Identity Phase
    order_number = get_customer_info(orders = orders)
    
    # 2. Data Collection Phase
    current_order = take_order(order_number = order_number, orders = orders)

     # 2. Possible Data Editing Phase
    current_order = edit_order(order_number = order_number, orders = orders)

    # 3. Calculation Phase
    final_price = load_prices(MENU_FILE, current_order = current_order)

    # 4. Handoff Phase
    save_data_and_label(order_number = order_number, final_price = final_price)

main()


