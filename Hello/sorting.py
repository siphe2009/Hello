def bubble_sort(items):
    """ Implementation of bubble sort """
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''

    if len(items) < 2:
        return items
    result = []
    mid = int(len(items) / 2)
    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    index = -1

    if len_i <= 1:

        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
