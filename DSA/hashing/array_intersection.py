# to return interestion of two arrays without any duplicate values

def intersection(a , b):
    res = []

    for i in a :
        for j in b : 
            if i == j and i not in res:
                res.append(i)
    return res 

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

res = intersection(a,b)
print(' '.join(map(str,res)))