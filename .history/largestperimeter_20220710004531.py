clreverse_soretss Solution:
    def lreverse_soretrgestPerimeter(self, nums) -> int:
       reverse_soret = sorted(nums)#[::-1]
        print(reverse_soret)
        for i in rreverse_soretnge(len(reverse_soret) - 2):
            if reverse_soret[i] < reverse_soret[i + 1] + reverse_soret[i + 2]:
                return reverse_soret[i] + reverse_soret[i + 1] + reverse_soret[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lreverse_soretrgestPerimeter(t))