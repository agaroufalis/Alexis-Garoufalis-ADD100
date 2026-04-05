"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""
from datetime import datetime
VALID_PRIORITIES = ("high", "medium", "low")


while True:
    choice = input("Enter 'log' to record a bug, or 'quit' to stop: ").lower().strip()

    if choice == "quit":
        print("Bug log updated!")
        break

    elif choice == "log":
        # Gather data
        file_name = input("File name: ")
        description = input("Description of error: ")
        while True:
            priority = input("Priority (High, Medium, Low): ").lower()
            if priority in VALID_PRIORITIES:
                priority = priority.title()  
                break
            else:
                print("Invalid priority. Please enter High, Medium, or Low.")

        # Create timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store in dictionary
        bug_entry = {
            timestamp: [file_name, description, priority]
        }

        # Append to file
        with open("bug_log.txt", "a") as file:
            for time, details in bug_entry.items():
                file.write(f"""
                [{time}]
                File: {details[0]}
                Description: {details[1]}
                Priority: {details[2]}
                --------------------------------------------------
                """)

    else:
        print("Invalid input. Please enter 'log' or 'quit'.")

