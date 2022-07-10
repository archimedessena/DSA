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
     def subtractProductAndSum(self, n: int) -> int:
        sum, prod = 0, 1
        while n:
            digit = n % 10
            sum += digit
            prod *= digit
            n //= 10
        return prod - sum
    
    


test = Solution()
test.subtractProductAndSum(5678)

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         arr = list(map(int, str(n)))
#         return prod(arr)-sum(arr)