# Explaining Big-O Notation in Simple Terms for a Layman
# (Including All Common Time Complexities and Python List Methods)

# What is Big-O Notation?
# - Big-O notation is like a speedometer for code. It tells us how "slow" or "fast" a program runs as the amount of data (like a list size) gets bigger.
# - It focuses on the worst-case scenario and how the time grows with more data.
# - Imagine you're organizing a pile of books: Big-O tells you how much longer it takes if the pile gets huge.

# Why Does It Matter?
# - It helps us predict if a program will stay fast or grind to a halt with lots of data.
# - Example: Will checking a list take seconds or hours if the list has millions of items?

# Analogy:
# - Think of sorting books:
#   - Grabbing the top book is instant (fast).
#   - Checking every book one by one takes longer.
#   - Comparing every book to every other book takes forever!
# - Big-O describes how the effort grows as the pile gets bigger.

# All Common Big-O Time Complexities (From Fastest to Slowest):
# 1. O(1) - Constant Time
#    - The time stays the same, no matter how big the data is.
#    - Like grabbing the first book from a pile, always quick.
my_list = [1, 2, 3, 4]
first = my_list[0]  # O(1) - Takes the same time for 4 or 4 million items.

# 2. O(log n) - Logarithmic Time
#    - The time grows very slowly; doubling the data adds only a tiny bit more time.
#    - Like finding a book in a sorted pile by splitting it in half each time (binary search).
#    - Not a built-in list method, but used in libraries like bisect.
from bisect import bisect_left
sorted_list = [1, 2, 3, 4, 5]
index = bisect_left(sorted_list, 3)  # O(log n) - Super fast, even for huge sorted lists.

# 3. O(n) - Linear Time
#    - The time grows directly with the data size (n = number of items).
#    - Like checking each book one by one to find a specific one.
found = 3 in my_list  # O(n) - If the list doubles in size, time doubles.

# 4. O(n log n) - Log-Linear Time
#    - The time grows a bit faster than linear but still manageable.
#    - Common in efficient sorting, like Python’s list.sort().
my_list.sort()  # O(n log n) - Sorting 1000 items takes more than 1000 steps but way less than 1000^2.

# 5. O(n^2) - Quadratic Time
#    - The time grows with the square of the data size; gets slow for big data.
#    - Like comparing every book to every other book.
for i in my_list:
    for j in my_list:  # O(n^2) - For 10 items, 10x10=100 steps; for 100 items, 10,000 steps.
        pass

# 6. O(n^3) - Cubic Time
#    - The time grows with the cube of the data size; much slower than quadratic.
#    - Like checking every possible group of three books.
for i in my_list:
    for j in my_list:
        for k in my_list:  # O(n^3) - For 10 items, 10x10x10=1000 steps; for 100 items, 1 million steps.
            pass

# 7. O(n^k) - Polynomial Time (Generalized)
#    - Any time where the growth is n raised to a constant power k (e.g., O(n^2), O(n^3), O(n^4)).
#    - Higher k means slower performance; rare in list methods but seen in complex algorithms.
#    - Example: Four nested loops would be O(n^4).

# 8. O(2^n) - Exponential Time
#    - The time doubles with each additional item; insanely slow for large data.
#    - Like trying every possible combination of books (e.g., all subsets).
#    - Not in list methods, but common in problems like generating all subsets.
def subsets(lst):
    result = [[]]
    for x in lst:
        result += [subset + [x] for subset in result]  # O(2^n) - Doubles work per item added.

# 9. O(n!) - Factorial Time
#    - The time grows with the factorial of the data size (e.g., 5! = 120, 10! = 3,628,800); slowest of all.
#    - Like trying every possible order of books.
#    - Not in list methods, but seen in problems like permutations.
from itertools import permutations
for perm in permutations(my_list):  # O(n!) - For 10 items, 3.6 million steps.

# Big-O for Python List Methods (From Your Previous Question):
# - Here’s how the list methods you asked about fit into these complexities:
# 1. append(x): O(1) amortized
#    - Fast, like adding a book to the top of a pile.
#    - "Amortized" means it’s O(1) on average, even though rare resizing is O(n).
my_list.append(5)  # O(1) amortized

# 2. extend(iterable): O(k) where k is the length of the iterable
#    - Like adding multiple books; time depends on how many you add.
my_list.extend([6, 7])  # O(k), k=2 here

# 3. insert(i, x): O(n)
#    - Slow, like sliding a book into the middle of a pile and shifting others.
my_list.insert(1, 'a')  # O(n)

# 4. remove(x): O(n)
#    - Slow, like searching for a book and shifting others to close the gap.
my_list.remove('a')  # O(n)

# 5. pop([i]): O(1) for last item, O(n) for other indices
#    - Popping the last item is instant; popping from the middle shifts items.
item = my_list.pop()  # O(1)
item = my_list.pop(1)  # O(n)

# 6. clear(): O(1)
#    - Instant, like throwing out the whole pile (Python just resets the list).
my_list.clear()  # O(1)

# 7. index(x[, start[, end]]): O(n)
#    - Slow, like checking each book to find one.
index = my_list.index(2)  # O(n)

# 8. count(x): O(n)
#    - Slow, like counting how many times a book appears in the pile.
count = my_list.count(2)  # O(n)

# 9. sort(key=None, reverse=False): O(n log n)
#    - Efficient, like organizing books in a smart way (uses Timsort).
my_list.sort()  # O(n log n)

# 10. reverse(): O(n)
#     - Slowish, like flipping the order of all books.
my_list.reverse()  # O(n)

# 11. copy(): O(n)
#     - Slowish, like copying every book to make a new pile.
new_list = my_list.copy()  # O(n)

# Layman’s Takeaway:
# - O(1) and O(log n): Super fast, like grabbing a book or splitting a pile.
# - O(n): Okay, like checking each book one by one.
# - O(n log n): Pretty good for complex tasks like sorting.
# - O(n^2), O(n^3), etc.: Slow, like comparing tons of books.
# - O(2^n) and O(n!): Crazy slow, like trying every possible combination or order.
# - Python list methods are mostly O(1), O(n), or O(n log n), making them efficient for most tasks.

# Notes on Amortized (Since You Asked Before):
# - Amortized means averaging the cost over many operations.
# - For append(), most adds are O(1), but sometimes Python resizes the list (O(n)).
# - It’s like paying a small fee most days but a big one rarely; the average is still low (O(1)).

# Non-Method List Operations:
# - Indexing: my_list[0]  # O(1)
# - Slicing: my_list[1:3]  # O(k) where k is slice length
# - Concatenation: my_list + [4, 5]  # O(n + k)
# - Length: len(my_list)  # O(1)
# - Membership: 3 in my_list  # O(n)
