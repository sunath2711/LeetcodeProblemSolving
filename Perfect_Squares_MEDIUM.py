# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1)
        dp[0] = 0

        squares = [x**2 for x in range(0, n) if x**2<=n]

        for target in range(1,n+1):
            dp[target] = target
            for square in squares: 
                if target - square < 0: 
                    break
                dp[target] = min(dp[target], 1+dp[target-square])
        return dp[n]           

        
