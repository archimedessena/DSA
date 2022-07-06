# Binary search algorithm in python 
def binary_search(list, item):
    low = 0 # low position
    high = len(list) - 1 # highest number and position

    while low <= high:  # While you haven`t narrowed it down to one element
        mid = (low + high)  # check middle element
        guess = list[mid]
        if guess == item: # found item
            return mid
        if guess > item: # guess was too high
            high = mid - 1
        else: # guess was too high
            low = mid + 1
    return None # item does not exist 


my_list = [100, 99, 98, 97, 96, 95]

print(binary_search(my_list, 95))


# binary search algo with O(log n)
def binary_one(arr, items):
    lowest = 0
    highest = len(arr) - 1
    while lowest <= highest: 
        mid = (lowest + highest)
        guesses = arr[mid]
        if guesses == items:
            return mid
        if guesses > items:
            highest = mid - 1
        else: 
            low = mid + 1
    return None




my_list = [100, 99, 98, 97, 96, 95]

print(binary_one(my_list, 100))   