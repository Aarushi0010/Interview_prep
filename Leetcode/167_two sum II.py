# input array is sorted in ascending order 
# 2 pointer solution for optimal search 


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0 
        right = len(numbers)-1

        while left < right : 
            sum = numbers[left] + numbers[right]

            if(sum > target) : 
                right -=1 
            elif (sum < target) : 
                left += 1
            else : 
                return (left+1 , right+1)
        