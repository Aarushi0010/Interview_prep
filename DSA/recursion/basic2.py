# print numbers from n down to 1 and then print "Liftoff" and then print numbers from 1 to n

def countOff(n):

    if n ==0:
        print('LiftOff')
        return 
    
    print(n)
    countOff(n-1)

    print(n)    

countOff(5) 