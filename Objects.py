"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object Practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class RamenOrder:
    def __init__(self, customer_name, drink, appetizer, ramen):
        # Private attributes with double underscores
        self.__customer_name = customer_name
        self.__drink = drink
        self.__appetizer = appetizer
        self.__ramen = ramen

    # =========================
    # GETTERS
    # =========================
    def get_customer_name(self):
        return self.__customer_name

    def get_drink(self):
        return self.__drink

    def get_appetizer(self):
        return self.__appetizer

    def get_ramen(self):
        return self.__ramen

    # =========================
    # SETTERS
    # =========================
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_drink(self, drink):
        self.__drink = drink

    def set_appetizer(self, appetizer):
        self.__appetizer = appetizer

    def set_ramen(self, ramen):
        self.__ramen = ramen

    # =========================
    # SUMMARY FUNCTION
    # ========================
    def get_summary(self):
        return (
            f"Customer: {self.__customer_name}\n"
            f"Drink: {self.__drink}\n"
            f"Appetizer: {self.__appetizer}\n"
            f"Ramen Order: {self.__ramen}\n"
        )

# =========================
# OBJECTs
# =========================

order1 = RamenOrder(
    "Alexis",
    "Ramune",
    "Takoyaki",
    ("Large", "White", "Hot", "Egg")
)

order2 = RamenOrder(
    "Jordan",
    "Sapporo",
    "Edamame",
    ("Small", "Shoyu", "Medium", "Corn")
)
# =========================
# PRINT SUMMARIES
# =========================

print(order1.get_summary())
print(order2.get_summary())