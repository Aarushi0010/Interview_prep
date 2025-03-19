tree = [None] * 10

def root(key):
    if tree[0] != None:
        print('root already exists')
    else: 
        tree[0] = key

def left(key , parent):
    if tree[parent] == None:
        print('no parent exists')

    else:
        tree[(parent * 2) + 1 ] = key

def right(key , parent):
    if tree[parent] == None :
        print('parent does not exist')

    else:
        tree[((parent * 2) + 2)] = key

def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i] , end = ' ')

        else : 
            print('-' , end = ' ')

root('A')
left('B' , 0)
right('C' , 0 )
left('D' , 1 )

print_tree()