# print fabonacci series for a number n 

def fabonacci(n):
    if n == 0 :
        return 0 
    
    if n == 1:
        return 1 
    
    return fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(6))