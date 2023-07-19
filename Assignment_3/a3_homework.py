#asignment for week 3
import random
import timeit
from tabulate import tabulate

def generate_list_of_N_numbers(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 10000))
    return list


def Selection_Sort(list):
    '''
        The function is sorting the elements of the list using Selection Sort.
        :param list: the list that is needed to be sorted
        :param step: from how many steps the function print the intermediary list
        :return: the list sorted
    '''
    length = len(list) # the length of the list
    for i in range(length - 1):
        indexMin = i # the smallest element so far
        for j in range(i + 1, length):
            if list[j] < list[indexMin]:
                indexMin = j # saving the index of the newly smallest found element
        list[i], list[indexMin] = list[indexMin], list[i] # swapping the elements
    return list


def getNextGap(n):
    return int(n // 1.3)


def Comb_Sort(list):
    '''
    The function is sorting the elements of the list using Comb Sort.
    Comb sort is an improved version of bubble sort
    :param list: the list that is needed to be sorted
    :param step: from how many steps the function print the intermediary list
    :return: the list sorted
    '''
    length = len(list)
    gap = getNextGap(length)
    swapped = True
    while gap > 1 or swapped is True:
        swapped = False
        for i in range(0, length - gap):
            if list[i] > list[i + gap]:
                list[i], list[i + gap] = list[i + gap], list[i] # swapping the elements
                swapped = True
        gap = getNextGap(gap)
    return list


def BestCase():
    length = 500
    times = [['Length', 'Selection Sort', 'Comb Sort']] # initialising the list with the times
    for i in range(5):
        list1 = generate_list_of_N_numbers(length)
        list1.sort()
        list2 = list1[:]
        time1 = timeit.timeit(lambda: Selection_Sort(list1), number = 1)
        time2 = timeit.timeit(lambda: Comb_Sort(list2), number = 1)
        times.append([length, time1, time2])
        length *= 2 # doubling the size of the list
    print("The Best Case:")
    print(tabulate(times, headers = "firstrow", tablefmt = "fancy_grid"))


def WorstCase():
    length = 500
    times = [['Length', 'Selection Sort', 'Comb Sort']]  # initialising the list with the times
    for i in range(5):
        list1 = generate_list_of_N_numbers(length)
        list1.sort(reverse = True) # elemets in decreasing order
        list2 = list1[:]
        time1 = timeit.timeit(lambda: Selection_Sort(list1), number=1)
        time2 = timeit.timeit(lambda: Comb_Sort(list2), number=1)
        times.append([length, time1, time2])
        length *= 2  # doubling the size of the list
    print('The Worst Case:')
    print(tabulate(times, headers="firstrow", tablefmt="fancy_grid"))


def AverageCase():
    length = 500
    times = [['Length', 'Selection Sort', 'Comb Sort']]  # initialising the list with the times
    for i in range(5):
        list1 = generate_list_of_N_numbers(length)
        list2 = list1[:]
        time1 = timeit.timeit(lambda: Selection_Sort(list1), number=1)
        time2 = timeit.timeit(lambda: Comb_Sort(list2), number=1)
        times.append([length, time1, time2])
        length *= 2  # doubling the size of the list
    print('The Average Case:')
    print(tabulate(times, headers="firstrow", tablefmt="fancy_grid"))


def GUI():
    numberFromUser = -1
    list = []
    while(numberFromUser != 0):
        print('''
        0 - Exit the program
        1 - Generate n random numbers
        2 - Sort using Selection Sort
        3 - Sort using Comb Sort
        4 - Show list
        
        Find the time complexity of the algorithms:
        7 - Best Case Test
        8 - Worst Case Test
        9 - Average Case Test
        ''')
        numberFromUser = input('Choose a number: ')
        if numberFromUser == '1':
            n = int(input("How many elements do you want to have in the list?: "))
            list = generate_list_of_N_numbers(n)

        elif numberFromUser == '2':
            list = Selection_Sort(list)

        elif numberFromUser == '3':
            list = Comb_Sort(list)

        elif numberFromUser == '4':
            print(list)

        elif numberFromUser == '7':
            BestCase()

        elif numberFromUser == '8':
            WorstCase()

        elif numberFromUser == '9':
            AverageCase()

        elif numberFromUser == '0':
            break


if __name__ == "__main__":
    GUI()
