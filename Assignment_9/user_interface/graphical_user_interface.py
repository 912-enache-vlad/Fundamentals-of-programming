# from game.game import Game
# import pygame
#
# #make a graphical user interface for connect 4 using pygame
# """
#     - the game is played on a 6x7 board
#     - the first player to get 4 of their pieces in a row (horizontally, vertically, or diagonally) wins
#     - the game is played by a player and a computer
#     - the player can choose a column to drop a piece in
#     - the computer will choose a column to drop a piece in
#
#     """
# class Grafical_user_interface:
#     def __init__(self, game: Game):
#         self.__game = game
#         self.__board = game.get_board()
#         self.__boardSize = self.__board.get_size()
#         self.__rows = self.__boardSize[0]
#         self.__cols = self.__boardSize[1]
#         self.__cellSize = 100
#         self.__width = self.__cols * self.__cellSize
#         self.__height = (self.__rows + 1) * self.__cellSize
#         self.__size = (self.__width, self.__height)
#         self.__radius = int(self.__cellSize / 2 - 5)
#         self.__screen = pygame.display.set_mode(self.__size)
#         self.__font = pygame.font.SysFont("monospace", 75)
#
#     def __call__(self):
#         pygame.init()
#         pygame.display.set_caption("Connect 4")
#         self.__screen.fill(pygame.Color("white"))
#         self.__draw_board()
#         pygame.display.update()
#         myfont = pygame.font.SysFont("monospace", 75)
#         label = myfont.render("Player 1", 1, (0, 0, 0))
#         self.__screen.blit(label, (40, 10))
#         label = myfont.render("Player 2", 1, (0, 0, 0))
#         self.__screen.blit(label, (40, 10))
#         pygame.display.update()
#         game_over = False
#         turn = 0
#         while not game_over:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
#                 if event.type == pygame.MOUSEMOTION:
#                     pygame.draw.rect(self.__screen, pygame.Color("white"), (0, 0, self.__width, self.__cellSize))
#                     posx = event.pos[0]
#                     if turn == 0:
#                         pygame.draw.circle(self.__screen, pygame.Color("red"), (posx, int(self.__cellSize / 2)), self.__radius)
#                     else:
#                         pygame.draw.circle(self.__screen, pygame.Color("yellow"), (posx, int(self.__cellSize / 2)), self.__radius)
#                 pygame.display.update()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     pygame.draw.rect(self.__screen, pygame.Color("white"), (0, 0, self.__width, self.__cellSize))
#                     # print(event.pos)
#                     # Ask for Player 1 Input
#                     if turn == 0:
#
#
#
#
# # class Grafical_user_interface:
# #     def __init__(self, game: Game):
# #         self.__game = game
# #
# #     def __call__(self):
# #         #initialise pygame
# #         pygame.init()
# #
# #         #use the structure from user_interface.py
# #         #create a window
# #         window = pygame.display.set_mode((700, 600))
# #         pygame.display.set_caption("Connect 4")
# #
# #         #create a  6 x 7 board
# #         board = pygame.Surface((600, 500))
# #         board.fill((255, 255, 255))
# #         board_rect = board.get_rect()
# #         board_rect.center = (350, 300)
# #
# #         #create a 7 x 1 column
# #         column = pygame.Surface((100, 500))
# #         column.fill((255, 255, 255))
# #         column_rect = column.get_rect()
# #
# #         #create a 1 x 1 circle
# #         circle = pygame.Surface((100, 100))
# #         circle.fill((255, 255, 255))
# #         circle_rect = circle.get_rect()
# #
# #         #use the structure from user_interface.py
# #         #create a loop
# #         while True:
# #             #use the structure from user_interface.py
# #             #check for events
# #             for event in pygame.event.get():
# #                 #check if the event is quit
# #                 if event.type == pygame.QUIT:
# #                     #quit the game
# #                     pygame.quit()
# #                     quit()
# #                 #check if the event is mouse button down
# #                 if event.type == pygame.MOUSEBUTTONDOWN:
# #                     #get the mouse position
# #                     mouse_pos = pygame.mouse.get_pos()
# #                     #check if the mouse position is in the column
# #                     if column_rect.collidepoint(mouse_pos):
# #                         #get the column number
# #                         column_number = mouse_pos[0] // 100
# #                         #get the row number
# #                         row_number = self.__game.gravity_col(column_number)
# #                         #make the human move
# #                         self.__game.human_move(row_number, column_number)
# #                         #make the computer move
# #                         self.__game.computer_move()
# #
# #             #use the structure from user_interface.py
# #             #draw the board
# #             window.blit(board, board_rect)
# #             #draw the column
# #             window.blit(column, column_rect)
# #             #draw the circle
# #             window.blit(circle, circle_rect)
# #             #update the display
# #             pygame.display.update()
# #
# #
# #
#
#
