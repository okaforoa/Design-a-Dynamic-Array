
# Dynamic Array (Resizable Array) Implementation in Python

## Overview

This project provides a custom implementation of a Dynamic Array in Python, similar to Python's built-in list but with explicit control over its behavior and sizing. The Dynamic Array allows for efficient array operations such as adding, accessing, and removing elements, with the added capability of automatically resizing itself to accommodate more elements as needed.

## Features

- **Initialization with Capacity**: Initialize the dynamic array with a specified capacity.
- **Get Element**: Access an element at a given index.
- **Set Element**: Modify the value of an element at a given index.
- **Push Back**: Add an element to the end of the array, automatically resizing the array if needed.
- **Pop Back**: Remove and return the last element of the array, reducing the size but not the capacity.
- **Resize**: Double the array's capacity when it reaches its current limit to accommodate additional elements.
- **Get Size**: Retrieve the current number of elements in the array.
- **Get Capacity**: Retrieve the current capacity of the array.

## Usage

To use this dynamic array, simply instantiate the `DynamicArray` class with the desired initial capacity. You can then use the provided methods to manipulate the array as needed.

Example:
```python
from dynamic_array import DynamicArray

# Create a new dynamic array with an initial capacity of 2
da = DynamicArray(2)

# Add elements to the array
da.pushback(1)
da.pushback(2)

# Automatically resize when adding another element
da.pushback(3)

# Access elements
print(da.get(0))  # Output: 1

# Remove the last element
last_element = da.popback()
print(last_element)  # Output: 3
```

## Testing

This implementation includes test cases demonstrating initialization, adding elements, automatic resizing, accessing and setting values, and popping elements.

## Contribution

Contributions to improve this dynamic array implementation are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

