class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        def twoSum(start,end,target):
            res = []
            while start < end:
                curr = nums[start] + nums[end]
                if curr == target:
                    res.append([nums[start],nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif curr > target:
                    end -= 1
                else:
                    start+=1    
            return res

        final_res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            twoSumRes = twoSum(i+1,len(nums)-1,target)
            for pair in twoSumRes:
                final_res.append([nums[i]] + pair)
        return final_res

        
