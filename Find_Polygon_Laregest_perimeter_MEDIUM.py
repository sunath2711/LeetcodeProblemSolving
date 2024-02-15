# You are given an array of positive integers nums of length n.

# A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

# The perimeter of a polygon is the sum of lengths of its sides.

# Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        sum_array = [0]*n
        sum_array[0] = nums[0]
        
        for i in range(1, len(nums)):
            sum_array[i]=sum_array[i-1] + nums[i]
        print(sum_array)
        i = len(nums) - 1
        j = len(nums) - 2
        while j >= 0:
            if sum_array[j] > nums[i]:
                return sum_array[j+1]
            else:
                i-=1
                j-=1
        return -1            

        
        
