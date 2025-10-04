class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        sort_s1 = "".join(sorted(s1))
        for i in range(0,m-n+1,1):
            temp_str = s2[i:i+n]
            sort_temp = "".join(sorted(temp_str))
            if sort_temp == sort_s1:
                return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n>m:
            return False
        def idx(c):
            return ord(c)-ord('a')

        s1_count = [0]*26
        window = [0]*26
        for i in range(n):
            s1_count[idx(s1[i])] += 1
            window[idx(s2[i])] += 1
        
        if s1_count == window:
            return True
        
        for i in range(n,m):
            window[idx(s2[i])] += 1
            window[idx(s2[i-n])] -= 1

            if s1_count == window:
                return True
        return False

        

            
