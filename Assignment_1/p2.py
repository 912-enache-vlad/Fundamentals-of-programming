# Solve the problem from the second set here

def TwinPrimeNumbersLargerThanN(n):
    # Making the Sieve Of Eratosthenes
    sieve = [False] * 1000000
    sieve[0] = sieve[1] = True
    i = 0
    while i * i < 1000000 :
        if(sieve[i] == False): # if it is a prime number
            j = 2
            while(i * j < 1000000):
                sieve[i * j] = True
                j += 1
        i += 1
    #searching for the twin prime numbers
    found = False
    p1 = n + 1
    while(found == False):
        if(sieve[p1] == False and sieve[p1 + 2] == False):
            found = True
            return p1, p1 + 2
        p1 += 1

n = int(input('Enter a number and I will give to you two prime numbers bigger than N that has the difference between them of 2: '))
print(TwinPrimeNumbersLargerThanN(n))