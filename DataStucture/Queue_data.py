# Queue Data Structure


class Queue:
    # Constructor
    def __init__(self):
        self.items = []

    # function for ENQUEUE
    def enqueue(self, item):
        self.items.append(item)

    # function for DEQUEUE
    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        if self.items == []:
            return True
        return False


if __name__ == '__main__':
    # Creating a class object
    s = Queue()

    # here store data in Queue
    s.enqueue('Rajib')
    s.enqueue('Raiyan')
    s.enqueue('Sojib')

    # Now we dequeue data from Queue
    while not s.is_empty():
        person = s.dequeue()
        print(person)

