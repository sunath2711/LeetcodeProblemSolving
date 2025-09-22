class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = []
        right_max = [0]*n
        leftMax = -9999
        rightMax = -9999
        for i in range(0,n):
            leftMax = max(leftMax, height[i])
            left_max.append(leftMax)

        for i in range(n - 1, -1, -1):
            rightMax = max(rightMax, height[i])
            right_max[i] = rightMax
        
        total_water = 0
        for i in range(1,n-1):
            total_water += min(left_max[i],right_max[i]) - height[i]
        return total_water

