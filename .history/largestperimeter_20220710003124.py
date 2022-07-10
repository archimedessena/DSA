class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n =  nums.sort()
        return n
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))