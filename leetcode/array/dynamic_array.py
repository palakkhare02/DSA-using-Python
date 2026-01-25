class DynamicArray:
    def __init__(self):
        # Initial capacity of the array
        self.capacity = 1
        # Number of elements currently in array
        self.size = 0
        # Internal static array
        self.arr = [None] * self.capacity

    def __len__(self):
        # Return number of elements
        return self.size

    def __getitem__(self, index):
        # Get element at given index
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def append(self, value):
        # Add element at the end
        if self.size == self.capacity:
            self._resize(2 * self.capacity)   # Double the capacity

        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        # Remove last element
        if self.size == 0:
            raise IndexError("Pop from empty array")

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1

        # Optional: shrink the array if too empty
        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

        return value

    def insert(self, index, value):
        # Insert element at a specific index
        if not 0 <= index <= self.size:
            raise IndexError("Index out of bounds")

        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]

        self.arr[index] = value
        self.size += 1

    def remove(self, index):
        # Remove element at a specific index
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")

        removed_value = self.arr[index]

        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.size - 1] = None
        self.size -= 1

        # Optional shrinking
        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

        return removed_value

    def _resize(self, new_capacity):
        # Create a new array with new capacity
        new_arr = [None] * new_capacity

        # Copy elements to new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def display(self):
        # Display current elements
        return [self.arr[i] for i in range(self.size)]
