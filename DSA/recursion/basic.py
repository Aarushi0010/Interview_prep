# print name n times 

def name(user , n):
    if n <= 0 :
        return
    
    print(user)

    name(user , n-1)

name('Aarushi' , 6)
