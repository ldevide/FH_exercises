# exercise 5.1
def selection_sort(numbers: list):
    for fill_slot in range(len(numbers) - 1, -1, -1):
        position_of_max = fill_slot
        for location in range(0, fill_slot):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp
    return numbers



# exercise 5.2
# text: sorted list of words
# target: word to search
# return: target if found, otherwise None
def binary_search(text: list, target: str):
    first = 0
    last = len(text)
    if last == 0:
        return None
    while first != last:
        position = (first + last) // 2

        if text[position] == target:
            return target
        if text[position] > target:
            last = position - 1
        else:
            first = position + 1
    if first < len(text) and text[first] == target:
        return target

    return None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[]] * self.size


    def __my_hash(self, key):
       if type(key) == str:
           return len(key) % self.size
       elif type(key) == int:
           return key % self.size
       else: # unknown type -> use slot 0
           return 0

    def getIndex(self, lst, key):
        index = 0
        while index < len(lst):
            if lst[index][0] == key:
                return index
            index = index + 1
        return None
    def put(self, key, data):
        bucket_index = self.__my_hash(key)
        bucket = self.slots[bucket_index]
        key_index = self.getIndex(bucket, key)
        if key_index == None:
            bucket.append([key, data])
        else:
            bucket[key_index][1] = data

    def get(self, key):
        bucket_index = self.__my_hash(key)
        bucket = self.slots[bucket_index]
        for element in bucket:
            if element[0] == key:
                return element[1]
        result = None


if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        print("exercise 1:")
        lst = [31, 46, 23, 8, 12, 7, 44, 63, 82]
        print(lst)
        selection_sort(lst)
        print(lst)
    elif exercise == '2':
        print("exercise 2:")
        text = []
        print(binary_search(text, "rose"))
        text = ["rose"]
        print(binary_search(text, "rose"))
        print(binary_search(text, "tulip"))
        text = ["rose", "tulip"]
        print(binary_search(text, "rose"))
        print(binary_search(text, "tulip"))
        print(binary_search(text, "daisy"))
        text = ["daisy", "rose", "tulip"]
        print(binary_search(text, "rose"))
        print(binary_search(text, "tulip"))
        print(binary_search(text, "daisy"))
        print(binary_search(text, "daffodil"))
        text = ["daffodil", "daisy", "rose", "tulip"]
        print(binary_search(text, "rose"))
        print(binary_search(text, "tulip"))
        print(binary_search(text, "daisy"))
        print(binary_search(text, "daffodil"))
        print(binary_search(text, "poppy"))
    elif exercise == '3':
        print("exercise 3:")
        hashTable = HashTable(4)
        print(hashTable.get("Elefant"), "expected: None")
        print(hashTable.get(1997), "expected: None")
        hashTable.put(23, 66)
        print(hashTable.get("Elefant"), "expected: None")
        print(hashTable.get(1997), "expected: None")
        print(hashTable.get(23), "expected: 66")
        hashTable.put("Elefant", 4)
        print(hashTable.get("Elefant"), "expected: 4")
        print(hashTable.get(1997), "expected: None")
        print(hashTable.get(23), "expected: 66")
    else:
        print(f"unknown exercise {exercise}")


