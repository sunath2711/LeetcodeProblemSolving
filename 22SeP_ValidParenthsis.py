class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]*len(s)
        i = 0
        top = 0
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack[top] = s[i]
                top+=1
            else:
                if top == 0:
                    return False
                top-=1
                top_element = stack[top]
                
                if s[i] == "]" and top_element!="[":
                    return False
                if s[i] == ")" and top_element!="(":
                    return False
                if s[i] == "}" and top_element!="{":
                    return False

        return top == 0
