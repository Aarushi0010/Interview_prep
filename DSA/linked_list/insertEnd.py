class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class ListNode : 
    def __init__(self):
        self.head = None
    
    # accept new node 
    def new(self , value) :
        new = Node(value)

    # if no node exists then set head as new and return it 
        if self.head == None:
            self.head = new 
            return 
        
    # else we will iterate to end of list and add the value 

        current = self.head
        while current.next : 
            current = current.next

    # out of loop means add the new node to list 
        current.next = new

    def getValue(self) :
        if self.head is None : 
            return -1
        else :
            current = self.head
            while current :
                print(f"{current.value}")
                current = current.next 

list1 = ListNode()
list1.new(1)
list1.new(2)
list1.new(3)
list1.getValue()