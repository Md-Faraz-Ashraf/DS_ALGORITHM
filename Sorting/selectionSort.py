def selectionSort(a):
    for staringIndex in range(0,len(a)):
        min = a[staringIndex]
        for i in range(staringIndex,len(a)):
            if a[i] <= min:
                min = a[i]
                minIndex = i
        a[staringIndex],a[minIndex]=a[minIndex],a[staringIndex]
    print(a)

selectionSort([4,3,6,-3,0,9,-8])



