# implementation using Linked List 
# base node 
class Node :
    def __init__(self, value) :
        self.value = value
        self.next = None 

class LinkedNode :
    def __init__(self):
        self.top = None
        self.size = 0 

    # adding elements
    def push(self , value):
        new = Node(value)
        new.next = self.top
        self.top = new
        self.size += 1 

        print(f"Pushed : {value}")
        return 
    
    def isEmpty(self):
        return self.top == None

    # removing element 
    def pop(self):
        if self.isEmpty():
            print("stack underflow!")
            return 
        
        popped_val = self.top.value
        self.top = self.top.next
        self.size -= 1

        return popped_val
    
    def peek(self):
        if self.isEmpty:
            return None
        return self.top.value
    
    def display(self):
        if self.isEmpty():
            print(f"(Empty stack)")
            return 
        
        current = self.top
        print("Stack from top to bottom : ")
        while current :
            print(f"{current.value}")
            current = current.next

if __name__ == '__main__':
    stack = LinkedNode()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.display()

    stack.pop()
    stack.display()