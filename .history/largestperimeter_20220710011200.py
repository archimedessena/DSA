class Solution:
    def largestPerimeter(self, A):
        A = sorted(A)[::-1] # sort elements but give it out in the reverse 
        for i in range(len(A) - 2): # getting the last two elements of the for loop           if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
    
    
test = Solution()
t = [2, 1, 2]
print(test.largestPerimeter(t))