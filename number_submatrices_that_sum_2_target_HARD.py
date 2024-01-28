# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Calculate prefix sum for each row
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]

        # Iterate over all possible pairs of columns
        for col1 in range(cols):
            for col2 in range(col1, cols):
                prefix_sum = {0: 1}
                current_sum = 0

                # Iterate over all rows
                for row in range(rows):
                    current_sum += matrix[row][col2] - (matrix[row][col1 - 1] if col1 > 0 else 0)
                    count += prefix_sum.get(current_sum - target, 0)
                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count
        
