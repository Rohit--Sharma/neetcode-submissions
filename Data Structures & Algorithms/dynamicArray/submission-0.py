class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = []

    def get(self, i: int) -> int:
        if i < self.capacity:
            return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        self.array.append(n)
        self.size += 1
        if self.size > self.capacity:
            self.resize()

    def popback(self) -> int:
        self.size -= 1
        return self.array.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
