class Solution:
    def largestPerimeter(self, nums) -> int:
      reverse_sort = sorted(nums)#[::-1]
        print(a)
        for i in range(len(a) - 2):
            if a[i] < a[i + 1] + a[i + 2]:
                return a[i] + a[i + 1] + a[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))