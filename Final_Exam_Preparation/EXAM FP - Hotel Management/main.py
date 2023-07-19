from services import Services
from userInterface import UserInterface

if __name__ == "__main__":
    service = Services()
    userInterface = UserInterface(service)
    userInterface()