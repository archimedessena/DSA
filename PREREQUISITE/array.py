arr = [1, 3, 5, 7, 9, -5]
def find_smallest():
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

#print(find_smallest())

arr1 = [2, 4, 6, 8, 10, -2]
arr1.append(12)
arr1.insert(0, 45)
arr1.remove(6)
arr1.sort()

def find_largest():
    largest = arr1[0]
    for num in arr1:
        if num > largest:
            largest = num
    return largest

def do_something():
    if find_largest() > find_smallest():
        return "Largest is greater than smallest"
    else: print("Sleep is calling")
    
    
print(do_something())