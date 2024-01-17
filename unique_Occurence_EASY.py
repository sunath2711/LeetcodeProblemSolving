class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        D = {}
        for i in arr:
            if i in D.keys():
                D[i] += 1
            else:
                D[i] = 1
        print(D)        
        return len(D.values()) == len(set(D.values()))
