class Queue:
    def __init__(self , capacity):
        self.queue = [None] * capacity
        self.front = 0 
        self.rear = -1
        self.size = 0 
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0 

    def enqueue(self,x):
        if self.isFull():
            print("Queue is already full")

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = x
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")

        x = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return x
    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def getRare(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    
    def display(self):
        if self.isEmpty():
            return -1
        
        items = []
        count = 0 
        index = self.front

        while count < self.size:
            items.append(self.queue[index])
            index = (index + 1) % self.capacity
            count += 1

        print("Queue:", items)

q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.display()