class Queue():
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        

    def isFull(self):
        return len(self.queue) == self.capacity
    
    def isEmpty(self):
        return len(self.queue) == 0 
    
    def enqueue(self , x):
        if self.isFull():
            print("Already Full!")
        
        self.queue.append(x)
        return True 
    
    def dequeue(self):
        if self.isEmpty():
            print("empty list!")
        
        return self.queue.pop(0)
    
    def getFront(self):
        if self.isEmpty():
            return -1
        
        return self.queue[0]
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[-1]
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        if self.isEmpty():
            return -1
        print(self.queue)



q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.display()
print(q.size())