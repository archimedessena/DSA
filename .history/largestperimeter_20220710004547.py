clss Solution:
    def lrgestPerimeter(self, nums) -> int:
        = sorted(nums)#[::-1]
        print()
        for i in rnge(len() - 2):
            if [i] < [i + 1] + [i + 2]:
                return [i] + [i + 1] + [i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lrgestPerimeter(t))