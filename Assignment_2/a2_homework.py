#asignment for week 2
import random
def generate_list_of_N_numbers(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 100))
    return list


def Selection_Sort(list, step):
    '''
        The function is sorting the elements of the list using Selection Sort.
        :param list: the list that is needed to be sorted
        :param step: from how many steps the function print the intermediary list
        :return: the list sorted
        '''
    length = len(list) # the length of the list
    count = 0
    for i in range(length - 1):
        indexMin = i # the smallest element so far
        for j in range(i + 1, length):
            if list[j] < list[indexMin]:
                indexMin = j # saving the index of the newly smallest found element
        list[i], list[indexMin] = list[indexMin], list[i] # swapping the elements
        count += 1
        if count % step == 0:
            print(list)
    return list


def getNextGap(n):
    return int(n // 1.3)


def Comb_Sort(list, step):
    '''
    The function is sorting the elements of the list using Comb Sort.
    Comb sort is an improved version of bubble sort
    :param list: the list that is needed to be sorted
    :param step: from how many steps the function print the intermediary list
    :return: the list sorted
    '''
    count = 0
    length = len(list)
    gap = getNextGap(length)
    swapped = True
    while gap > 1 or swapped is True:
        swapped = False
        for i in range(0, length - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i] # swapping the elements
                swapped = True
                count += 1
                if count % step == 0:
                    print(list)
        gap = getNextGap(gap)
        #printing from step to step


    return list



def asignment2():
    numberFromUser = -1
    list = []
    while(numberFromUser != 0):
        print('''
        1 - Generate n random numbers
        2 - Sort using Selection Sort
        3 - Sort using Comb Sort
        4 - Show list
        0 - Exit the program
        ''')
        numberFromUser = input('Choose a number: ')
        if numberFromUser == '1':
            n = int(input("How many elements do you want to have in the list?: "))
            list = generate_list_of_N_numbers(n)

        elif numberFromUser == '2':
            step = int(input("Enter the steps: "))
            list = Selection_Sort(list, step)

        elif numberFromUser == '3':
            step = int(input("Enter the steps: "))
            list = Comb_Sort(list, step)

        elif numberFromUser == '4':
            print(list)

        else:
            break


asignment2()
