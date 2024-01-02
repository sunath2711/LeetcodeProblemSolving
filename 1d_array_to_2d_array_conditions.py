#You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        uniq_values = list(set(nums))
        rows = []
        while nums:
            current_row = []
            for value in uniq_values:
                if value in nums:
                    current_row.append(value)
                    nums.remove(value)
            rows.append(current_row)

        return rows
# first i thought of the approach where i was storing the occurence in dictionaries - which is not best way
#instead make set of unqiue values from the array each time. then if that is present in main array then add to row and delete one occurence from the main array
