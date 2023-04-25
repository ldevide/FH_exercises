"""
Exercise template for exercise 04 linked lists
"""


# singly linked list
# node class of the singly linked list
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node

    def __str__(self):
        return str(self.data)


# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the SLLNode class
        node = SLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
        else:  # if it is not empty, we need to find the last node and append the new node
            current = self.head
            while current.next is not None:
                current = current.next
            # set the pointer of the last node to the new node
            current.next = node
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    """
    Exercise part 1,2,3,4

    Implement the given methods below according to the requirements in the exercise sheet.
    Make sure to return the correct values.
    """

    def insert(self, prev_node_data, new_node_data):
        current = self.head
        if current == None:
            return False
        if prev_node_data == current.data:
            node = SLLNode(new_node_data)
            node.next = current.next
            current.next = node
            self.size += 1
            return True
        while current.next is not None:
            current = current.next
            if prev_node_data == current.data:
                node = SLLNode(new_node_data)
                node.next = current.next
                current.next = node
                self.size += 1
                return True
        return False


    def clear(self):
        self.head = None
        self.size = 0
        return

    def get_data(self, data):
        current = self.head
        if current == None:
            return False
        if data == current.data:
            return data
        while current.next is not None:
            current = current.next
            if data == current.data:
                return data
        return False

    def delete(self, data):
        current = self.head
        if current == None:
            return
        if data == current.data:
            self.head = current.next
            self.size -= 1
            return
        while current.next is not None:
            previous = current
            current = current.next
            if data == current.data:
                previous.next = current.next
                self.size -= 1
                return



"""
Exercise part 5
Implement a doubly linked list according to the exercise sheet.
You can copy the code from the singly linked list and modify it.
"""


class DLLNode:
    """Implement the node of the doubly linked list here"""
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next node
        self.previous = None  # pointer to the previous node
class DoublyLinkedList:
    """Implement the doubly linked list and its methods here"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        # Create the new node the pointer is set to None through the constructor of the DLLNode class
        node = DLLNode(data)
        if self.head is None:  # if the list is empty, the new node is the head
            self.head = node
            self.tail = node
        else:  # if it is not empty, we need to find the last node and append the new node
            # current = self.head
            # while current.next is not None:
                # current = current.next
            # set the pointer of the last node to the new node
            self.tail.next = node
            node.previous = self.tail
        self.size += 1  # increase the size of the list

    def get_size(self):
        return self.size

    # string representation of the linked list
    def __str__(self):
        return str([node for node in self])

    # iteration function without this function we can not iterate over the list
    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def insert(self, prev_node_data, new_node_data):
        current = self.head
        if current == None:
            return False
        if prev_node_data == current.data:
            node = DLLNode(new_node_data)
            node.next = current.next
            current.next = node
            node.previous = current
            self.size += 1
            return True
        while current.next is not None:
            current = current.next
            if prev_node_data == current.data:
                node = DLLNode(new_node_data)
                node.next = current.next
                current.next = node
                node.previous = current
                self.size += 1
                return True
        return False


    def clear(self):
        self.head = None
        self.size = 0
        return

    def get_data(self, data):
        current = self.head
        if current == None:
            return False
        if data == current.data:
            return data
        while current.next is not None:
            current = current.next
            if data == current.data:
                return data
        return False

    def delete(self, data):
        current = self.head
        if current == None:
            return
        if data == current.data:
            self.head = current.next
            if current.next:
                current.next.previous = None
            self.size -= 1
            return
        if data == self.tail.data:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return
        while current.next is not None:
            current = current.next
            if data == current.data:
                current.previous.next = current.next
                current.next.previous = current.previous
                self.size -= 1
                return

"""
Exercise Part 5 and 7:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet
"""


class MyStack:

    def push(self, element):
        return

    def pop(self):
        return

    def top(self):
        return

    def size(self):
        return


class MyQueue:

    def push(self, element):
        return

    def pop(self):
        return

    def show_left(self):
        return

    def show_right(self):
        return

    def size(self):
        return
def test(ll):
        print(f'clear() empty list: {ll.clear()} - expected: None')
        print(f'get_data() of empty list: {ll.get_data(5)} - expected: False')
        print(f'insert() into empty list: {ll.insert(5, "Hase")} - expected: False')
        print(f'delete() from empty list: {ll.delete(5)} - expected: None')
        # test with one element in list
        ll.append(1997)
        print(f'get_data() of non existing data: {ll.get_data(5)}, {ll.get_size()} - expected: False, 1')
        print(f'insert() after non existing data: {ll.insert(5, "Hase")}, {ll.get_size()} - expected: False, 1')
        print(f'delete() non existing data: {ll.delete(5)}, {ll.get_size()} - expected: None, 1')
        # test with existing data
        print(f'get_data() of existing data: {ll.get_data(1997)}, {ll.get_size()} - expected: 1997, 1')
        print(f'insert() after existing data: {ll.insert(1997, "Hase")}, {ll.get_size()} - expected: True, 2')
        print(f'delete() existing data: {ll.delete(1997)}, {ll.get_size()} - expected: None, 1')
        print(f'delete() existing data: {ll.delete("Hase")}, {ll.get_size()} - expected: None, 0')
        ll.append("Toast")
        ll.append("Ham")
        print(f'insert() after existing data: {ll.insert("Toast", "Cheese")}, {ll.get_size()} - expected: True, 3')
        print(ll)
        print(f'clear() empty list: {ll.clear()}, {ll.get_size()} - expected: None, 0')
        print(ll)

if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        print("exercise 1:")
        test(SinglyLinkedList())
    if exercise == '5':
        print("exercise 5:")
        test(DoublyLinkedList())