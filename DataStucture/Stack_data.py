# Stack Data structure formation


class Stack:
    # Constructor function
    def __init__(self):
        self.items = []

    # Push function for add new data
    def push(self, item):
        self.items.append(item)

    # Pop function for remove the data
    def pop(self):
        return self.items.pop()

    # function for check the list that empty or not
    def is_empty(self):
        if self.items == []:
            return True
        return False


if __name__ == '__main__':
    # Creating a class object
    s = Stack()

    # Here we store data in Stack
    s.push(1)
    s.push(2)
    s.push(3)

    # Now we pop the data from Stack
    while not s.is_empty():
        item = s.pop()
        print(item)
