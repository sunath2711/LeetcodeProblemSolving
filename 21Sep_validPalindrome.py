class Solution:
    def isPalindrome(self, s: str) -> bool:
        good_list = list(''.join([c.lower() for c in s if c.isalnum()]))
        i = 0
        n = len(good_list)
        for i in range(0,n//2):
            if good_list[i] != good_list[n-i-1]:
                return False
            else:
                continue
        return True


#extra list is not good above
#make it less Space complex by directly iteartin over string

