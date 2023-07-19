# "RULES"
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values

# from a5_dict_repr import *
from a5_list_repr import *



# Functions that deal with subarray/subsequence properties

def longest_subarray_of_distinct_nrs(complex_nrs:list):
    '''
    The function is searching for the longest subarray of distinct numbers
    @param complex_nrs: list of complex numbers
    @return: the longest subarray of distinct numbers
    '''
    n = len(complex_nrs)
    maxLength = 0
    length = 1
    start = -1
    end = -1
    used = [] # caracteristic vector for complex numbers
    for i in range(n - 1):
        used = [complex_nrs[i]]  # starting the sequence again
        length = 1
        j = i + 1
        while j < n:
            if complex_nrs[j] not in used:
                used.append(complex_nrs[j])
                length += 1
            else:
                break
            j += 1
        if length > maxLength:
            maxLength = length
            start = i
            end = j

    return complex_nrs[start:end]


def longest_increasing_subsequence_of_modulus(complex_nrs:list):
    '''
    The function is searching for the longest increasing subsequence considering the modulus of the numbers
    @param complex_nrs: list of complex numbers
    @return: the elements of the longest increasing subsequence of modulus
    '''
    n = len(complex_nrs)
    maxLength = 0
    idxMaxLength = -1
    lis = [] # list of longest increasing subsequence
    precedent = [] # list for knowing who is the precedent of an element

    # constructing the list of modulus + initialising the lis and precedence list
    list_of_modulus = []
    for e in complex_nrs:
        list_of_modulus.append(modulus(e))
        lis.append(1)
        precedent.append(-1)

    # finding the longest increasing subsequence of modulus
    for i in range(1, n):
        for j in range(i):
            if list_of_modulus[j] < list_of_modulus[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
                if lis[i] > maxLength:
                    maxLength = lis[i]
                    idxMaxLength = i
                precedent[i] = j

    # constructing the result list
    result = []
    while idxMaxLength != -1:
        result.append(complex_nrs[idxMaxLength])
        idxMaxLength = precedent[idxMaxLength]

    result.reverse()

    return result



#The other functions

def to_str(a):
    return str(get_real(a)) + " + " + str(get_img(a)) + "i"

def modulus(z):
    return (get_real(z) ** 2 + get_img(z) ** 2) ** (1/2)


