#  For Linked List


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        # first we create blank node and linked with head
        # and data = None, next = None
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

            # All nodes shows in string format
            # After every two nodes are divided by Comma
            return ",".join(nodes)

    def append(self, data):
        # now we create node object
        node = Node(data)

        if self.head.next is None:
            # if linked list is blank then the value of head.next is None
            # now we keep the node in head.next and then return it
            self.head.next = node

            return

        # now we reach the last value of node by continue our loop
        # After finish looping, current_node store the last node of linked list
        current_node = self.head.next

        while current_node.next:
            current_node = current_node.next

        # node will be next of last node then now node is the last node of list
        current_node.next = node

    def prepend(self, data):
        # We create a first node of linked list
        # and copy the head.next in next part
        node = Node(data, self.head.next)

        # We keep the node in head.next
        # because this is first node of linked list
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                # now we create new node and its data is new_data
                # current_node.next is the after node of current node
                new_node = Node(new_data, current_node.next)

                # now keep the new_node in current_node.next
                current_node.next = new_node

                # though we store the new_node in right place
                # then get out of the loop
                break

            current_node = current_node.next

    def search(self, item):
        current_node = self.head.next

        # if current_node is None then it get out of the loop
        # otherwise loop in continue for other value except None
        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next

        return None

    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if self.head == previous_node:
            self.head.next = current_node.next

        else:
            previous_node.next = current_node.next

