class Node():
    def __init__(self , data):
        self.data = data
        self.next = None

    
class ListQueue():
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 

    def isEmpty(self):
        return self.head is None
    
    def enqueue(self , item):
        new_node = Node(item)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        else :
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1 

    def dequeue(self):

        if self.isEmpty():
            return -1
        
        item = self.head.data

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -=1

        return item
    
    def peek(self) -> int:
        if self.head is None:
            return -1
        return self.head.data
    
    def __len__(self):
        return self.size
    

    def __str__(self):
        if self.isEmpty():
            return "Queue : []"
        
        items = []
        current = self.head
        while current: 
            items.append(str(current.data))

            current = current.next

        return "Queue: [" + ", ".join(items) + "]"
    

if __name__ == '__main__':
    queue = ListQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)

    print(queue.dequeue())
    print(queue)

    print(queue.peek())
    print(len(queue))