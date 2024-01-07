# Given an integer array nums, return the number of all the arithmetic subsequences of nums.

# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [{} for _ in range(n)]  # 2D array to store the counts

        total_count = 0  # Total count of arithmetic subsequences

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
                dp[i][diff] = dp[i].get(diff, 0) + 1
                total_count += dp[j].get(diff, 0)

        return total_count

#HARD pronblem asked by MAANG - very imprtatnt question - need to visit atleast 5 times
