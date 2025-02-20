MAX_SIZE = 10
a = [0]*MAX_SIZE
def peep():
    global top 
    if top >= 0 :
        ele = a[top]
        return ele
    
    else : 
        return -1
    
def is_Full():
    return top>=  MAX_SIZE

def is_Empty():
    return top == -1
