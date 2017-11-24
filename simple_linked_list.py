class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next

    def Insert(self, data):

        if (self.head == None):
            head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    #
    # llist.head.next = second
    # second.next = third

    #Insert by function
    llist.Insert(2)
    llist.Insert(3)

    llist.printList()
