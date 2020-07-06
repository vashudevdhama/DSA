'''
We divide the array in two half (sorted and unsorted)  and take minimum element from the unsorted half and put that at it's best place.
Suitable when we need to minimize the number of swaps like in HDD files sorting.
Worst Time Complexity: O(n^2).
Avg Time Complexity: O(n^2).
Space complexity: O(1).
In-place algorithm.
Not Stable algorithm.
'''


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
