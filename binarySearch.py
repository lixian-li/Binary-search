
# recursive binary search
averagecost = 0
def binary_search(alist, key):
    n = len(alist)

    if n > 0:
        mid = n // 2

        if alist[mid] == key:
            return True
        elif key < alist[mid]:
            return binary_search(alist[:mid], key)
        else:
            return binary_search(alist[mid + 1:], key)
    return False


# non-recursive binary search
def binary_search_2(alist, item):
    n = len(alist)
    averagecost = 0
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            averagecost=averagecost+1
            return averagecost
        elif item < alist[mid]:
            averagecost=averagecost+1
            last = mid - 1
        else:
            averagecost=averagecost+1
            first = mid + 1
    return averagecost


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 55, 77, 93]
    print(binary_search(li, 17))
    print(binary_search(li, 100))
    print(binary_search_2(li, 55))
    print(binary_search_2(li, 100))
