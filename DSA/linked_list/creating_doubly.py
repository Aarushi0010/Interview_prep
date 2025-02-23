# initializing the node 
class Node : 
    def __init__(self, data): 
        self.data = data 
        self.prev = None 
        self.next = None 

class LinkedList : 
    def __init__(self):
        self.head = None 

    def insertEnd(self, data):
        new_node = Node(data)

        # if list is empty 
        if self.head is None : 
            self.head = new_node 
            return 
        
        # to traverse and enter at last 

        temp = self.head 
        while(temp.next): 
            temp = temp.next 

        temp.next = new_node
        new_node.prev = temp 

    def display(self):
        temp = self.head
        while temp : 
            print(temp.data, end =" ")
            temp = temp.next
        print("Finish")

# backwards display 
    def backDisplay(self) : 
        temp = self.head
        if temp is None : 
            print("Empty list")
            return 
        
        while temp.next : 
            temp = temp.next

        while temp : 
            print(temp.data , end = " ")
            temp = temp.prev
        print("finish")
# create a linked list 

l1 = LinkedList()
l1.insertEnd(1)
l1.insertEnd(2)
l1.insertEnd(3)
l1.display()  
l1.backDisplay()
