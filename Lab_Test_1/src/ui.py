
from functions import *
def start():
    # having  6 animals hard coded
    animals = []
    animal1 = {"code": "Z01", "name": "Alex", "type": "herbivore", "species": "zebra"}
    animals.append(animal1)
    animal2 = {"code": "Z02", "name": "George", "type": "herbivore", "species": "zebra"}
    animals.append(animal2)
    animal3 = {"code": "Z03", "name": "Stefan", "type": "herbivore", "species": "zebra"}
    animals.append(animal3)
    animal4 = {"code": "Z04", "name": "Matei", "type": "carnivore", "species": "bear"}
    animals.append(animal4)
    animal5 = {"code": "Z05", "name": "Pavel", "type": "carnivore", "species": "bear"}
    animals.append(animal5)
    animal6 = {"code": "Z06", "name": "Cristian", "type": "carnivore", "species": "bear"}
    animals.append(animal6)


    while True:
        option = input("""

            1 - add an animal
            2 - modify the type of an animal
            3 - change all types for a species
            4 - show all animals with a given type (sorted in ascending order of their name)

            """)
        if option == '1':
            # getting the input
            print("Enter the following regarding the animal you want to add:")
            code = input("code = ")
            name = input("name = ")
            type = input("type = ")
            species = input("species = ")

            # chacking for void input
            if len(code) == 0 or len(name) == 0 or len(type) == 0 or len(species) == 0:
                print("One of the input is void. Please try again.")
                continue

            # checking for used code
            for i in range(len(animals)):
                if animals[i]["code"] == code:
                    print("Sorry, the code you entered is already used. Please eneter another one.")
                    continue

            # calling the add_animal function
            animals = add_animal(animals, code, name, type, species)

        # ---------------------------------------------------
        elif option == '2':
            # getting the input
            code = input("code = ")
            type = input("type = ")

            # calling the modify_type function
            animals = modify_type(animals, code, type)

        # ---------------------------------------------------
        elif option == '3':
            # getting the input
            species = input("species = ")
            new_type = input("type = ")

            # validating
            if len(new_type) == 0:
                print("The type is void. Please try again.")
                continue

            #calling the change_types function
            animals = change_types(animals, species, new_type)

            # ---------------------------------------------------
        elif option == '4':
            # getting the input
            type = input("type = ")

            #calling the show_animals_with_type
            print(show_animals_with_type(animals, type))


test_add_animal()
start()