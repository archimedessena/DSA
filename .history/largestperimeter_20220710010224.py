class Solution:
    def largestPerimeter(self, nums) -> int:
        n = sorted(nums)[::-1] # sort but it should be in the reverse form
        print(n)
        for i in n(len(n) - 2):
            if n[i] < n[i + 1] + n[i + 2]:
                return n[i] + n[i + 1] + n[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))