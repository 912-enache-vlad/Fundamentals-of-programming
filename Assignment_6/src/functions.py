#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
from random import randint
def add_new_transaction(apartments:list, nr_ap:int, type:str, amount:int):
    '''
    The function adds the amount of type to the apartment with number nr_ap
    @param apartments: list of apartments
    @param nr_ap: the apartment number
    @param type: type of the transaction (water, heating, electricity, gas, other>
    @param amount: the amount of the transaction in RON
    @return: the apartments list modified accordingly
    '''

    apartments[nr_ap][type] += amount
    return apartments


def test_add_new_transaction(apartments:list):
    '''
    The function test if the add_new_transaction function works properly
    @param apartments: apartment list
    @return: nothing but an AssertError will appear if something does not work correctly
    '''
    # saving the values of the first apartment in order to verify in the end if add_new_transaction() works properly
    apartment_copy = apartments[0].copy()

    apartments = add_new_transaction(apartments, 0, "gas", 100)

    # testing if it works correctly
    assert (apartment_copy["gas"] + 100 == apartments[0]["gas"])


def modify_expenses(apartments:list, nr_ap_st:int, nr_ap_end:int, type:str, amount):
    '''
    The function modifies the expeneses from the specified apartments
    @param apartments: list of apartments
    @param nr_ap_st: the first apartment number
    @param nr_ap_end: the last apartment number
    @param type: the type of the expense or "all" in the case when removing all expenses from the specified apartments
    @param amount: amount wanted to replace an expense or -1 when removing from all apartments a specific expense
    @return: the apartments list modified accordingly
    '''

    if type == "all": # the case when removing all expenses from the specified apartments
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            for type in apartments[nr_ap]:
                apartments[nr_ap][type] = 0

    elif amount == -1: # the case when removing from all apartments a specific expense
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            apartments[nr_ap][type] = 0

    else:
        apartments[nr_ap_st][type] = amount

    return apartments


def test_modify_expenses(apartments:list):
    '''
        The function test if the modify_expenses function works properly
        @param apartments: apartment list
        @return: nothing but an AssertError will appear if something does not work correctly
        '''
    # case when removing all expenses from an apartment
    apartments = modify_expenses(apartments, 0, 0, "all", -1)

    for type in apartments[0]:
        assert (apartments[0][type] == 0)

    # case when all expenses from apartment 3 to 5
    apartments = modify_expenses(apartments, 3, 5, "all", -1)

    for nr_ap in [3, 4, 5]:
        for type in apartments[nr_ap]:
            assert (apartments[nr_ap][type] == 0)

    # case when removing all gas expenses from all apartments
    apartments = modify_expenses(apartments, 0, len(apartments) - 1, "gas", -1)

    for nr_ap in range(len(apartments)):
        assert (apartments[nr_ap]["gas"] == 0)

    # case when replacing an amount of an expense from an apartments
    apartments = modify_expenses(apartments, 6, 6, "gas", 50)

    assert apartments[6]["gas"] == 50


def display_apartments(apartments:list, nr_ap_st, nr_ap_end:int, comparison_sign:str, amount):
    '''
    The function displays the apartments with some properties
    @param apartments: list of apartments
    @param nr_ap_st: the first apartment number
    @param nr_ap_end: the last apartment number
    @param comparison_sign: the comparison sign used in displaying - "" empty string if is not needed
    @param amount: the amount used in comparing or -1 when is not necessary
    @return: a string containing the output wanted
    '''

    result = "" #initialising the result string

    if comparison_sign == "": # if comparison sign is empty => just displaying
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            result += f"Expenses for apartment {nr_ap}:\n"
            for expense_type in apartments[nr_ap]:
                result += f"   -{expense_type} = {apartments[nr_ap][expense_type]}\n"

        return result

    # initialising the list where it will be stores total expenses of every apartment
    apartments_expenses = []

    # building apartments_expenses list
    for nr_ap in range(len(apartments)):
        temp = 0
        for expense_type in apartments[nr_ap]:
            temp += apartments[nr_ap][expense_type]
        apartments_expenses.append(temp)


    if comparison_sign == "<":
        result += f"Apartments having total expenses < {amount}:\n"
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            if apartments_expenses[nr_ap] < amount:
                result += f"   -Apartment {nr_ap}\n"
    elif comparison_sign == "=":
        result += f"Apartments having total expenses = {amount}:\n"
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            if apartments_expenses[nr_ap] == amount:
                result += f"   -Apartment {nr_ap}\n"
    elif comparison_sign == ">":
        result += f"Apartments having total expenses > {amount}:\n"
        for nr_ap in range(nr_ap_st, nr_ap_end + 1):
            if apartments_expenses[nr_ap] > amount:
                result += f"   -Apartment {nr_ap}\n"

    return result


