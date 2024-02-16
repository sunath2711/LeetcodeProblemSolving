# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        counts = Counter(arr)
        heap = list(counts.values())
        heapq.heapify(heap)
        
        res = len(heap)
        

        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                res -= 1
        return res        
 
