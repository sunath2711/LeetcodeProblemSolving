Set method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        S = len(set(nums))

        return not N == S

Hashmap method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums:
            if i in map:
                return True
            else:
                map[i] = 1
        return False            
