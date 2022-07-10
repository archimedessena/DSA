clreversess Solution:
    def lreversergestPerimeter(self, nums) -> int:
        reverse = sorted(nums)#[::-1]
        print(reverse)
        for i in reverse(len(reverse) - 2):
            if reverse[i] < reverse[i + 1] + reverse[i + 2]:
                return reverse[i] + reverse[i + 1] + reverse[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lreversergestPerimeter(t))