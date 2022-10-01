def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result


def mergesort(collection):
    if len(collection) <= 1:
        return collection

    half = len(collection) // 2
    left = mergesort(collection[:half])
    right = mergesort(collection[half:])

    return merge(left, right)
