# sorting technique where we find the minimum element and swap it with the index element

def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_ind = i 

        for j in range(i+1 , n):
            if arr[j] < arr[min_ind]:
                min_ind = j 

        arr[i] , arr[min_ind] = arr[min_ind] , arr[i]

def display(arr):
    for i in arr : 
        print(arr[i])
        
    print()
    
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print("Original array : ")
    print(arr)

    selectionSort(arr)

    print("sorted array : ")
    print(arr)