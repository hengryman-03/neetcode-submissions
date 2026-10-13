class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for i, val in enumerate(s):

            if val == "]":
                string = ""
                while stack and stack[-1] != "[":
                    string += stack.pop()
                stack.pop() # remove "["
                
                num = ""
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                length = int(num[::-1])  
                res = ""
                for i in range(length):
                    res += string
                stack.append(res)
                print(res)
            else:
                stack.append(val)
        
        final = ""
        while stack:
            final += stack.pop()
        return final[::-1]