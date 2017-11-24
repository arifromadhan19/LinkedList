class Node:
    def __init__(self, data=None, next=None):
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

    def InsertTailNode(self, data):

        if (self.head == None):
            head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head

    def InsertHeadNode(self,data):
        current = Node(data)
        current.next = self.head
        self.head = current

    def InsertSpecificPosition(self,data,position):
        if not position == 0:
            current = self.head
            current_position = 1
            while (position - current_position > 0):
                current = current.next
                current_position += 1
            if current.next is None:
                current.next = Node(data, None)
                return self.head
            else:
                prev = current.next
                current.next = Node(data, prev)
                return self.head
        else:
            return Node(data, self.head)

    def Delete(self, position):
        temp = self.head
        if position == 0:
            return temp.next

        while position - 1 > 0:
            head = self.head.next
            position -= 1
        self.head.next = self.head.next.next
        return temp


if __name__ == '__main__':
    llist = LinkedList()

    # llist.head = Node(1)
    #Insert Manual
    # second = Node(2)
    # third = Node(3)
    # llist.head.next = second
    # second.next = third

    #Insert by function
    llist.InsertHeadNode(1)
    llist.InsertSpecificPosition(2,1)
    llist.InsertSpecificPosition(3, 2)
    llist.InsertTailNode(4)

    # llist.Delete(2)

    llist.printList()
