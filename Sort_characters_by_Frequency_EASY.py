class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        sorted_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        final_string = ''.join([key * freq[key] for key in sorted_keys])
        return final_string



# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.
