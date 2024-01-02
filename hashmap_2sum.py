#approach with hashmap inpython
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            comple = target - nums[i]
            if comple in hashmap and hashmap[comple] != i:
                return [i,hashmap[comple]]
