"""Insertion sort works by building the final sorted array one item at a time.
It iterates through the input array from the second element (index 1).
For each iteration, it takes the current element (key) and compares it with the elements before it.
It shifts elements that are greater than the key to the right.
Then it places the key in its correct position.

The time complexity of insertion sort is:

Best case: O(n) - when the array is already sorted
Average case: O(n²)
Worst case: O(n²)

This makes it inefficient for large lists, but it's simple to implement and works well for small lists or nearly sorted arrays."""

def insertion_sort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        key = arr[i]
        print(key)
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        print(j)
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(j + 1)
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test the insertion sort algorithm
    example_list = [464, 134, 245, 172, 22, 11, 990]
    print("Original list:", example_list)
    
    sorted_list = insertion_sort(example_list)
    print("Sorted list:", sorted_list)