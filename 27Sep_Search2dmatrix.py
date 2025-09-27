class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n = len(matrix),len(matrix[0])
        top,bottom = 0,m-1

        while top <= bottom:
            mid_row = (top+bottom)//2
            row = -1
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                row = mid_row
                break
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1
            
        if row == -1:
            return False

        left,right = 0,n-1
        while left <= right:
            mid = (left+right)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid+1
            else:
                right = mid - 1

        return False 
