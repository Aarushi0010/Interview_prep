class Node :
    def __init__(self , value):
        self.value = value
        self.next = None

class ListNode : 
    def __init__(self):
        self.head = None
    
    # accept new node
    def insert(self, value , k):
        new = Node(value)
        current = self.head

        if current is None :
            self.head = new
            return
        
        for i in range(k) : 
            current = current.next
        new.next = current.next
        current.next = new

    def display(self):
        current = self.head 
        while current:
            print(current.value , end=" ")
            current = current.next

list1 = ListNode()
list1.insert(2 , 1)
list1.insert(4 , 0)
list1.display()