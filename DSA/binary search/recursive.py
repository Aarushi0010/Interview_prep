# Here we will create a function to check for target while also changing the values of low , high and mid

def binarySearch (nums : list[int] , low : int , high : int , target : int) : 
    if low > high : 
        return -1
    
    mid = (low + high)//2 
    if (nums[mid] == target) : 
        return mid 
    elif target > nums[mid]:
        return binarySearch(nums , mid+1 , high , target)
    else : 
        return binarySearch(nums , low , mid-1, target)
    
def search(nums: list[int], target: int):
    return binarySearch(nums, 0, len(nums) - 1, target)

if __name__ == '__main__':
    a = a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = search(a , target)
    if ind == -1 :
        print("element does not exist")
    else : 
        print("element is at index : ", ind)