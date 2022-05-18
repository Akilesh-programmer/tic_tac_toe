# Function to check win.
def check_win(board):
    # Checking for "X" win.
    if board[1] == board[2] == board[3] == "X":
        return "X"
    elif board[4] == board[5] == board[6] == "X":
        return "X"
    elif board[7] == board[8] == board[9] == "X":
        return "X"
    elif board[1] == board[4] == board[7] == "X":
        return "X"
    elif board[2] == board[5] == board[8] == "X":
        return "X"
    elif board[3] == board[6] == board[9] == "X":
        return "X"
    elif board[1] == board[5] == board[9] == "X":
        return "X"
    elif board[3] == board[5] == board[7] == "X":
        return "X"

    # Checking for "O" win.
    elif board[1] == board[2] == board[3] == "O":
        return "O"
    elif board[4] == board[5] == board[6] == "O":
        return "O"
    elif board[7] == board[8] == board[9] == "O":
        return "O"
    elif board[1] == board[4] == board[7] == "O":
        return "O"
    elif board[2] == board[5] == board[8] == "O":
        return "O"
    elif board[3] == board[6] == board[9] == "O":
        return "O"
    elif board[1] == board[5] == board[9] == "O":
        return "O"
    elif board[3] == board[5] == board[7] == "O":
        return "O"
    else:
        return None


# Function to check draw
def check_draw(moves_available):
    if len(moves_available) == 0:
        return True


# Function to find the square which was clicked.
def find_square_clicked(coordinates):
    x = coordinates[0]
    y = coordinates[1]

    if x <= 200 and y <= 200:
        return 1
    elif 200 <= x <= 400 and y <= 200:
        return 2
    elif x >= 400 and y <= 200:
        return 3
    elif x <= 200 and 200 <= y <= 400:
        return 4
    elif 200 <= x <= 400 and 200 <= y <= 400:
        return 5
    elif x >= 400 and y >= 200 and y <= 400:
        return 6
    elif x <= 200 and y >= 400:
        return 7
    elif 200 <= x <= 400 <= y:
        return 8
    elif x >= 400 and y >= 400:
        return 9


# Function to find the coordinate for image to be displayed.
def square_coordinates(square_number):
    if square_number == 1:
        return 50, 50
    elif square_number == 2:
        return 250, 50
    elif square_number == 3:
        return 450, 50
    elif square_number == 4:
        return 50, 250
    elif square_number == 5:
        return 250, 250
    elif square_number == 6:
        return 450, 250
    elif square_number == 7:
        return 50, 450
    elif square_number == 8:
        return 250, 450
    elif square_number == 9:
        return 450, 450
