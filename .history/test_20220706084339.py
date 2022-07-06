# count the number of bit in a binary   

def hamming_weight(selfnum):
    """
    :type n: int
    :rtype: int
    """
    num = 0
    while num:
        num &= num - 1
        num +=1    
    return num

print(hamming_weight(binary))
    