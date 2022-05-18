# Imports
import single_player

# Asking the player which mode they want to play. Again and again asking them if they give wrong input.
mode = int(input("Do you want to play single player(1) or multiplayer(2)? Type the number.: "))
if mode != 1 and mode != 2:
    print("You have to type 1 or 2.")
    mode_input_invalid = True
    while mode_input_invalid:
        mode = int(input("Do you want to play single player(1) or multiplayer(2)? Type the number.: "))
        if mode == 1 or mode == 2:
            mode_input_invalid = False

if mode == 1:
    single_player.single_player()
