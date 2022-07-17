# A sequence of numbers is called an arithmetic progression 
# if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the 
# array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] 
# with differences 2 and -2 respectively, between each consecutive elements.
# Example 2:

# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

# Constraints:

# 2 <= arr.length <= 1000
# -106 <= arr[i] <= 106


# Pseudocode 
# 1. Sort array 
# 2. Check if the difference in the consecutive elements is the same

arr1 = [2, 4,23, 32, 10, 1]
arr2 = [2, 6, 4, 8, 10]

arr3 = [1,3,]

class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        m = min(arr)
        print(m)
        print(max(arr))
        gap = (max(arr) - m) / (len(arr) - 1)
        print(gap)
        if gap == 0: return True
        s = set(num - m for num in arr)
        print(s)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)
    
    
    
    
soln = Solution()
print(soln.canMakeArithmeticProgression(arr2))  
    
    
