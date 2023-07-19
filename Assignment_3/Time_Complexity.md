# Time Complexity

## Selection Sort
    
    As there are 2 nested loops, the time complexity for Selection Sort is:
    -O(n) for the loop that selects an element from the array one by one and
    -O(n) for the loop to compare that element with each other from the loop
    Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N^2)

### The Best Case - O(n^2)

### The Worst Case - O(n^2)

    Unfortunately, the time complexity for Best, Worst and Average are all the same. 
    Regardless of the placing of the elements, at every step,
    the algorithm is searching the minimum element from the index i untill the end.

## Comb Sort

### The Best Case - O(nlog(n))

    The best configuration occurs when all the elements are already sorted or nearly sorted. 
    In this case, the loop with gap=1 will be run only once (as the others).

### The Worst Case - O(n^2)

    It occurs when the array elements are required to be sorted in reverse order. 
    That means suppose you have to sort the array elements in ascending order, but its elements are in descending order. 
    The worst-case time complexity of comb sort is O(n2)