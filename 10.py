class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_beginning(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        removed_item = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        removed_item.next = None
        return removed_item.data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        removed_item = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        removed_item.prev = None
        return removed_item.data

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
