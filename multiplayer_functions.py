# Function to ask the player if they want to start with X or O.
def start_symbol():
    start = input("Do you want to start with X or O?, type 'X' or 'O': ")
    start = start.upper()

    if start != 'X' and start != 'O':
        print("You have to type 'X' or 'O'")
        input_invalid = True

        # If the user gives wrong input then just going in a while loop until he gives the correct one.
        while input_invalid:
            start = input("Do you want to start with X or O?, type 'X' or 'O': ")
            start = start.upper()

            if start == 'X' or start == 'O':
                return start
    else:
        return start
