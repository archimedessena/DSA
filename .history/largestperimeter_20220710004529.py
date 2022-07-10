clreverse_ss Solution:
    def lreverse_rgestPerimeter(self, nums) -> int:
       reverse_ = sorted(nums)#[::-1]
        print(reverse_)
        for i in rreverse_nge(len(reverse_) - 2):
            if reverse_[i] < reverse_[i + 1] + reverse_[i + 2]:
                return reverse_[i] + reverse_[i + 1] + reverse_[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lreverse_rgestPerimeter(t))