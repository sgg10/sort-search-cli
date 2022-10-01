def quicksort(collection):
    if len(collection) <= 1:
        return collection
    else:
        pivot = collection[0]
        return (
                quicksort([x for x in collection[1:] if x < pivot]) +
                [pivot] +
                quicksort([x for x in collection[1:] if x >= pivot])
        )
