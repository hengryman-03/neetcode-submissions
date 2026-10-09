class Solution:
    def simplifyPath(self, path: str) -> str:
        
        new = path.split("/")

        test = []
        for word in new:
            if word != "":
                test.append(word)
        stack = []

        for i, word in enumerate(test):
            if word == "..":
                if stack:
                    stack.pop()
                    continue
                else:
                    continue

            if word == ".":
                continue 
            stack.append(word)
        

        return "/" + "/".join(stack)
            



