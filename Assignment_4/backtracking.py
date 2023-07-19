from tabulate import tabulate
'''
    A number of `n` coins are given, with values of a<sub>1</sub>, ..., a<sub>n</sub>
    and a value `s`. Display all payment modalities for the sum `s`.
    If no payment modality exists print a message.
'''

ok = False
res = []
v = []
used = []


def back_rec(ind:int, csum:int, sum:int): #index in list values, curent sum, total sum
    i = 0
    global ok
    while i <= 1 and v[ind] * i + csum <= sum:
        used[ind] = i
        if i == 1:
            res.append(v[ind])
        if v[ind] * i + csum == sum :
            print(res)
            ok = True
        elif v[ind] * i + csum <= sum and ind < len(v) - 1:
            back_rec(ind + 1, v[ind] * i + csum, sum)
        if i == 1:
            res.pop()
        used[ind] = 0
        i += 1



def back_iter(sum:int):
    csum = 0
    ind = 0
    global ok
    array = [-1]
    while len(array) > 0:
        chosen = False
        while not chosen and array[-1] < 1 and len(array) <= len(v):
            array[-1] += 1
            if array[-1] == 1:
                res.append(v[len(array) - 1])
                csum += v[len(array) - 1]
            chosen = (csum <= sum)
        if chosen:
            if csum == sum and array[-1]:
                print(res)
                ok = True
            array.append(-1)
        else:
            if array[-1] == 1:
                res.pop()
                csum -= v[len(array)-1]
            array.pop()






def interracting_with_the_user():
    n = int(input("How many coins?:"))



    for i in range(n):
        print("The value of coin", i + 1, ":", end=" ")
        x = int(input())
        v.append(x)
        used.append(0)

    sum = int(input("Enter the amount: "))

    v.sort()

    option = int(input("""
    1 - for Recursive version
    2 - for Iterative version
    Enter the number:"""))
    if option == 1:
        print("Recursive version: ")
        back_rec(0, 0, sum)
    elif option == 2:
        print("Iterative version: ")
        back_iter(sum)

    if ok is False:
        print("There are no methods to pay the sum with the given values of coins")



interracting_with_the_user()
