class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0  
        self.tail = 0  
        self.size = 0  

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise IndexError("A fila está cheia.")
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")
        return self.queue[self.head]

    def display(self):
        if self.is_empty():
            print("A fila está vazia.")
        else:
            print("Fila:")
            index = self.head
            count = 0
            while count < self.size:
                print(self.queue[index])
                index = (index + 1) % self.capacity
                count += 1
