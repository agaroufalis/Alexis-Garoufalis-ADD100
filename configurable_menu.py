"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

MENU_FILE = "menu_config.txt"

#Phase 1: Use the menu creator sample to create a menu with at least 4 categories.

#Collects menu categories and items from the user
def get_menu_options():
    menu = {}

    while True:
        print("Type 'Q' when done")
        category = input("Enter a category: ").upper().strip()

        if category == "Q":
            break

        items = input("Enter items separated by commas: ").strip()
        menu[category] = items

    return menu

#Saves menu dictionary to a file using comma-separatd format
def save_to_file(menu):
    with open(MENU_FILE, "w") as file:
        for category, items in menu.items():
            file.write(f"{category},{items}\n")

#Reads the menu file and builds a dictionary.
def read_menu():
    
    menus = {}

    try:
        with open(MENU_FILE, "r") as file:
            for line in file:
                # Required parsing pipeline
                parts = line.strip().split(",", 1)

                category = parts[0].strip()
                items = parts[1].strip()

                menus[category] = items

    except FileNotFoundError:
        print("Error: menu_config.txt not found.")
        return {}

    return menus

#Breaks dictionary into individual category variables
def split_into_variables(menu_items):

    categories = {}
    for key in menu_items:
        categories[key] = menu_items.get(key, "")

    return categories

#Prints each category and its items 
def print_menu(categories):

    print("         MENU AUDIT")
    print("-" * 35)

    for category, items in categories.items():
        print(f"\n{category}")
        print("-" * 15)

        for item in items.split(","):
            print(f"* {item.strip()}")


def main():
    """Main program driver."""
    # Phase 1
    menu = get_menu_options()
    save_to_file(menu)

    # Phase 2
    menu_items = read_menu()

    if menu_items:  
        categories = split_into_variables(menu_items)
        print_menu(categories)


main()