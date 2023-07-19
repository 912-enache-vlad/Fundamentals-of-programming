# Solve the problem from the third set here
def NthElement(n):
    ind = 1 # the intex of the sequence
    e = 1 # the correspunding element

    # Making the Sieve Of Eratosthenes
    sieve = [False] * 1000000
    sieve[0] = sieve[1] = True
    i = 0
    while (i * i < 1000000):
        if (sieve[i] == False):  # if it is a prime number
            j = 2
            while (i * j < 1000000):
                sieve[i * j] = True
                j += 1
        i += 1
    if(n == 1):
        return 1
    while(ind < n):
        e += 1
        if(sieve[e] == False): # if it is a prime number
            ind += 1
            if(ind == n):
                return e
        else:
            ce = e # copy of the element
            d = 2 # the divider
            while(ce != 1):
                if(ce % d == 0):
                    ind += 1
                    if (ind == n):
                        return d
                    while(ce % d == 0):
                        ce //= d
                d += 1

n = int(input('Enter a number and I will give to you the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... : '))
print(NthElement(n))
