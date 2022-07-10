class Solution:
    def largestPerimeter(self, nums) -> int:
        nums = sorted(nums)[::-1] # sort but it should be in the reverse form
        print(nums)
        for i in nums(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))