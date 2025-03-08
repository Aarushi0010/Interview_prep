class Node:
    def __init__(self,key):
        left = None
        right = None 
        value = key

firstnode = Node(40)
secondnode = Node(10)
thirdnode = Node(20)
fourthnode = Node(15)

firstnode.left = secondnode
firstnode.right = thirdnode
thirdnode.left = fourthnode
