class Solution:
    def largestPerimeter(self, nums) -> int:
        reverse_sort = sorted(nums)[::-1] # sort but it should be in the reverse form
        print(reverse_sort)
        for i in reverse_sort(len(reverse_sort) - 2):
            if reverse_sort[i] < reverse_sort[i + 1] + reverse_sort[i + 2]:
                return reverse_sort[i] + reverse_sort[i + 1] + reverse_sort[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))