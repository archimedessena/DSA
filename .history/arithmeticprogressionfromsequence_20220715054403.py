# A sequence of numbers is called an arithmetic progression 
# if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the 
# array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] 
# with differences 2 and -2 respectively, between each consecutive elements.
# Example 2:

# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

# Constraints:

# 2 <= arr.length <= 1000
# -106 <= arr[i] <= 106


# Pseudocode 
# 1. Sort array 
# 2. Check if the difference in the consecutive elements is the same

arr = [2, 4,23, 32, 10, 1]


def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#Now you can use this function to write selection sort:
def selectionSort(arr): #Sorts an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # Finds the smallest element in the array, and adds it to the new array
        newArr.append(arr.pop(smallest))
    return newArr


    