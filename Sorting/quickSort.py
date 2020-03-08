def quickSort(a,start,end):
    if start>end:
        return
    if(start<end):
        pi=quickSortLeftRightPartition(a,start,end)
        quickSort(a,start,pi-1)
        quickSort(a,pi+1,end)
    return a

def quickSortPartition(a,start,end):
    # Pivot element is the one which needs to be at its sorted position in the pass.
    pivot=a[end]
    PartitionIndex=start
    # We make sure that any point PartitionIndex has only elements smaller than pivot to it's left.
    # As while iterating if we find an element smaller than pivot
    # it means that it has to be pushed before PartionIndex. Thus we, swap(a[pi],a[i])
    # And then increase Pi to the next location.
    for i in range(start,end):
        # Here we are just determining the partion Index.
        if a[i]<=pivot:
            # We need to send all elements smaller than or equal to pivot behind Pi.
            # If element is smaller than pivot we swap
            # with element at PartitionIndex, and increase Partition index by 1.
            a[i],a[PartitionIndex]=a[PartitionIndex],a[i]
            PartitionIndex=PartitionIndex+1
    # Once Partition Index is determined we need to put our pivot here, so we swap.
    a[PartitionIndex], a[end] = a[end], a[PartitionIndex]
    # We need to return the PartionIndex so that left and right unsorted arrays can be determined.
    return PartitionIndex

def quickSortLeftRightPartition(a,start,end):
    left=start
    right=end
    pivot=a[end]
    while(left<right):
        if a[left]<pivot:
            left=left+1
        if a[right]<pivot:
            right=right-1
        if left<=right:
            a[right],a[left]=a[left],a[right]
            left=left+1
            right=right-1
    return left





#print("Sorted", quickSortPythonic([7,3,4,1,8,2,0,6,9,5],0,9))





















