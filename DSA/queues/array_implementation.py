class ArrayQueue : 
    def __init__(self , capacity = 10):
        self.capacity = capacity
        self.start = 0
        self.end = 0
        self.currSize = 0 
        self.arr = [0]*capacity


    def isFull(self):
        return self.currSize == self.capacity
    
    def isEmpty(self):
        return self.currSize ==0 

    def enqueue(self, item : int) -> None:

        if self.isFull():
            return -1
        

        self.end = (self.end + 1) % self.capacity
        self.arr[self.end] = item
        print(item , 'added')
        self.currSize += 1

    def dequeue(self) -> int : 

        if self.isEmpty():
            return -1
        
        self.start = (self.start + 1)% self.capacity
        self.currSize -= 1
        print('popped at index: ', self.start ,'value : ' ,self.arr[self.start])

    
    def peek(self) -> int : 
        if self.isEmpty():
            return -1
        
        print (self.arr[self.start])
    
    def size(self) -> int:
        print (self.currSize)


if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.peek()
    q.size()