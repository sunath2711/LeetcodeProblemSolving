# given an integer array nums, return the length of the longest strictly increasing 
# subsequence

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = [nums[0]]

        for num in nums[1:]:
            if num > lis[-1]:
                lis.append(num)
            else:
                # Use binary search to find the position to insert the current element
                index = bisect.bisect_left(lis, num)
                lis[index] = num

        return len(lis)  

#python  bisect function is used herer
