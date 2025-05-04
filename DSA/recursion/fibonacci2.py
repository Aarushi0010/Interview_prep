# here we will print the series instead of the entire sum 
def fibonaaci(n):
    if n == 0 :
        return 0 
    
    if n == 1 :
        return [0,1] 
    
    sequence = fibonaaci(n-1)

    sequence.append(sequence[-1] + sequence[-2])

    return sequence

print(fibonaaci(5))