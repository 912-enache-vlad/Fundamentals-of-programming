'''

This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#TODO Write the user commands but I m not sure if this is necessary or not
user commands:

'''

from random import randint
from functions import *
from copy import deepcopy
def valid_input_validator(tokens:list, length_apartments:int):

    types = ["water", "heating", "electricity", "gas", "other"]
    errors = 0
    if len(tokens) >= 1:
        if tokens[0] == "add":
            # verifing the number apartment
            try:
                nr_ap = int(tokens[1])
                if nr_ap < 0:
                    print(f"The apartment number you entered is negative. Please enter a number between 0 and {length_apartments - 1} for the apartment number")
                    errors += 1
                if nr_ap > length_apartments:
                    print(f"The apartment number is too big. Please enter a number between 0 and {length_apartments - 1} for the apartment number")
                    errors += 1
            except ValueError or TypeError:
                print("The apartment number you entered is not a number. Please try again. :)")
                errors += 1

            # verifing the expense type
            type_found = False
            for exp_type in types:
                if tokens[2] == exp_type:
                    type_found = True
            if not type_found:
                print("Invalid expense type. Please try to choose from these expenses: water, heating, electricity, gas, other")
                errors += 1

            # verifing the amount
            try:
                amount = int(tokens[3])
                if amount < 0:
                    print("The amount you entered is negative. Please try again with a positive number.")
            except ValueError or TypeError:
                print("The amount you entered is not a number. Please try again. :)")

        elif tokens[0] == "remove" or tokens[0] == "replace":
            try:
                nr_ap_st = int(tokens[1])   # verifying nr_ap_st
                if len(tokens) == 2 and tokens[0] == "remove":
                    return True  # instruction - remove 15
                elif len(tokens) == 4 and tokens[0] == "remove":
                    try:
                        nr_ap_end = int(tokens[3])  # verifying nr_ap_end
                        if tokens[2] == "to":
                            return True  # instruction - remove 5 to 10
                        else:
                            print("The word between apartment numbers is not -to- as is should be. Please try again. :)")
                    except ValueError or TypeError:
                        print("The last apartment number is not a number. Please try again. :)")
                        errors += 1
                elif len(tokens) == 5 and tokens[0] == "replace":

                    # verifying the expense type
                    type_found = False
                    for exp_type in types:
                        if tokens[2] == exp_type:
                            type_found = True
                    if not type_found:
                        print("Invalid expense type. Please try to choose from these expenses: water, heating, electricity, gas, other")
                        errors += 1

                    # verifying "with"
                    if tokens[3] != "with":
                        print("The word between the expense and amount is not -with- as is should be. Please try again. :)")
                        errors += 1

                    # verifying the amount
                    try:
                        amount = int(tokens[4])
                        if amount < 0:
                            print("The amount you entered is negative. Please try with a positive number.")
                            errors += 1
                    except ValueError or TypeError:
                        print("The amount is not a number. Please try again. :)")
                        errors += 1

                else: # the case when the input
                    print("Incorrect number of parameters or invalid command. Please try again. :)")
                    errors += 1
            except ValueError or TypeError:

                # verifing the expense type
                type_found = False
                for exp_type in types:
                    if tokens[1] == exp_type:
                        type_found = True
                if not type_found:
                    print("The first apartment number nighter a number nor a expense. Please try again. :)")
                    errors += 1


        elif tokens[0] == "list":
            if len(tokens) == 1:
                return True # instruction - list
            try:
                nr_ap = int(tokens[1])
                if nr_ap > length_apartments:
                    print("Number to big. Please try again.")
            except ValueError or TypeError:
                if tokens[1] not in [">", "=", "<"]:
                    print("The 2nd word is nighter a comparison sign nor a number. Please try again. :)")
                    errors += 1
                try:
                    amount = int(tokens[2])
                except ValueError or TypeError:
                    print("The amount you entered is not a number. Please try again. :)")
                    errors += 1

        elif tokens[0] == "filter":
            try:
                amount = int(tokens[1])
            except ValueError or TypeError:
                # verifying the expense type
                type_found = False
                for exp_type in types:
                    if tokens[1] == exp_type:
                        type_found = True
                if not type_found:
                    print("The first apartment number nighter a number nor a expense. Please try again. :)")
                    errors += 1

        elif tokens[0] in ["undo", "exit"]:
            return True  # instruction - undo

        else:
            print("Invalid command. Please choose from: add, remove, list, filter, undo.")
    else:
        print("Not enough arguments. Please try again. :)")
    return (errors == 0)

def procces_user_command(user_command:str):

    tokens = user_command.split(" ")
    for i in range(len(tokens)):
        if tokens[i] == '':     #if tokens[i] is an empty space
            tokens.pop(i)       #then remove it from the list
            i -= 1              #decrement the index in order to not get over the next element

    return tokens


def user_interface():

    print("Open the Help_User.md to see the user commands.")

    #initalising the list of dictionary
    apartments = []
    stack = []

    #having a least 10 elements randomly generated
    size =  randint(10, 30)
    for i in range(size):
        temp = {}
        temp["water"] = randint(1, 100)
        temp["heating"] = randint(1, 100)
        temp["electricity"] = randint(1, 100)
        temp["gas"] = randint(1, 100)
        temp["other"] = randint(1, 100)
        apartments.append(temp)

        stack.append(deepcopy(apartments))

    while True:
        user_command = input(">")
        tokens = procces_user_command(user_command)

        if valid_input_validator(tokens, len(apartments)):
            command = tokens[0]

            if command == "add":
                #making the changes the user wants to make
                apartments = add_new_transaction(apartments, int(tokens[1]), tokens[2], int(tokens[3]))
                # saving the change into the stack
                stack.append(deepcopy(apartments))

            elif command == "remove" or command == "replace":
                # making the changes the user wants to make
                if len(tokens) == 2 and command == "remove":
                    if tokens[1] not in ["water", "heating", "electricity", "gas", "other"]: # then token 1 is an apartment number
                        apartments = modify_expenses(apartments, int(tokens[1]), int(tokens[1]), "all", -1)
                    else:
                        apartments = modify_expenses(apartments, 0, len(apartments) - 1, tokens[1], -1)
                elif len(tokens) == 4 and command == "remove":
                    apartments = modify_expenses(apartments, int(tokens[1]), int(tokens[3]), "all", -1)
                elif len(tokens) == 5 and command == "replace":
                    apartments = modify_expenses(apartments, int(tokens[1]), int(tokens[1]), tokens[2], int(tokens[4]))
                # saving the change into the stack
                stack.append(deepcopy(apartments))

            elif command == "list":
                result = ""
                if len(tokens) == 1:
                    result = display_apartments(apartments, 0, len(apartments) - 1, "", -1)
                elif len(tokens) == 2:
                    result = display_apartments(apartments, int(tokens[1]), int(tokens[1]), "", -1)
                elif len(tokens) == 3:
                    result = display_apartments(apartments, 0, len(apartments) - 1, tokens[1], int(tokens[2]))
                print(result)

            elif command == "filter":
                # making the changes the user wants to make
                if tokens[1] not in ["water", "heating", "electricity", "gas","other"]:  # then token 1 is the amount
                    apartments = filter(apartments, "", int(tokens[1]))
                else:
                    apartments = filter(apartments, tokens[1], -1)
                # saving the change into the stack
                stack.append(deepcopy(apartments))

            elif command == "undo":
                if len(stack) > 1:
                    stack.pop() # removing the operation just performed
                apartments = stack[-1] # restoring apartment list before the last operation


            elif command == "exit":
                break




