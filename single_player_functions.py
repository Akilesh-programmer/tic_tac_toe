import random


# Function to ask who will start first.
def who_first():
    first = input("Type 1 for you to start first and type 2 for for computer to start first.: ")

    if first != "1" and first != "2":
        print("You have to type 1 or 2.")
        input_invalid = True

        while input_invalid:
            first = input("Type 1 for you to start first and type 2 for the computer to start first.: ")

            if first == "1" or first == "2":
                input_invalid = False
    return int(first)


# Asking the player if they want to be X or O.
def x_or_o_():
    x_or_o = input("Type X for you to be X and type O for you to be O.: ")

    if x_or_o != "X" and x_or_o != "O" and x_or_o != "x" and x_or_o != "o":
        print("You have to type X or O.")
        input_invalid = True

        while input_invalid:
            x_or_o = input("Type X for you to be X and type O for you to be O.: ")

            if x_or_o == "X" or x_or_o == "O" or x_or_o == "x" or x_or_o == "o":
                input_invalid = False
    return x_or_o.upper()


# Function to check if the move is available.
def check_move_available(move, moves_available):
    if move in moves_available:
        return True


# Function for computer to make move.
def computer_move_(moves_available):
    computer_move = random.choice(moves_available)
    return computer_move
