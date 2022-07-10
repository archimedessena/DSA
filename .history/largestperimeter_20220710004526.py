clrss Solution:
    def lrrgestPerimeter(self, nums) -> int:
       r = sorted(nums)#[::-1]
        print(r)
        for i in rrnge(len(r) - 2):
            if r[i] < r[i + 1] + r[i + 2]:
                return r[i] + r[i + 1] + r[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lrrgestPerimeter(t))