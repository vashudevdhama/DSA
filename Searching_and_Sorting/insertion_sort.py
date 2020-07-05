'''
Pick an element and insert it at its correct sorted position.
Best suited for the array which is partially sorted.
Worst Time Complexity: O(n^2) But it's more efficient than other O(n^2) selection and buble sort because of lesser number of swaps and comparisions.
Best Time Complexity: O(n).
Space complexity: O(1).
Inplace algorithm.
Stable algorithm.
'''


def insertion_sort(arr):
    arr_size = len(arr)
    for i in range(1, arr_size):
        temp_val = arr[i]
        index = i
        while(index > 0 and temp_val < arr[index-1]):
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = temp_val
    return arr
