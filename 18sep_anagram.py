class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_letter = {}
        for i in range(len(s)):
            if s[i] in map_letter:
                map_letter[s[i]] = map_letter[s[i]] + 1
            else:
                map_letter[s[i]] = 1
        for i in range(len(t)):
            if t[i] in map_letter:
                map_letter[t[i]] = map_letter[t[i]] - 1
            else:
                return False

        for i in map_letter:
            if map_letter[i] != 0:
                return False
        return True                
    


        
