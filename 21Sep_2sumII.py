#List is sorted alreay so dont use the map approach

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left < right:
            num_sum = numbers[left] + numbers[right]
            if num_sum == target:
                return [left+1,right+1]
            elif num_sum < target:
                left+=1
            else:
                right-=1
        return False
