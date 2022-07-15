# selection sort algorithm
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




our_list = [5, 3, 6, 2, 10, 23, 78, 89, 12, 4, 6, 89, 2, 57, 84, 35, 67, 56783, 78, 23, 56, 7889, 5, 6, 6, 8, 2, 4, 56, 7, 433, 7, 8, 9, 0, 7, 4, 3, 22, 4, 5, 66, 789, 2, 33, 44, 5, 5, 6778, 9, 900, 5667, 89, 123, 4556, 778, 990, -1, 23]
print(len(our_list))
print(findSmallest(our_list))
print(selectionSort(our_list))




# def my_number(a):
#     smallest_number = a[0]
#     smallest_number_position = 0
#     for i in range(1, len(a)):
#         if a[i] < smallest_number:
#             smallest_number = a[i]
#             smallest_number_position = i
#         return smallest_number

# def sort_me(a):
#     new = []
#     for i in range(len(a)):
#         smallest_number = my_number(a)
#         new.append(a.pop(smallest_number))
#     return new



# our_list = [5, 3, 6, 2, 10, 23, 78, 89, 12, 4, 6, 89, 2, 57, 84, 35, 67, 56783, 78, 23, 56, 7889, 5, 6, 6, 8, 2, 4, 56, 7, 433, 7, 8, 9, 0, 7, 4, 3, 22, 4, 5, 66, 789, 2, 33, 44, 5, 5, 6778, 9, 900, 5667, 89, 123, 4556, 778, 990, 23]

# print(my_number(our_list))






