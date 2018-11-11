from Linked_data import Node, LinkedList


def mergeList(firstList, secondList, mergedList):
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break
        if currentSecond is None:
            mergedList.insertEnd(currentFirst)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.insertEnd(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insertEnd(currentSecond)
            currentSecond = currentSecondNext

# First List
nodeOne = Node(1)
nodeTwo = Node(3)
nodeThree = Node(4)
firstList = LinkedList()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

# Second List
nodeFour = Node(2)
nodeFive = Node(7)
nodeSix = Node(9)
secondList = LinkedList()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("Printing first List")
firstList.printList()
print('Printing second List')
secondList.printList()

mergedList = LinkedList()

mergeList(firstList, secondList, mergedList)
del firstList
del secondList

print('Printing Merge List')
mergedList.printList()

