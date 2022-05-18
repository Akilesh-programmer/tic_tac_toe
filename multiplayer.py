#  Imports
import pygame
import constants
import multiplayer_functions
import common_functions


# Creating a function for the gameplay for multiplayer.
def multiplayer():
    # Defining the symbol's of the players.
    player_1_symbol = multiplayer_functions.start_symbol()
    if player_1_symbol == 'X':
        player_2_symbol = 'O'
    else:
        player_2_symbol = 'X'

    # Board
    board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    # Creating a list to store moves available.
    moves_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Initializing pygame.
    pygame.init()
    # Screen
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    # Title
    pygame.display.set_caption("Tic Tac Toe")
    # Icon
    icon = pygame.image.load(constants.TIC_TAC_TOE_IMAGE)
    pygame.display.set_icon(icon)
    # Images
    x_image = pygame.image.load(constants.CROSS_IMAGE)
    o_image = pygame.image.load(constants.NOT_IMAGE)
    x_image = pygame.transform.scale(x_image, constants.DEFAULT_IMAGE_SIZE)
    o_image = pygame.transform.scale(o_image, constants.DEFAULT_IMAGE_SIZE)

    # Game boolean variable
    game_on = True
    # Variable to track the number of moves.
    number_of_moves = 0

    number_of_times_running = 0

    while game_on:
        number_of_times_running += 1
        if number_of_times_running == 1:
            print("CLick on the recently opened window to start.")
        # Getting all the events happening in the screen.
        for event in pygame.event.get():
            # Quitting the game if the user clicks the wrong button.
            if event.type == pygame.QUIT:
                game_on = False
            # Detecting the click in the mouse button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Getting the coordinates of the click.
                position = event.pos
                # Finding the square which was clicked.
                clicked_square = common_functions.find_square_clicked(position)

                if number_of_moves % 2 == 0 or number_of_moves == 0:
                    # Move to be done by player 1.
                    player_1_move = clicked_square
                    # Checking if the move is valid.
                    if player_1_move in moves_available:
                        board[player_1_move] = player_1_symbol
                        moves_available.remove(player_1_move)

                        number_of_moves += 1

                if number_of_moves % 2 != 0:
                    # Move to be done by player 2.
                    player_2_move = clicked_square
                    # Checking if the move is valid.
                    if player_2_move in moves_available:
                        board[player_2_move] = player_2_symbol
                        moves_available.remove(player_2_move)

                        number_of_moves += 1

        # Background colour
        screen.fill(constants.BACKGROUND_COLOUR)

        # Draw lines
        pygame.draw.line(screen, constants.LINE_COLOUR, (400, 0), (400, 600), constants.LINE_WIDTH)
        pygame.draw.line(screen, constants.LINE_COLOUR, (200, 0), (200, 600), constants.LINE_WIDTH)
        pygame.draw.line(screen, constants.LINE_COLOUR, (0, 200), (600, 200), constants.LINE_WIDTH)
        pygame.draw.line(screen, constants.LINE_COLOUR, (0, 400), (600, 400), constants.LINE_WIDTH)

        # Image displaying
        if board[1] == "X":
            screen.blit(x_image, common_functions.square_coordinates(1))
        elif board[1] == "O":
            screen.blit(o_image, common_functions.square_coordinates(1))

        if board[2] == "X":
            screen.blit(x_image, common_functions.square_coordinates(2))
        elif board[2] == "O":
            screen.blit(o_image, common_functions.square_coordinates(2))

        if board[3] == "X":
            screen.blit(x_image, common_functions.square_coordinates(3))
        elif board[3] == "O":
            screen.blit(o_image, common_functions.square_coordinates(3))

        if board[4] == "X":
            screen.blit(x_image, common_functions.square_coordinates(4))
        elif board[4] == "O":
            screen.blit(o_image, common_functions.square_coordinates(4))

        if board[5] == "X":
            screen.blit(x_image, common_functions.square_coordinates(5))
        elif board[5] == "O":
            screen.blit(o_image, common_functions.square_coordinates(5))

        if board[6] == "X":
            screen.blit(x_image, common_functions.square_coordinates(6))
        elif board[6] == "O":
            screen.blit(o_image, common_functions.square_coordinates(6))

        if board[7] == "X":
            screen.blit(x_image, common_functions.square_coordinates(7))
        elif board[7] == "O":
            screen.blit(o_image, common_functions.square_coordinates(7))

        if board[8] == "X":
            screen.blit(x_image, common_functions.square_coordinates(8))
        elif board[8] == "O":
            screen.blit(o_image, common_functions.square_coordinates(8))

        if board[9] == "X":
            screen.blit(x_image, common_functions.square_coordinates(9))
        elif board[9] == "O":
            screen.blit(o_image, common_functions.square_coordinates(9))

        # Checking for wins and draw.
        winner = common_functions.check_win(board)
        if winner == "X" or winner == "O":
            game_on = False
            print(f"{winner} wins.")
        if common_functions.check_draw(moves_available):
            game_on = False
            print("Draw")

        # Updating the display.
        pygame.display.update()
