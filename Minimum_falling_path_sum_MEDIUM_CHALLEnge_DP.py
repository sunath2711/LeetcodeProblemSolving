class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0][:]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1):min(n, j+2)])

        return min(dp[-1])
        
