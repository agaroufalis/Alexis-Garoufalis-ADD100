"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

available_seats = list(range(1, 6))

while available_seats:
    print("Please enter an available seat number or type “0” to quit")
    print(f"available seats: {available_seats}")
	
    while True: 
        try:
            selected_seat = int(input("What seat would you like to select? "))
        except ValueError:
            print("Sorry! That is not a valid seat number.")
            print("Please enter an available seat number or type “0” to quit")
        if selected_seat < 20 and selected_seat >= 0: #input is a numerical non-negative value less than 20
            if selected_seat in available_seats:
                available_seats.remove(selected_seat)
                print(f"Seat {selected_seat} has been reserved for you")
                break
            elif selected_seat == 0:
                break
            else:
                print("Sorry! That is not a valid seat number.")
                print("Sorry! That seat is not available.")
        else:
            print("Please enter an available seat number or type “0” to quit")
print("There are no more seat available")