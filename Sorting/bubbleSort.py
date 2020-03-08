def bubbleSort(a):
    n=len(a)
    for iterationNo in range(1,n+1):
        # Here we have n number of iterations.
        # At the end of each, we have the highest element at the end.
        for j in range(n-iterationNo):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


print(bubbleSort([4,6,3,-2,9,0]))