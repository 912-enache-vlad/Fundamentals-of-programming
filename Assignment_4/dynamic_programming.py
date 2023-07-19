from tabulate import tabulate
def dp(s:list, sum:int):
    res = []
    d1 = [[0 for x in range(sum + 1)] for x in range(len(s))]
    d2 = [[0 for x in range(sum + 1)] for x in range(len(s))] # -1 = not used and 1 = used

    for i in range(1, len(s)):
        for j in range(1, sum + 1):
            if j < s[i]:
                d1[i][j] = d1[i-1][j]
                d2[i][j] = -1 # not used
            elif d1[i-1][j] < s[i] + d1[i-1][j - s[i]]:
                d1[i][j] = s[i] + d1[i-1][j - s[i]]
                d2[i][j] = 1 # used
            else:
                d1[i][j] = d1[i - 1][j]
                d2[i][j] = -1  # not used

    i = len(s) - 1
    j = sum
    while i > 0 and j > 0:
        if d2[i][j] == -1:
            i = i - 1
        else:
            j = j - s[i]
            res.append(s[i])
            i = i - 1

    #printing the result
    res.reverse()
    print(res)

    #printing the matrices used
    for i in range(len(s)):
        d1[i][0] = d2[i][0] = s[i]
    for i in range(sum + 1):
        d1[0][i] = d2[0][i] = i
    print()
    print(tabulate(d1, tablefmt="fancy_grid"))
    print("""
        -1 means that the element is not used
        1 means that the element is used""")
    print(tabulate(d2, tablefmt="fancy_grid"))


ok = False
res = []
s = []
used = []


def back_iter(s:list, sum:int):
    csum = 0
    global ok
    array = [-1, -1]
    while len(array) > 1:
        chosen = False
        while not chosen and array[-1] < 1 and len(array) <= len(s):
            array[-1] += 1
            if array[-1] == 1:
                res.append(s[len(array) - 1])
                csum += s[len(array) - 1]
            chosen = (csum <= sum)
        if chosen:
            if csum == sum and array[-1]:
                print(res)
            array.append(-1)
        else:
            if array[-1] == 1:
                res.pop()
                csum -= s[len(array) - 1]
            array.pop()


def used_interface():
    s = []  # initialising the set list
    n = int(input("How long is the set you want to enter: "))
    for i in range(n):
        x = int(input("Enter number " + str(i + 1) + ":"))
        s.append(x)
    sum = int(input("Enter the number k:"))

    s.insert(0, 0)  #

    option = int(input("""
        What version of solving the problem do you want to use?
        1 - Dinamic verion (the matrices used for solving it will be displayed)
        2 - Naiv version
        Enter the number:
        """))
    if option == 1:
        dp(s, sum)
    elif option == 2:
        back_iter(s, sum)

used_interface()