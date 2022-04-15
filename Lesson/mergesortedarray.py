class Solution(object):
       def merge(self, nums1, m, nums2, n):
      i = 0
      j = 0
      end = len(nums1)-1
      while end>=0 and not nums1[end]:
         end-=1
      while j<len(nums2) :
         if i>end and not nums1[i]:
            nums1[i] = nums2[j]
            j+=1
         elif nums1[i]>nums2[j]:
            self.shift(nums1,i)
            nums1[i] = nums2[j]
            end+=1
            j+=1
         i+=1
      return nums1
   def shift(self,num,i):
      j = len(num)-1
      while not num[j]:
         j-=1
      while j>=i:
         num[j+1] = num[j]
         j-=1
ob = Solution()
print(ob.merge([1,2,3,0,0,0],3,[2,5,6],3))








# Python program to merge
# two sorted arrays

# Merge arr1[0..n1-1] and
# arr2[0..n2-1] into
# arr3[0..n1+n2-1]
def mergeArrays(arr1, arr2, n1, n2):
	arr3 = [None] * (n1 + n2)
	i = 0
	j = 0
	k = 0

	# Traverse both array
	while i < n1 and j < n2:
	
		# Check if current element
		# of first array is smaller
		# than current element of
		# second array. If yes,
		# store first array element
		# and increment first array
		# index. Otherwise do same
		# with second array
		if arr1[i] < arr2[j]:
			arr3[k] = arr1[i]
			k = k + 1
			i = i + 1
		else:
			arr3[k] = arr2[j]
			k = k + 1
			j = j + 1
	

	# Store remaining elements
	# of first array
	while i < n1:
		arr3[k] = arr1[i];
		k = k + 1
		i = i + 1

	# Store remaining elements
	# of second array
	while j < n2:
		arr3[k] = arr2[j];
		k = k + 1
		j = j + 1
	print("Array after merging")
	for i in range(n1 + n2):
		print(str(arr3[i]), end = " ")

# Driver code
arr1 = [1, 3, 5, 7]
n1 = len(arr1)

arr2 = [2, 4, 6, 8]
n2 = len(arr2)
mergeArrays(arr1, arr2, n1, n2);

# This code is contributed
# by ChitraNayal

