def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        # Value to be inserted.
        value = a[i]
        # current probable index
        currentProbableIndex = i
        # current probable index for insertion. We need to verify is the current probable index is correct or not.
        # For that we compare value to be inserted to the value just before the current probable index. If value just
        # before the current probable index is smaller than the value to be inserted. We are sure that current
        # probable index is the place of insertion.

        while (currentProbableIndex > 0 and a[currentProbableIndex - 1] > value):
            # we exit the loop when:
            # 1. currentProbableIndex=0
            # 2. Element just before the currentProbableIndex is smaller than the value, thus we know that currentProbableIndex is the position for the value.
            a[currentProbableIndex] = a[currentProbableIndex - 1]
            currentProbableIndex = currentProbableIndex - 1
        # Here we are sure that currentProbableIndex is the correct index for insertion so we insert.
        a[currentProbableIndex] = value
    return(a)
print(insertionSort([5,3,2,0,1,6,-8]))
