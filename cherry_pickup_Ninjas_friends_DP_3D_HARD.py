# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid),len(grid[0])
        cache = {}

        def dfs(r,c1,c2):
            if (r,c1,c2) in cache:
                return cache[(r,c1,c2)]
            if c1 == c2 or min(c1,c2) < 0 or  max(c1,c2) == COLS:
                return 0
            if r == ROWS - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1_d in [-1,0,1]:
                for c2_d in [-1,0,1]:
                    res = max(
                        res,
                        dfs(r+1,c1+c1_d,c2+c2_d)
                    )
            cache[(r,c1,c2)] = res + grid[r][c1] + grid[r][c2]
            return cache[(r,c1,c2)]
        return dfs(0,0,COLS-1)                 
