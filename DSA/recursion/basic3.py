# you have to find out the sum of the digits in a number 

def sumD(n):
    if n < 10:
        return n
    
    i = n % 10 
    print(i + sumD(n//10)) 


sumD(24)