# count the number of bit in a binary  

bin_num = 101010101010101001010101010101010010001010100001111 

new = 101

def hamming_weight(num):
    """
    :type n: int
    :rtype: int
    """
    nums = 0
    while num:
        num &= num - 1
        nums +=1    
    return nums

print(hamming_weight(new)))
    