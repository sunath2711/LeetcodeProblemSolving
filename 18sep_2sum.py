class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_map and index_map[complement] != i:
                return [i, index_map[complement]]



for i, num in enumerate(nums):
    diff = target - num
    if diff in index_map:
        return [index_map[diff], i]
    index_map[num] = i
