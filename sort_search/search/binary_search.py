def binary_search(collection, element, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if element == collection[mid]:
            return mid
        elif element > collection[mid]:
            return binary_search(collection, element, mid+1, high)
        return binary_search(collection, element, low, mid-1)
    return -1
