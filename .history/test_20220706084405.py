# count the number of bit in a binary  

bin_num = 101010101010101001010101010101010010001010100001111 

def hamming_weight(self, num):
    """
    :type n: int
    :rtype: int
    """
    num = 0
    while num:
        num &= num - 1
        num +=1    
    return num

print(hamming_weight(bin))
    