# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i,j = 0,0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i    

#take two pointers i and j starting zero
# j is fast pointer and i is slow pointer
# as we compare nums[j] with val given. if the value is same then we increment then we increment j since that value doesnt need to be removed
#if the nums[j] is not same as val, then we swap with current i and increase i and j both
