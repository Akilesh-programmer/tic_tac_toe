# Imports
import pygame
import constants
import single_player_functions
import common_functions


def single_player():
    # Asking the player who is first.
    first = single_player_functions.who_first()

    # Asking the player if they want to be X or O.
    player_symbol = single_player_functions.x_or_o_()

    # Setting computer symbol.
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

    # Board where the data will be stored.
    board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

    # Creating a list to store the moves available.
    moves_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Initializing pygame
    pygame.init()

    # Screen
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)

    # Title
    pygame.display.set_caption("Tic Tac Toe")

    # Icon
    icon = pygame.image.load(constants.TIC_TAC_TOE_IMAGE)
    pygame.display.set_icon(icon)

    # Game
    game_on = True

    # Variable to track the number of moves done.
    number_of_moves_done = 0

    # Images
    x_image = pygame.image.load(constants.CROSS_IMAGE)
    o_image = pygame.image.load(constants.NOT_IMAGE)
    x_image = pygame.transform.scale(x_image, constants.DEFAULT_IMAGE_SIZE)
    o_image = pygame.transform.scale(o_image, constants.DEFAULT_IMAGE_SIZE)

    number_of_times_running = 0

    while game_on:
        number_of_times_running += 1
        if number_of_times_running == 1:
            print("Click anywhere in the recently opened window to start.")
        for event in pygame.event.get():
            # Quitting the game if the player presses cross button.
            if event.type == pygame.QUIT:
                game_on = False

            # Detecting the click in mouse button.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Getting the coordinates of the click.
                position = event.pos
                # Finding the square which was clicked.
                clicked_square = common_functions.find_square_clicked(position)

                # If player wants to go first.
                if first == 1:
                    if number_of_moves_done % 2 == 0:
                        # Player's move.
                        player_move = clicked_square
                        # Checking if player's move is available.
                        if single_player_functions.check_move_available(player_move, moves_available):
                            board[player_move] = player_symbol
                            moves_available.remove(player_move)

                            number_of_moves_done += 1

                    if number_of_moves_done % 2 != 0:
                        # Computers' move.
                        computer_move = single_player_functions.computer_move_(moves_available)
                        board[computer_move] = computer_symbol
                        moves_available.remove(computer_move)

                        number_of_moves_done += 1

                # If the player wants to go second.
                elif first == 2:
                    if number_of_moves_done % 2 != 0:
                        # Player's move.
                        player_move = clicked_square
                        if single_player_functions.check_move_available(player_move, moves_available):
                            board[player_move] = player_symbol
                            moves_available.remove(player_move)

                        print("Player moving.")
                        number_of_moves_done += 1
                    if number_of_moves_done % 2 == 0:
                        # Computer's move.
                        print("Computer moving.")
                        computer_move = single_player_functions.computer_move_(moves_available)
                        board[computer_move] = computer_symbol
                        moves_available.remove(computer_move)

                        number_of_moves_done += 1

        # Background colour of the screen.
        screen.fill(constants.BACKGROUND_COLOUR)

        # Drawing lines.
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
            break
        if common_functions.check_draw(moves_available):
            game_on = False
            print("Draw")

        # Updating the display.
        pygame.display.update()
