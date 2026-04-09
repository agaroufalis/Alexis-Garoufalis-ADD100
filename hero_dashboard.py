"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

# Global Constants
OFFICE_NAME = "Office Hero HQ"
TAX_RATE = 0.05

# Returns TWO values (float, string)
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


def main():
    print(f"Welcome to {OFFICE_NAME} Expense Dashboard")

    item_name = input("Enter item name: ")

    # Input validation with try/except
    try:
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Error: Please enter valid numeric values for price and quantity.")
        return

    # Call function using KEYWORD arguments
    total, summary = process_expenses(
        item_name=item_name,
        price=price,
        quantity=quantity
        )

    # Print both returned values
    print(summary)
    print(f"Final Total (returned): ${total:.2f}")


# Run the program

main()


   