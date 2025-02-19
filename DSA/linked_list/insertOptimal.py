class Node : 
    def __init__(self , value):
        self.value = value
        self.next = None
class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertEnd(self , value) : 
        new = Node(value)

        if self.head is None : 
            self.head = new
            self.tail = new
            return 
        
        self.tail.next = new 
        self.tail = new 
