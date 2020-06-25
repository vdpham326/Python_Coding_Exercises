# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
    arr = []
    arr.append(a[len(a) / 2])
    arr.append(b[len(b) / 2])

    return arr