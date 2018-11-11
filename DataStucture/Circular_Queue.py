# This is Circular Queue Data Structure


class Queue:
    # Constructor function
    def __init__(self):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    # ENQUEUE function for add new data
    def enqueue(self, item):
        if self.is_full():
            print('Queue is full!')

            return

        print('Inserting', item)
        self.items[self.tail] = item
        self.tail = ( self.tail + 1 ) % self.max_size
        self.size += 1

    # DEQUEUE function for take data from Queue
    def dequeue(self):
        item = self.items[self.head]
