def linearSearch(a, key):
    for element in a:
        if element == key:
            return 'Found'
    return 'Not Found'


def binarySearch(a, key):
    n = len(a)
    if n == 1:
        if a[0] == key:
            return 'Found'
        return 'Not Found'
    mid = n // 2
    if a[mid] == key:
        return 'Found'
    elif a[mid] <= key:
        return binarySearch(a[mid:], key)
    else:
        return binarySearch(a[:mid], key)



