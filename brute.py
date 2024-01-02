#2 Sum problem to return the indices of the element in the list whose sum is the target [2,7,15,11] with T=9 returns [0,1]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(0,len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output    
