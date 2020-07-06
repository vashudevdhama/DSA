'''
Repeatedly breaks down a list into several sublists until each sublist consists of a single element and merging those sublists in a manner that results into a sorted list.
Divide and Conquer approach.    
Worst Time Complexity: O(nlog(n)).
Best Time Complexity: O(nlog(n)).
Space complexity: O(n).
Not-In-place algorithm.
Stable algorithm.
'''


def merge_sort(arr):
    size = len(arr)
    if size < 2:
        return
    mid = size//2
    l = arr[:mid]
    r = arr[mid:]
    merge_sort(l)
    merge_sort(r)
    merge(l, r, arr)


def merge(l, r, arr):
    i, j, k = 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1
