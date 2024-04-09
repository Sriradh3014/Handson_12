class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = [None] * self._capacity

    def add(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._array[index]

    def __len__(self):
        return self._size

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

# Example usage:
dyn_array = DynamicArray()
for i in range(10):
    dyn_array.add(i)

print("Array size:", len(dyn_array))
print("Array elements:")
for i in range(len(dyn_array)):
    print(dyn_array[i])
