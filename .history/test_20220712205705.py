#Given an integer number n, return the difference between 
# the product of 
# its digits and 
# the sum of its digits.


# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# Constraints:

# 1 <= n <= 10^5

class Solution:
    def product_sum_subtract(self, n):
        sum = 0
       product = 1   
       while n:
           num = n % 10   
           sum += num    
           product *= num  
           n //= 10  
        return product - sum
    

test = Solution()
test1 = test.product_sum_subtract(5678)
print(test1)
    