# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

    # Check if there is only one set bit in the binary representation of n
        return bin(n).count('1') == 1
        
