class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def preorder(node):
    if node is None :
        return 
    print(node.data , end=' ')
    preorder(node.left)
    preorder(node.right)

# In-order traversal
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data ,end=' ' )
    inorder(node.right)

# Post-order traversal
def postorder(node):
    if node is None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data , end = ' ')

# level-order traversal
def bfs(root):
    if root is None:
        return 
    queue = [root]
    while queue : 
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# driver code
if __name__ == '__main__':
    root = Node(50)
    root.left = Node(40)
    root.right = Node(35)
    root.left.left = Node(20)
    root.right.right = Node(15)

    print('Preorder DFS : ', end = ' ')
    preorder(root)

    print('\nInorder DFS : ', end=' ')
    inorder(root)

    print('\nPostorder DFS : ' , end = ' ')
    postorder(root)

    print('\nLevelorder BFS : ' , end= ' ')
    bfs(root)
