# Imports
import single_player
import multiplayer

mode = None

# Getting to know from the user if they want to play single player or multiplayer
invalid_input = True
while invalid_input:
    try:
        mode = int(input("Do you want to play single player(1) or multiplayer(2)? Type the number.: "))
        if mode == 1 or mode == 2:
            invalid_input = False
        else:
            print("You have to type 1 or 2.")
    except ValueError:
        print("You have to type 1 or 2.")

# Playing the single player
if mode == 1:
    single_player.single_player()
# Playing the multiplayer.
elif mode == 2:
    multiplayer.multiplayer()
