# Pseudocode for binary search

# Search for a particular number among a list of sorted numbers
# Start from the middle
        # assign the first number as lowest 
        # the last number in the array as the highest number
# If the middle number is equal to the number then the return the middle numbers position
# if it is less then 
    # the high is mid minus one
# else the low is mid plus 1


def binary(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + high
        mid_num = arr[mid]
        if mid_num < high:
            low = mid + 1
        elif mid_num == target:
            return mid
        else:
            high = mid - 1 
    return -1


nu = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary(nu, 9))