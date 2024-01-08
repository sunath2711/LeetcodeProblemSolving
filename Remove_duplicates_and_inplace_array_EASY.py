# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#python used dictionary to store once occuring element , if occuring second time dont add and take pointer 2 ahead and 1st pointer at inital place to replace with that 
#for next unique place
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,0
        dups = {}
        while j < len(nums):
            if nums[j] in dups:
                j+=1
            else:
                dups[nums[j]] = 1
                nums[i] = nums[j]
                i+=1
                j+=1
        return i
