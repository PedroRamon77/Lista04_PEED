class   Item:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Item(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Item(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove_from_beginning(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        removed_item = self.head
        self.head = self.head.next
        removed_item.next = None
        return removed_item.data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("A lista está vazia.")

        current = self.head
        previous = None

        while current.next is not None:
            previous = current
            current = current.next

        if previous is None:
            self.head = None
        else:
            previous.next = None

        return current.data

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
            return

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
