def linear_search(collection, element):
    for i in range(collection):
        if collection(i) == element:
            return i
    return -1
