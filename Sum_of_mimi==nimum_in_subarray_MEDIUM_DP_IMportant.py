# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
# # Since the answer may be large, return the answer modulo 109 + 7.
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
 
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n

        # Calculate the next smaller element on the left for each element
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        # Clear the stack for the next iteration
        stack = []

        # Calculate the next smaller element on the right for each element
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        result = 0

        # Calculate the contribution of each element to the final sum
        for i in range(n):
            result = (result + arr[i] * (i - left[i] + 1) * (right[i] - i) % MOD) % MOD

        return result
