# There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

# A point of the cheese with index i (0-indexed) is:

# reward1[i] if the first mouse eats it.
# reward2[i] if the second mouse eats it.
# You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

# Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.

class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """    
        arr = zip(reward1, reward2)
        result = 0
        sortedarr = sorted(arr, key=lambda x: x[0]-x[1], reverse = True)
        for pair in sortedarr:
            if k:
                k -= 1
                result += pair[0]
            else:
                result += pair[1]    
        return result
#time complexity for this is nlog(n) required for sorted function python. Good problem - using zip and sorted on difference , where the difference is sorted for first K we use
#reward1 and then reward2
