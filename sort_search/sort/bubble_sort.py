def bubble_sort(collection):
    for i in range(1, len(collection)):
        for j in range(len(collection) - i):
            if collection[j+1] < collection[j]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    return collection
