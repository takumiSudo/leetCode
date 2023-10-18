# DSA Array

Arrays are a fundamental data structure used in programming to store a collection of elements of the same data type. They are typically used to store a fixed number of elements, and each element is accessed by an index, with the first element having an index of 0. Here's a simple rundown of arrays in Python and C++.

### Arrays in Python:

In Python, arrays are implemented using lists. Lists are dynamic arrays, which means they can grow or shrink as needed.

```python
# Creating an array in Python
my_array = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_array[0]  # Access the first element (index 0)
second_element = my_array[1]  # Access the second element (index 1)

# Modifying elements
my_array[2] = 42  # Change the third element to 42

# Getting the length of the array
array_length = len(my_array)

# Iterating through the array
for element in my_array:
    print(element)
```

### Arrays in C++:

In C++, arrays are a fixed-size collection of elements. Once declared, the size of the array cannot be changed.

```cpp
#include <iostream>

int main() {
    // Creating an array in C++
    int myArray[5] = {1, 2, 3, 4, 5};  // Declare and initialize an array of integers

    // Accessing elements
    int firstElement = myArray[0];  // Access the first element (index 0)
    int secondElement = myArray[1];  // Access the second element (index 1)

    // Modifying elements
    myArray[2] = 42;  // Change the third element to 42

    // Getting the length of the array
    int arrayLength = sizeof(myArray) / sizeof(myArray[0]);

    // Iterating through the array
    for (int i = 0; i < arrayLength; i++) {
        std::cout << myArray[i] << " ";
    }

    return 0;
}
```

It's important to note that in C++, arrays have a fixed size, and the size must be known at compile time. If you need a dynamic-sized array, you would typically use data structures like `std::vector` from the Standard Template Library (STL) in C++ or dynamically allocate memory for an array.