class Solution:
    def largestPerimeter(self, A):
        A = sorted(A)[::-1]
        for i in range(len(A) - 2): # getting the last two elements of the            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))