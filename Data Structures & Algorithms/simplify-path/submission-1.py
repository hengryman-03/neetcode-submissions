class Solution:
    def simplifyPath(self, path: str) -> str:
        
        new = path.split("/")
        print(new)

        test = []
        for word in new:
            if word != "":
                test.append(word)
        print(test)

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
        
        print(stack)

        return "/" + "/".join(stack)
            



