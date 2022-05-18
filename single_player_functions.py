import random


# Function to ask who will start first.
def who_first():
    input_invalid = True
    while input_invalid:
        try:
            first = int(input("Type 1 for you to start first and type 2 for for computer to start first.: "))
            if first == 1 or first == 2:
                input_invalid = False
                return first
            else:
                print("You have to type 1 or 2.")
        except ValueError:
            print("You have to type 1 or 2.")


# Asking the player if they want to be X or O.
def x_or_o_():
    input_invalid = True
    while input_invalid:
        try:
            x_or_o = input("Type X for you to be X and type O for you to be O.: ")
            x_or_o = x_or_o.upper()
            if x_or_o == "X" or x_or_o == "O":
                input_invalid = False
                return x_or_o
            else:
                print("You have to type X or O.")
        except ValueError:
            print("You have to type X or O.")


# Function to check if the move is available.
def check_move_available(move, moves_available):
    if move in moves_available:
        return True


# Function for computer to make move.
def computer_move_(moves_available):
    computer_move = random.choice(moves_available)
    return computer_move
