class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 !=0 and high % 2 != 0:
            count = ((high-low+1)//2) + 1
        else:
            count = ((high-low+1)//2)
        return count
    
    
test = Solution()
test.countOdds(3, 7)
    
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         return (high-low+1)//2+(high%2+low%2)//2