# using recursion in binary search algo
def bsearch(list, indx0, indxn, val):
    if indxn < indx0:
        return None
    else:
        midval = indx0 + ((indxn - indxn - indx0) // 2)

# compare the search item with middle most value
        if list[midval] > val:
            return bsearch(list, indx0, midval - 1, val)
        elif list[midval] < val:
            return bsearch(list, midval + 1, indxn, val)
        else:
            return midval


list = [8, 11, 24, 56, 88, 131]
print(bsearch(list, 0, 5, 24))  # 2
print(bsearch(list, 0, 5, 51)) #None
