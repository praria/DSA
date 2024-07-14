import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Example Usage
bf = BloomFilter(20000, 10)

# Adding items to the filter
bf.add("apple")
bf.add("banana")
bf.add("cherry")

# Checking for items
print(bf.check("apple"))  # Output: True
print(bf.check("grape"))  # Output: False (definitely not in the set)