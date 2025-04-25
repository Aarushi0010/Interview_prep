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

if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(20)
    q.enqueue(10)