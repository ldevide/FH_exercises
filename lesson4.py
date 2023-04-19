class SSLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def append(self, data):
        node = SSLNode(data)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def __str__(self):
        return str([node for node in self])

my_ssl = SinglyLinkedList()
print(my_ssl)
print(my_ssl.size)
my_ssl.append(24)
print(my_ssl.size)
print(my_ssl)
my_ssl.append(32)
print(my_ssl.size)
print(my_ssl)




