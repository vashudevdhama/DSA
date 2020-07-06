'''
We pick a pivot element and make sure that all elements left to pivot are smaller than pivot and all elements right to pivot are greater than pivot.
Divide and conquer approach.
Worst Time Complexity: O(n^2).
Avg Time Complexity: O(nlog(n)).
Space complexity: O(1).
In-place algorithm.
Not Stable algorithm.
'''


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot_index = partition(arr, start, end)
    quick_sort(arr, start, pivot_index-1)
    quick_sort(arr, pivot_index+1, end)


def partition(arr, start, end):
    pivot = arr[end]
    pivot_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return pivot_index
