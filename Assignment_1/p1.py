# Solve the problem from the first set here
def largestNumberFromN(n):
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    newN = 0
    #making the characteristic list
    while n != 0:
        c[n % 10] += 1
        n = n // 10
    #building the largest number from N
    for i in range(9, -1, -1):
        while c[i]:
            newN = newN * 10 + i
            c[i] -= 1
    return newN

n = int(input("Enter a number and I'll give you the largest number that can be created from it: "))
print(largestNumberFromN(n))

