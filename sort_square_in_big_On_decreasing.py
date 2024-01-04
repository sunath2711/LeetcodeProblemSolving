#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#good problem. using the concept of two pointers to keep track from front and back two different pointers are taken
#the sqaures are taken and then compared - if left is smaller push it into new array and take pointer of left ahead same for right 
#run this in a while till left <= right
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_index = 0
        right_index = n-1
        sq_array = [0]*n
        sq_array_index = n-1
        
        while left_index <= right_index:
            left_square = nums[left_index] ** 2
            right_square = nums[right_index] ** 2
            
            if left_square > right_square:
                sq_array[sq_array_index] = left_square
                left_index += 1
            else:
                sq_array[sq_array_index] = right_square
                right_index -= 1
            sq_array_index -= 1
            
            
        return sq_array 
