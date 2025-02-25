class Queue:
    def __init__(self):
        self.value = []

    def enqueue(self , x):
        self.value.append(x)

    def dequeue(self):
        front = self.values[0]
        self.value = self.value[1:]
        return front
    
    def display(self):
        for i in range (len(self.value)):
            print(self.value[i])
        print()
    
q = Queue()
q.enqueue(1)
q.display()