# brute force solution
def compare(arr, arr1):
    for i in len(arr):
        for j in len(arr1):
            if i == j:
                return True
    return False 
   


arr3 = [1, 2, 4, 5]
arr4 = [1, 3, 5, 6]
print(compare(arr3, arr4))