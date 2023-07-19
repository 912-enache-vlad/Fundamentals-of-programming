from src.service import Game, EndOfGame, EndOfPlacement, GameException


class UserInterface:
    def __init__(self):
        self.__game = Game("game.txt")

    def __call__(self):

        while True:
            choice = input("""
            1 - load game
            2 - start new game
            """)
            if choice == "1":
                try:
                    humanPiece = self.__game.loadGame()
                    if humanPiece == "x":
                        computerPiece = "o"
                    else:
                        computerPiece = "x"
                    print(self.__game.displayBoard())
                    break
                except Exception as e:
                    print(f"Error - {e}")
                    continue
            elif choice == "2":

                while True:
                    choice = input("""
                            1 - play with x and you make the first move
                            2 - play with o and computer makes the first move
                            """)
                    if choice == "1":
                        humanPiece = "x"
                        computerPiece = "o"
                        break

                    elif choice == "2":
                        humanPiece = "o"
                        computerPiece = "x"
                        break

                    else:
                        print("Invalid command!")

            else:
                print("Invalid command!")


        # when starting the program, the user is asked if he wants to load a game or start a new one

        print(self.__game.displayBoard())

        print("Placement phase:\n")
        rounds = 0
        while True:
            save = input("Do you want to save the game? (y/n) ")
            if save == "y":
                self.__game.saveGame()
                print("Game saved!")
            if rounds == 8:
                break
            if humanPiece == "x":
                try:
                    i = int(input("i = "))
                    j = int(input("j = "))
                    self.__game.place(i, j, "x")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except GameException as ge:
                    print(ge)
                    continue
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())
                rounds += 1
                try:
                    self.__game.compMove("o")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except EndOfPlacement:
                    print(self.__game.displayBoard())
                    break
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())
                rounds += 1

            elif humanPiece == "o":
                try:
                    lastMove = self.__game.compMove("x")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())
                rounds += 1
                try:
                    i = int(input("i = "))
                    j = int(input("j = "))
                    self.__game.place(i, j, "o")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except EndOfPlacement:
                    print(self.__game.displayBoard())
                    break
                except Exception as e:
                    print(f"Error - {e}")

                print(self.__game.displayBoard())
                rounds += 1

        print("Movement phase:\n")
        while True:
            save = input("Do you want to save the game? (y/n) ")
            if save.lower() == "y":
                self.__game.saveGame()
                print("Game saved!")
            if humanPiece == "x":
                try:
                    iFrom = int(input("iFrom = "))
                    jFrom = int(input("jFrom = "))
                    iTo = int(input("iTo = "))
                    jTo = int(input("jTo = "))
                    self.__game.move(iFrom, jFrom, iTo, jTo, "x")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())
                try:
                    self.__game.compMoveMovementPhase("o")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())

            elif humanPiece == "o":
                try:
                    self.__game.compMoveMovementPhase("x")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())
                try:
                    iFrom = int(input("iFrom = "))
                    jFrom = int(input("jFrom = "))
                    iTo = int(input("iTo = "))
                    jTo = int(input("jTo = "))
                    self.__game.move(iFrom, jFrom, iTo, jTo, "o")
                except EndOfGame as eog:
                    print(eog)
                    print(self.__game.displayBoard())
                    return
                except Exception as e:
                    print(f"Error - {e}")
                print(self.__game.displayBoard())

