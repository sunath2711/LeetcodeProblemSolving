class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        S = len(set(nums))

        return not N == S
