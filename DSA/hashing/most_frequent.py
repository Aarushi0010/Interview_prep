# to find the most frequent element in an array 
import math as mt
def frequent(arr , n):
    
    #inserting elements in hash 
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1 

        else:
            Hash[arr[i]] = 1 

    # find max frequency
    max_count = 0 
    res = -1
    for i in Hash:
        if(max_count < Hash[i]):
            res = i 
            max_count = Hash[i] 

    return res

arr = [ 40,50,30,40,50,30,30] 
n = len(arr)
print(frequent(arr, n)) 