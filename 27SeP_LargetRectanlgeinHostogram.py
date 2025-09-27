class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        Stack = []
        for i,h in enumerate(heights):
            start = i
            while Stack and Stack[-1][1] > h:
                index,height = Stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            Stack.append((start,h))
        
        for i,h in Stack:
            maxArea = max(maxArea, h * ( len(heights) - i))
        return maxArea

        
