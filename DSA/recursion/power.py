def power(x, n):
    if x == 0 :
        return 0 
    
    if n == 0 :
        return 1 
    
    res =   power(x,n//2)
    res = res * res 

    
    if n % 2 == 1 :
        return res * x 
    
    return res

print(power(2,3))