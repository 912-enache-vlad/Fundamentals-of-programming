
def add_animal(animals, code, name, type, species):
    """
    The function adds an animal to the collection of animals
    :param animals: the collection of animals
    :param code: the code for the new animal
    :param name: the name for the new animal
    :param type: the type for the new animal
    :param species: the species for the new animal
    :return: the collection of animals modified
    """

    new_animal = {"code": code, "name": name, "type": type, "species": species}
    animals.append(new_animal)

    return animals


def test_add_animal():
    animals = []
    animals_modified = []
    # adding animal 1 and 2 to both lists
    animal1 = {"code": "Z01", "name": "Alex", "type": "herbivore", "species": "zebra"}
    animals.append(animal1)
    animals_modified.append(animal1)
    animal2 = {"code": "Z02", "name": "George", "type": "herbivore", "species": "zebra"}
    animals.append(animal2)
    animals_modified.append(animal2)

    # adding a new animal only in animals_modified list
    new_animal = {"code": "Z03", "name": "Stefan", "type": "herbivore", "species": "zebra"}
    animals_modified.append(new_animal)

    assert animals_modified == add_animal(animals, new_animal["code"], new_animal["name"], new_animal["type"], new_animal["species"])


def modify_type(animals, code, type):

    # finding the animal with the code and changing the type
    for i in range(len(animals)):
        if animals[i]["code"] == code:
            animals[i]["type"] = type
            return animals

    return animals


def change_types(animals, species, new_type):

    for i in range(len(animals)):
        if animals[i]["species"] == species:
            animals[i]["type"] = new_type

    return animals


def animal_to_str(animal):
    return f"animal with code {animal['code']} have the name {animal['name']}, the type {animal['type']} and the species {animal['species']}\n"

def show_animals_with_type(animals, type):

    show_animals = []
    str_result = ""

    # building the list with the animals that will be displayed
    for i in range(len(animals)):
        if animals[i]["type"] == type:
            show_animals.append(animals[i])

    # sorting show_animals list by name
    for i in range(len(show_animals) - 1):
        for j in range(i+1, len(show_animals)):
            if show_animals[i]['name'] > show_animals[j]['name']:
                show_animals[i], show_animals[j] = show_animals[j], show_animals[i]

    # making the string to be printed
    for i in range(len(show_animals)):
        str_result += animal_to_str(show_animals[i])

    return str_result
