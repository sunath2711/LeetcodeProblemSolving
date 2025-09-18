class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0]*26
            for i in word:
                count[ord(i)-ord('a')] += 1
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())    


        
