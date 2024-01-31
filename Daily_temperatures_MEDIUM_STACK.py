# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you 
# have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: #find the higher
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res   
        
