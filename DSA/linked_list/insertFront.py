class ListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class LinkedList : 
    def __init__(self) : 
       self.head = None  #to initialize the first node 

    def insertFront (self, value): 
        print("Insertig " , value)

        # create a new node 
        new_node = ListNode(value)
        new_node.next = self.head

        # setting head node as new node 
        self.head = new_node

    def get_head(self): 
        if self.head == None:
            return -1
        else : 
            return self.head.value
        
list1 = LinkedList()
list1.insertFront(2)
list1.insertFront(3)
list1.get_head()