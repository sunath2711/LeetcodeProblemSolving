#Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i<j:
            i_val = nums[i]%2
            j_val = nums[j]%2
            if i_val == 0 and j_val == 0:
                i+=1
            elif i_val == 0 and j_val != 0:
                i+=1
                j-=1
            elif i_val != 0 and j_val != 0:
                j-=1
            elif i_val != 0 and j_val == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
         
        return nums
#easy concept two pointers from left and right, based on even and odd move pointers      
