class Item:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Item(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Item(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove_from_beginning(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        removed_item = self.head
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        removed_item.next = None
        return removed_item.data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        removed_item = None
        if self.head.next == self.head:
            removed_item = self.head
            self.head = None
        else:
            current = self.head
            previous = None
            while current.next != self.head:
                previous = current
                current = current.next
            previous.next = self.head
            removed_item = current
        removed_item.next = None
        return removed_item.data

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return

        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break
