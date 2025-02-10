# initializing the node 
class Node :
    def __init__(self, data) :
        self.data = data 
        self.next = None

# initializing the linked list 
class LinkedList : 
    def __init__(self): 
        self.head = None 

    def insertnode (self , data):
        new_node = Node(data)
        #if list is empty 
        if self.head ==  None : 
            self.head = new_node
            return 
        
        temp = self.head
        while temp.next : 
            temp = temp.next 

        temp.next = new_node

    def display(self) :
        temp = self.head
        while temp : 
            print(temp.data , end ="->")
            temp = temp.next
        print("None")

l1 = LinkedList()
l1.insertnode(10)
l1.insertnode(20)

l1.display()