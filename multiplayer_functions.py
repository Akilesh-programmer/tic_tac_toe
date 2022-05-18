# Function to ask the player if they want to start with X or O.
def start_symbol():
    input_invalid = True
    while input_invalid:
        try:
            start = input("Do you want to start with X or O?, type 'X' or 'O': ")
            start = start.upper()
            if start == 'X' or start == 'O':
                return start
            else:
                print("You have to type 'X' or 'O'")
        except ValueError:
            print("You have to type 'X' or 'O'")
