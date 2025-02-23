MAX_SIZE = 50
a = [0]*MAX_SIZE  # stack is created
top = -1

def push(ele):
    global top 
    if top <= MAX_SIZE - 1: 
        top += 1        #stack traversal 
        a[top] = ele
        print(f"Pushed : {ele}" ,)
    
    else :
        print(f"Stack overflow!")

def pop():
    global top
    if top >= 0 :
       ele = a[top]
       top -= 1
       print(f"Popped : {ele}")

    else :
        print(f"Stack underflow!")

