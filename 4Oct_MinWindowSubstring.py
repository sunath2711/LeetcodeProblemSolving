class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_chars = {}
        for ch in t:
            required_chars[ch] = required_chars.get(ch,0) + 1
        # built frequency map for t above

        remaining_to_match = len(t)
        left = best_start = best_end = 0

        for right,char in enumerate(s, start=1):
            if char in required_chars and required_chars[char] > 0:
                remaining_to_match -= 1 # if a needed char is seen so we reduce the 
            
            if char in required_chars:
                required_chars[char] -= 1
            
            if remaining_to_match == 0:
                while left < right:
                    left_char = s[left]

                    if left_char not in required_chars or required_chars[left_char] < 0:
                        if left_char in required_chars:
                            required_chars[left_char] += 1
                        left+=1
                    else:
                        break

                if best_end == 0 or right - left < best_end - best_start:
                    best_start, best_end = left,right

        return s[best_start:best_end]
