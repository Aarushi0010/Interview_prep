class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

def search(root , target):

    if root is None:
        return False 
        
    if root.data == target:
        return True
        
    left_check = search(root.left , target)
    right_check = search(root.right , target)

    return left_check or right_check

if __name__ == '__main__':
    root = Node(2)
    root.right = Node(3)
    root.left = Node(4)
    root.left.left = Node(5)
    root.right.right = Node(6)

    target = 4
    if search(root , target):
        print(f'{target} is present in BT')

    else : 
        print(f'Could not find {target} in BT')    