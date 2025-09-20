class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Prefix_array = [0]*n
        Suffix_array = [0]*n
        Prefix_array[0],Suffix_array[n-1] = 1,1 
        for i in range(1,n):
            Prefix_array[i] = Prefix_array[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            Suffix_array[i] = Suffix_array[i+1]*nums[i+1]
        res = [0]*n
        for i in  range(n):
            res[i] = Prefix_array[i] * Suffix_array[i]
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res    
