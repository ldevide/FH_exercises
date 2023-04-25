# Binary Search
def binary_search(numbers: list, target: int) -> bool:
    first = 0
    last = len(numbers) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if numbers[mid] == target:
            found = True
        else:
            if target < numbers[mid]:
                last = mid - 1
            else:
                first = mid + 1

        return found

# Hash Table:
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(selfself, old_hash, size):
        return (old_hash + 1) % size
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] is key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_funktion(key, len(self.slot))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

# Bubble Sort Implementation
def bubble_sort(numbers: list):
    for n in range(len(numbers)- 1, 0, -1):
        for k in range(n):
            if numbers[k] > numbers[k + 1]:
                temp = numbers[k]
                numbers[k] = numbers[k + 1]
                numbers[k + 1] = temp

# Selection Sort Implementation
def selection_sort(numbers: list):
    for fill_slot in range(0, len(numbers) - 1):
        position_of_min = fill_slot

        for location in range(fill_slot + 1, len(numbers)):
            if numbers[location] < numbers[position_of_min]:
                position_of_min = location

        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_min]
        numbers[position_of_min] = temp


