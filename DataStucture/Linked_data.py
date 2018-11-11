# Linked list Implementation
# Create Nodes
# Add nodes to linked list
# Print Linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print('Invalid Position!')
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertHead(self, newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertEnd(self, newNode):
        # Node => John => None
        if self.head is None:
            self.head = newNode
        else:
            # head => John => Ben => None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print('Linked list is empty.Delete Failed!')

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print('Invalid Position!')
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def deleteEnd(self):
        lastNode = self.head  # John
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next  # Ben
        previousNode.next = None

    def printList(self):
        # head => John => Ben => Mathew
        if self.head is None:
            print("List is empty!")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# node => data, next
# firstNode.data = John, firstNode.next = None
firstNode = Node('John')
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node('Ben')
linkedList.insertEnd(secondNode)
thirdNode = Node('Mathew')
linkedList.insertEnd(thirdNode)
linkedList.deleteAt(2)
linkedList.printList()




