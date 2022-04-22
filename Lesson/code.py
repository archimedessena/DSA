# merge sorted array
# function to merge a sorted array

# merge sorted array frm 


def merge_sorted_array(arr, arrr):
    if len(arr) == 0 and len(arrr) == 0:
        return arr + arrr
    # if that is not the case then this
    arrs = []
    num = 0 # init
    nums = 0   # init
    while num < len(arr) and nums < len(arrr):
        if arr[num] <= arrr[nums]:
            arrs.append(arr[num])
            num+=1   
        elif  arrr[nums] < arr[num]:
            arrs.append(arrr[nums])
            nums+=1
    return arrs


sorted_array = merge_sorted_array([1, 2, 3, 4, 5, 6,], [7, 8, 9])
print(sorted_array)