
from a5_program import *
# from a5_dict_repr import *
from a5_list_repr import *
from random import randint

# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities


def display_list(complex_nrs:list):
    for e in complex_nrs:
        print(to_str(e), end = ", ")

def read_list_of_complex_nrs():
    complex_nrs = []
    n = int(input("Enter how many numbers do you want to enter: "))
    for i in range(n):
        real = int(input("Enter the real part of number " + str(i + 1) + ": "))
        img = int(input("Enter the imaginary part of number " + str(i + 1) + ": "))
        complex_nrs.append(create_complex(real, img))

    return complex_nrs

def display_menu():
    print("""

            1 - Read a list of complex numbers (in z = a + bi form).
            2 - Display the entire list of numbers.
            3a - Length and elements of a longest subarray of distinct numbers.
            3b - The length and elements of a longest increasing subsequence, when considering each number's modulus
            x - Exit the application.

            """)

def user_interface():

    complex_nrs = []
    for i in range(10):
        complex_nrs.append(create_complex(randint(1, 10), randint(1, 10)))


    while True:

        display_menu()

        option = input("Enter the option: ")

        if option == "1":
            complex_nrs = read_list_of_complex_nrs()

        elif option == "2":
            display_list(complex_nrs)

        elif option == "3a":
            print("Hello")
            result = longest_subarray_of_distinct_nrs(complex_nrs)
            print("The longest subarray of distinct numbers is = " + str(len(result)))
            print("And the subarray is:")
            display_list(result)
        elif option == "3b":
            result = longest_increasing_subsequence_of_modulus(complex_nrs)
            print("Max length: " + str(len(result)))
            display_list(result)

        elif option == "x":
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    user_interface()