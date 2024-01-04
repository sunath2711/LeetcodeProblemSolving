# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        total_ops = 0
        if any(value == 1 for value in counts.values()):
            return -1
        else:
            for i in counts.values():
                div = i // 3
                rem = i % 3
                if rem == 1 or rem == 2:
                    rem = 1
                total_ops += (div+rem)
            return total_ops   
