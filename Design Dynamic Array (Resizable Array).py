class DynamicArray:
    # O(n) - n = capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    # O(1)
    def get(self, i: int) -> int:
        return self.arr[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # O(1) - Avg case / Amortized
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    # O(1)
    def popback(self) -> int:
        # Soft deletion
        self.size -= 1
        return self.arr[self.size]
 
    # O(n)
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity


        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.size
        
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity

# Test Case 1: Initialization
da = DynamicArray(2)
assert da.getCapacity() == 2, f"Expected capacity to be 2, got {da.getCapacity()}"
assert da.getSize() == 0, f"Expected size to be 0, got {da.getSize()}"

# Test Case 2: Adding an element with pushback
da.pushback(10)
assert da.get(0) == 10, f"Expected element at index 0 to be 10, got {da.get(0)}"
assert da.getSize() == 1, f"Expected size to be 1, got {da.getSize()}"

# Test Case 3: Resizing when capacity is reached
da.pushback(20)
da.pushback(30)  # This should trigger a resize
assert da.getCapacity() == 4, f"Expected capacity to be 4 after resize, got {da.getCapacity()}"
assert da.get(2) == 30, f"Expected element at index 2 to be 30, got {da.get(2)}"
assert da.getSize() == 3, f"Expected size to be 3, got {da.getSize()}"

# Test Case 4: Setting a value at a specific index
da.set(1, 25)
assert da.get(1) == 25, f"Expected element at index 1 to be 25, got {da.get(1)}"

# Test Case 5: Popping the last element
last_element = da.popback()
assert last_element == 30, f"Expected popped element to be 30, got {last_element}"
assert da.getSize() == 2, f"Expected size to be 2 after pop, got {da.getSize()}"

# Test Case 6: Getting the size and capacity
assert da.getSize() == 2, f"Expected size to be 2, got {da.getSize()}"
assert da.getCapacity() == 4, f"Expected capacity to be 4, got {da.getCapacity()}"

print("All test cases passed!")
