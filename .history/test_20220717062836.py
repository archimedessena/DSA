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
# 1. Search for the smallest number of element in the array

# 2. search the maximum element as well    
3. find the difference between the min and the max and divide it by the length of the array minus 1

4. division has a reminder of 0, then the array has arithmetic progression which is true  

5. Create a set to 

