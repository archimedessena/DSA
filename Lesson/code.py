numbers = [1, 2, 3, 9] # 9

numberss = [1, 2, 4, 4] # 8

def pair(arr, target):
    for i in arr:
        for j in arr:
            if i + j == target:
                return i, j 
            else:
                return None
    return i, j


print(pair([1, 2, 3, 9], 4))