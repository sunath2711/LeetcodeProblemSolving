# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        i,j = 0,n-1
        count = 0
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        mid = (n//2)
        while i < mid and j > mid-1:
            if s[i] in  vowels:
                count+=1
            if s[j] in  vowels:
                count-=1
            i+=1
            j-=1
        if count == 0:
            return True
        else:
            return False 