def test_display_apartments(apartments:list):


    # case when displaying all expenses from an apartment
    assert display_apartments(apartments, 1, 1, '', -1) == f'Expenses for apartment 1:\n   -water = {apartments[1]["water"]}\n   -heating = {apartments[1]["heating"]}\n   -electricity = {apartments[1]["electricity"]}\n   -gas = {apartments[1]["gas"]}\n   -other = {apartments[1]["other"]}\n'

    # case when displaying all expenses from all apartment
    apartments = []
    for i in range(2):
        temp = {}
        temp["water"] = 1
        temp["heating"] = 1
        temp["electricity"] = 1
        temp["gas"] = 1
        temp["other"] = 1
        apartments.append(temp)

    assert display_apartments(apartments, 0, len(apartments) - 1, '', -1) == 'Expenses for apartment 0:\n   -water = 1\n   -heating = 1\n   -electricity = 1\n   -gas = 1\n   -other = 1\nExpenses for apartment 1:\n   -water = 1\n   -heating = 1\n   -electricity = 1\n   -gas = 1\n   -other = 1\n'



    # creating apartments for the other tests
    apartments = []
    for i in range(4):
        temp = {}
        temp["water"] = i + 1
        temp["heating"] = i + 1
        temp["electricity"] = i + 1
        temp["gas"] = i + 1
        temp["other"] = i + 1
        apartments.append(temp)

    # case when displaying all apartments having total expenses > given amount
    assert display_apartments(apartments, 0, len(apartments) - 1, '>', 10) == 'Apartments having total expenses > 10:\n   -Apartment 2\n   -Apartment 3\n'

    # case when displaying all apartments having total expenses = given amount
    assert display_apartments(apartments, 0, len(apartments) - 1, '=', 10) == 'Apartments having total expenses = 10:\n   -Apartment 1\n'

    # case when displaying all apartments having total expenses < given amount
    assert display_apartments(apartments, 0, len(apartments) - 1, '<',
                              10) == 'Apartments having total expenses < 10:\n   -Apartment 0\n'


def filter(apartments: list, expense_type: str, amount: int):
    '''
    The function removes expenses according to the instruction
    @param apartments: the list of apartments
    @param expense_type: the expense type
    @param amount: the amount of money needed in finding apartments with less total expenses
    @return: the apartments list modified accordingly
    '''

    if amount == -1: # the case when keeping only expense_type transaction
        for nr_ap in range(len(apartments)):
            for exp_type in apartments[nr_ap]:
                if exp_type != expense_type:
                    apartments[nr_ap][exp_type] = 0
    else:
        for nr_ap in range(len(apartments)):
            for exp_type in apartments[nr_ap]:
                if apartments[nr_ap][exp_type] >= amount:
                    apartments[nr_ap][exp_type] = 0

    return apartments


def test_filter(apartments:list):

    # the case when keeping only one expense
    apartments = filter(apartments, "gas", -1)
    for nr_ap in range(len(apartments)):
        for exp_type in apartments[nr_ap]:
            if exp_type != "gas":
                assert apartments[nr_ap][exp_type] == 0

   # the case when keeping only expenses smaller then an given amount
    apartments = []
    temp = {}
    temp["water"] = 60
    temp["heating"] = 70
    temp["electricity"] = 50
    temp["gas"] = 100
    temp["other"] = 40
    apartments.append(temp)

    apartments = filter(apartments, "all", 61)
    assert apartments[0]["water"] == 60
    assert apartments[0]["heating"] == 0
    assert apartments[0]["electricity"] == 50
    assert apartments[0]["gas"] == 0
    assert apartments[0]["other"] == 40


def test_all():
    """
    The function tests if all the functions work properly
    @return:
    """

    # initialising the list of apartments
    apartments = []
    # generating the list of 2 apartments randomly
    size = 10
    for i in range(size):
        temp = {}
        temp["water"] = randint(1, 100)
        temp["heating"] = randint(1, 100)
        temp["electricity"] = randint(1, 100)
        temp["gas"] = randint(1, 100)
        temp["other"] = randint(1, 100)
        apartments.append(temp)

    test_add_new_transaction(apartments)
    test_modify_expenses(apartments)
    test_display_apartments(apartments)
    test_filter(apartments)


test_all()



