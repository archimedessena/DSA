// Understanding Arrays in JavaScript and How to Loop Through Them

// What is a JavaScript Array?
// - An array is a special type of object that stores a list of items (like numbers, strings, or objects).
// - Arrays are ordered, meaning each item has an index (starting at 0).
// - Similar to Python lists, but with JavaScript-specific methods and behaviors.

// Creating an Array
let myArray = [1, "hello", true, { name: "Alice" }]; // Array with mixed types
// Access items using index (O(1) time complexity, like Python lists)
let firstItem = myArray[0]; // 1

// Common JavaScript Array Methods (with Big-O Time Complexities)
// 1. push(...items) - Adds items to the end of the array
//    Time Complexity: O(1) amortized (like Python's append)
myArray.push(42); // O(1) - Adds 42 to the end

// 2. pop() - Removes and returns the last item
//    Time Complexity: O(1)
let lastItem = myArray.pop(); // O(1) - Removes 42, returns it

// 3. unshift(...items) - Adds items to the start of the array
//    Time Complexity: O(n) - Shifts all elements right
myArray.unshift(0); // O(n) - Adds 0 to the start

// 4. shift() - Removes and returns the first item
//    Time Complexity: O(n) - Shifts all elements left
let first = myArray.shift(); // O(n) - Removes 0, returns it

// 5. splice(start, deleteCount, ...items) - Adds/removes items at an index
//    Time Complexity: O(n) - Shifts elements after the splice point
myArray.splice(1, 1, "new"); // O(n) - Removes 1 item at index 1, adds "new"

// 6. slice(start, end) - Returns a shallow copy of a portion of the array
//    Time Complexity: O(k) where k is the slice length
let subArray = myArray.slice(1, 3); // O(k) - Copies elements from index 1 to 2

// 7. indexOf(item, [start]) - Returns the first index of an item
//    Time Complexity: O(n) - Scans the array
let index = myArray.indexOf("hello"); // O(n)

// 8. includes(item, [start]) - Checks if an item exists
//    Time Complexity: O(n) - Scans the array
let hasItem = myArray.includes("hello"); // O(n)

// 9. forEach(callback) - Executes a function for each element
//    Time Complexity: O(n) - Iterates through all elements
myArray.forEach(item => console.log(item)); // O(n)

// 10. map(callback) - Creates a new array with results of calling a function on each element
//     Time Complexity: O(n)
let doubled = myArray.map(x => typeof x === "number" ? x * 2 : x); // O(n)

// 11. filter(callback) - Creates a new array with elements that pass a test
//     Time Complexity: O(n)
let numbers = myArray.filter(x => typeof x === "number"); // O(n)

// 12. reduce(callback, initialValue) - Reduces array to a single value
//     Time Complexity: O(n)
let sum = myArray.reduce((acc, x) => typeof x === "number" ? acc + x : acc, 0); // O(n)

// 13. sort(compareFunction) - Sorts the array in place
//     Time Complexity: O(n log n) - Uses a mix of algorithms (usually Timsort-like)
myArray.sort((a, b) => a - b); // O(n log n) - For numbers; assumes numbers in array

// Looping Through an Array
// There are several ways to loop through a JavaScript array. Here are the most common:

// 1. for Loop (Traditional)
//    - Time Complexity: O(n)
//    - Good for control over indices and breaking early.
for (let i = 0; i < myArray.length; i++) {
    console.log(myArray[i]); // O(n) - Access each element (O(1) per access)
}

// 2. for...of Loop
//    - Time Complexity: O(n)
//    - Cleaner syntax for iterating over values, no index needed.
for (let item of myArray) {
    console.log(item); // O(n)
}

// 3. forEach Method
//    - Time Complexity: O(n)
//    - Functional approach, runs a callback for each element.
myArray.forEach((item, index) => {
    console.log(`Index ${index}: ${item}`); // O(n)
});

// 4. map Method (if transforming while looping)
//    - Time Complexity: O(n)
//    - Creates a new array, useful for transforming data.
let transformed = myArray.map(item => item.toString()); // O(n)

// 5. for...in Loop (Avoid for Arrays)
//    - Time Complexity: O(n)
//    - Meant for objects, iterates over enumerable properties (indices), but can include inherited properties.
//    - Not recommended for arrays due to potential issues.
for (let i in myArray) {
    console.log(myArray[i]); // O(n) - Use with caution
}

// Example: Looping Through an Array
let fruits = ["apple", "banana", "orange"];

// Using for loop
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]); // O(n) - Prints: apple, banana, orange
}

// Using for...of
for (let fruit of fruits) {
    console.log(fruit); // O(n) - Prints: apple, banana, orange
}

// Using forEach
fruits.forEach(fruit => console.log(fruit)); // O(n) - Prints: apple, banana, orange

// Notes on Time Complexities
// - Most array methods in JS have similar complexities to Python lists:
//   - O(1): push, pop (like append, pop in Python).
//   - O(n): unshift, shift, splice (like insert, remove, pop(i) in Python).
//   - O(n log n): sort (like Python’s sort).
//   - O(n): indexOf, includes, forEach, map, filter, reduce (like index, count in Python).
// - Looping (for, for...of, forEach) is always O(n) because you visit each element.

