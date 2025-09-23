class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        Stack = []
        val = 0
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                Stack.append(int(tokens[i]))
            else:
                a = Stack.pop()
                b = Stack.pop()
                if tokens[i] == "+":
                    val = b+a
                elif tokens[i] == "-":
                    val = b-a
                elif tokens[i] == "*":
                    val = b*a
                elif tokens[i] == "/":
                    val = int(float(b)/a)
                Stack.append(val)
        return Stack[-1]

        
