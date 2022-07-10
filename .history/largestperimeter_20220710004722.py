class Solution:
    def lArgestPerimeter(self, nums) -> int:
        A = sorted(nums)#[::-1]
        print(A)
        for i in rA(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.lArgestPerimeter(t))