# count the number of bit in a binary   

def hamming_weight(num):
    """
    :type n: int
    :rtype: int
    """
    num = 0
    while num:
        num &= num - 1
        num +=1    
    return num


bin = 000101010101010101001010101010101010010001010100001111


print(hamming_weight(binary))
    