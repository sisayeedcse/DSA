class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # Linkedlist Traversing (Print)
    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    # New Node Creation
    def newNode(self,data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_Node
    # Insertion at beginning
    def add_beg(self,data):
        begNode = Node(data)
        begNode.next = self.head
        self.head = begNode
    #Insertion at end
    def add_end(self,data):
        endNode = Node(data)
        if self.head is None:
            self.head = endNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = endNode
    # Insertion after specific item
    def add_after(self,data,x):
        addAfter = Node(data)
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            else:
                temp = temp.next
        if temp is None:
            print("The given item is not found")
        else:
            addAfter.next = temp.next
            temp.next = addAfter
    # Insertion before specific item
    def add_before(self,data,x):
        addBefore = Node(data)
        temp = self.head
        while temp is not None:
            if temp.next.data == x:
                break
            else:
                temp = temp.next
        if temp is None:
            print("The given item is not found")
        else:
            addBefore.next = temp.next
            temp.next = addBefore
    # Deletion from beginning
    def del_beg(self):
        if self.head is None:
            print("List is empty!")
        else:
            self.head = self.head.next
    # Deletion from end
    def del_end(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    # Deleting an specific value
    def del_value(self,data):
        temp = self.head
        while temp is not None:
            if temp.next.data == data:
                break
            else:
                temp = temp.next
        if temp is None:
            print("List is empty!")
        else:
            temp.next = temp.next.next
    # Deleting by position
    def del_pos(self,x):
        temp = self.head
        pos = 1
        while temp.next is not None:
            if pos == (x-1):
                break
            else:
                temp = temp.next
                pos = pos + 1
        temp.next = temp.next.next
    # Updating values
    def updates(self,x,data):
        temp = self.head
        pos = 1
        while temp.next is not None:
            if pos == (x-1):
                break
            else:
                temp = temp.next
                pos = pos + 1
        temp.next.data = data
    # Unsorted Search
    def Unsort_search(self,ITEM):
        ptr = self.head
        pos = 1
        while ptr is not None:
            if ptr.data == ITEM:
                print("The item is found at LOC- ", pos)
                break
            else:
                ptr = ptr.next
                pos = pos + 1
        if ptr is None:
            print("The ITEM is not found")
LL = LinkedList()
LL.newNode(10)
LL.newNode(20)
LL.newNode(30)
LL.add_beg(5)
LL.add_end(40)
LL.add_after(25,20)
LL.add_before(15,20)
LL.del_beg()
LL.del_end()
LL.del_value(20)
LL.del_pos(3)
LL.updates(3,40)
LL.Unsort_search(15)
LL.printLL()
