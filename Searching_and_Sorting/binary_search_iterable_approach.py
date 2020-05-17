arr = [1,2,3,4,5,6,7,9,11,14,19]
value = 11
# Note: input_array must be sorted before passing as parameter in binary_search function.
def binary_search(input_array, value):
    low = 0
    high = len(input_array)-1
    while low <= high:
        mid = (low + high)//2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        elif input_array[mid] > value:
            high = mid - 1
    return -1

print(binary_search(arr, value))

    
        
