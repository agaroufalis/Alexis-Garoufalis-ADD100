"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Soup-O-Ramen POS (V1.0)
Developer: Alexis Garoufalis
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"

def get_customer_info():
    """if here"""
    """Asks for table and seat #"""
    # TODO: Ask for table, seat# 
    return "173"
    """if to go"""
    """customer name"""
    # TODO: Ask for customer name
    return "#173"


def take_order():
    """Collects category, size, base, add-ons apps, drinks. Returns data."""
    # TODO: Capture category (Ramen/Drinks/Apps) and each item in each category
    return "Ramen" "Large" "White Miso"

def edit_order():
    """input order number"""
    """print existing order"""
    """call take_orders"""
    # TODO append edits to existing order
    pass


def calculate_total(order_data):
    """Calculates price based on user order."""
    # TODO: Load prices from menu.txt
    return 2.30

def save_data_and_label(customer, total):
    """Appends to order_history.txt and prints the human-readable label."""
    # TODO: Write raw data for computer and formatted box for barista
    pass

def main():
    # 1. Identity Phase
    order_number = get_customer_info()
    
    # 2. Data Collection Phase
    current_order = take_order()

     # 2. Possible Data Editing Phase
    current_order = edit_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase
    save_data_and_label(order_number, final_price)

main()