arr = [1, 3, 5, 7, 9, -5]
def find_smallest():
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

#print(find_smallest())

arr1 = [2, 4, 6, 8, 10, -2]
arr1.append(12)
arr1.insert(0, 45)
arr1.remove(6)
arr1.sort()

def find_largest():
    largest = arr1[0]
    for num in arr1:
        if num > largest:
            largest = num
    return largest

def do_something():
    if find_largest() > find_smallest():
        return "Largest is greater than smallest"
    else: print("Sleep is calling")
    
    
#print(do_something())

list_comprehension = [x for x in arr1 if x > 5]   
#print(list_comprehension)

def list_com(arr1):
    return [x for x in arr1 if x >= 10]

arr2 = [3, 45, 29, 10, 8, 6, 2, 1, 0, -1, -5, -10, -20]
arr2.sort()

greater_or_equal_to_ten = list_com(arr2)
#print(greater_or_equal_to_ten)
   
   
# Arrays: Organise items sequentially, allowing for efficient access and manipulation.
# Lists: Similar to arrays, but more flexible in Python, allowing for mixed data types and dynamic resizing.
# Tuples: Immutable sequences, useful for fixed collections of items.
# Sets: Unordered collections of unique items, useful for membership testing and eliminating duplicates 

# Properties  of arrays: include fixed size, efficient indexing, and contiguous memory allocation. 
# List of all methods of python's list: They are append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy.



# # Big-O time complexities for Python list methods

# 1. append(x)
# Adds an item x to the end of the list
# Time Complexity: O(1) amortized
# - Appending is constant time on average, but resizing (when the array is full) is O(n).
# - Python over-allocates memory, making resizing rare, so amortized O(1).
my_list = [1, 2, 3]
my_list.append(4)  # O(1) amortized

# 2. extend(iterable)
# Extends the list by appending all elements from the given iterable
# Time Complexity: O(k) where k is the length of the iterable
# - Each element is appended (O(1) amortized), so total time depends on the iterable's length.
my_list.extend([5, 6])  # O(k), k=2 here

# 3. insert(i, x)
# Inserts item x at index i (index i shifts to the right)
# Time Complexity: O(n) where n is the list length
# - Elements after index i must be shifted right, which takes O(n) in the worst case.
my_list.insert(1, 'a')  # O(n)

# 4. remove(x)
# Removes the first occurrence of x; raises ValueError if x not found
# Time Complexity: O(n)
# - Requires scanning the list to find x (O(n)) and shifting elements after it (O(n)).
my_list.remove('a')  # O(n)

# 5. pop([i])
# Removes and returns item at index i; defaults to last item if i not specified
# Time Complexity: O(1) for pop() (last item), O(n) for pop(i)
# - Popping the last item is O(1) as no elements need shifting.
# - Popping at index i requires shifting elements after i, which is O(n).
item = my_list.pop()  # O(1)
item = my_list.pop(1)  # O(n)

# 6. clear()
# Removes all items from the list
# Time Complexity: O(1)
# - Python sets the list's length to 0, leaving memory cleanup to the garbage collector.
my_list.clear()  # O(1)

# 7. index(x[, start[, end]])
# Returns index of first occurrence of x; raises ValueError if x not found
# Time Complexity: O(n)
# - Requires scanning the list (or slice) to find x, which takes O(n) in the worst case.
my_list = [1, 2, 3, 2]
index = my_list.index(2)  # O(n)

# 8. count(x)
# Returns the number of times x appears in the list
# Time Complexity: O(n)
# - Requires scanning the entire list to count occurrences of x.
count = my_list.count(2)  # O(n)

# 9. sort(key=None, reverse=False)
# Sorts the list in place
# Time Complexity: O(n log n)
# - Uses Timsort algorithm, which is O(n log n) on average and in the worst case.
# - Best case (nearly sorted) is O(n).
my_list = [3, 1, 2]
my_list.sort()  # O(n log n)

# 10. reverse()
# Reverses the list in place
# Time Complexity: O(n)
# - Requires swapping elements from both ends, processing all n elements.
my_list.reverse()  # O(n)

# 11. copy()
# Returns a shallow copy of the list
# Time Complexity: O(n)
# - Creates a new list and copies all elements, which takes O(n).
new_list = my_list.copy()  # O(n)

# Note: Non-method operations and their complexities:
# - Indexing: my_list[0]  # O(1)
# - Slicing: my_list[1:3]  # O(k) where k is the slice length
# - Concatenation: my_list + [4, 5]  # O(n + k) where k is the length of the added list
# - Length: len(my_list)  # O(1)
# - Membership: 3 in my_list  # O(n)





# Understanding "amortized" in the context of time complexity

# Definition of Amortized Time Complexity:
# - Amortized time complexity refers to the average time cost per operation when performing a sequence of operations.
# - It accounts for occasional expensive operations (like resizing a dynamic array) by spreading their cost over many operations.
# - For Python lists, this is relevant for methods like append(), where most operations are fast, but some trigger costly resizing.

# Example with append():
# - The append() method adds an item to the end of a list, typically in O(1) time.
# - Python lists are implemented as dynamic arrays, which have a fixed size in memory.
# - When the array is full, Python allocates a larger array (usually doubling the size) and copies all elements, which is O(n).
# - Because resizing happens infrequently (e.g., when the list size doubles), the total cost of n appends is roughly O(n).
# - This averages out to O(1) per append, hence "amortized O(1)".

my_list = []
for i in range(1000):
    my_list.append(i)  # O(1) amortized
    # Most appends are O(1), but resizing (e.g., at sizes 8, 16, 32, ...) is O(n).
    # Over many appends, the average cost per operation is O(1).

# Why "amortized"?
# - The term comes from accounting, where costs are spread over time.
# - Methods to analyze amortized complexity include:
#   - Aggregate method: Total cost of n operations divided by n.
#   - Banker's method: Assign "credits" to operations to pay for expensive ones.
#   - Potential method: Use a potential function to track costs.
# - For append(), the aggregate method shows that n appends cost O(n) total, so O(1) per operation.

# Other Python list methods with amortized complexity:
# - extend(iterable): O(k) where k is the length of the iterable, amortized due to potential resizes.
# - Most other list methods (e.g., insert, remove) have straightforward O(n) complexity without amortization.

# Practical takeaway:
# - Amortized O(1) for append() means it's very efficient for adding elements over time, even if rare resizes occur.
# - In practice, Python's over-allocation (reserving extra space) minimizes resizing frequency, making append() fast.




nest_Array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# accessing elements in a nested array
first = nest_Array[2][2]
#print(first)

for i in nest_Array:
    for j in i: 
        if j % 2 == 0:
             print(j)