# sorting where we compare the two items and swap to push the maximum to last position

def bubbblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False 

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True

        if(swapped == False):
            break 

if __name__ =='__main__':
    arr = [13, 46 , 24 , 52 , 20 , 9]

    print("given array : " , arr)

    bubbblesort(arr)
    print("sorted array : " , arr)

