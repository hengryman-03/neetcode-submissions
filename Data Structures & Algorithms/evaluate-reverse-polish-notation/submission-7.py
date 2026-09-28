class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        
        operators = ["+", "/", "-", "*"]
        stack = []
        start = False
        res = 0
        for i in range(len(tokens)):
            val = tokens[i]
            if val in operators:
                first = stack.pop()
                second = stack.pop()
                if val == "+":
                    res = int(first) + int(second) 
                if val == "*":
                    res = int(first) * int(second)
                if val == "-":
                    res = int(second) - int(first)
                if val == "/":
                    res = int(int(second) / int(first))
                stack.append(res)
            else:
                res = int(val)
                stack.append(val)
        return res