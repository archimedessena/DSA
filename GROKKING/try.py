# Selection sort algorithm
# Finding the smallest element in a list 

# Pseudocode 
# first find the smallest number
# Go through the entire list 
# Search for the smallest element and put it in a container 
# Go through the list again and if there is any element smaller than the earlier on found
# small element then use it to replace it  
# Keep doing it till the whole list is sorted 


class Sorting:
    def __init__(self, arr):
        self.arr = arr
        
        
    def smallest_number(self, arr):
        # assign the smallest number to the first number in the arr
        smallest = arr[0]
        # smallest number`s position or index
        smallest_index = 0
        # go through the entire arr and search for the smallest number
        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = 0
        return smallest_index
        
        



a = [12, 34, -1, 57,133, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
v = Sorting(a)
print(v.smallest_number(a))



