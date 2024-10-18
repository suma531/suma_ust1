class CircularQueue:
    def __init__(self):
        self.max_size = 5
        self.queue = {}
        self.first = 0
        self.last = 0
        self.size = 0

    def adding(self, item):
        if self.size == self.max_size:

            self.queue.pop(self.first)
            self.first = (self.first + 1) % self.max_size
        else:
            self.size += 1


        self.queue[self.first] = item
        self.last = (self.last + 1) % self.max_size

    def remove(self):
        if self.size == 0:
            print("Queue is empty!")
            return None
        item = self.queue.pop(self.first)
        self.first = (self.first + 1) % self.max_size
        self.size -= 1
        return item

    def display(self):
        if self.size == 0:
            print("Queue is empty!")
            return
        elements = []
        for i in range(self.size):
            index = (self.first + i) % self.max_size
            elements.append(self.queue[index])
        print("Queue elements:", elements)
