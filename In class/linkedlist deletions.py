class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Single_LinkedList:
    def __init__(self):
        self.head = None
    def printSLL(self):
        temp = self.head
        if temp is None:
            print("List is empty!")
        else:
            while temp is not None:
                print(temp.data)
                temp = temp.next
    def new_node(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
    def beg_del(self):
        if self.head is None:
            print("List is empty!")
        else:
            self.head = self.head.next
    def end_del(self):
        if self.head is None:
            print("List is empty!")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def mid_del_value(self,x):
        temp = self.head
        while temp is not None:
            temp = temp.next
            if temp.next.data == x:
                break
            else:
                continue
        temp.next = temp.next.next
    
    def mid_del_pos(self,x):
        temp = self.head
        pos = 1
        while temp.next is not None:
            if pos == (x-1):
                break
            else:
                temp = temp.next
                pos = pos + 1
        temp.next = temp.next.next
    
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
        
        
        
L = Single_LinkedList()
L.new_node(10)
L.new_node(20)
L.new_node(30)
L.new_node(40)
L.new_node(50)
L.new_node(60)
L.new_node(70)
L.new_node(80)
L.new_node(90)
L.new_node(100)
L.beg_del()
L.end_del()
L.mid_del_value(40)
L.mid_del_pos(3)
L.updates(3,40)
L.printSLL()
