"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "Possibly", "Unable to predict", "Absolutely not","Of course")

print("Welcome to the Digital Oracle!")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop

while True:
    print("Ask a question of the Digital Oracle... (type 'quit' to exit)")
    question = input("What is your question? ")

    # If user types "quit", break the loop
    if question.lower() == "quit": 
        print("The Digital Oracle has spoken!")
        break

    # Use random.choice(RESPONSES) to answer
    answer = random.choice(RESPONSES)
    print( answer, "\n")
