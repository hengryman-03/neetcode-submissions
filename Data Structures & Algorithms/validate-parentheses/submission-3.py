class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s or (len(s) % 2 != 0):
            return False

        paired_par = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        p_stack =[]
        for i in range(len(s)):
            if s[i] not in ["}", "]", ")"]:
                p_stack.append(s[i])
            else:
                if len(p_stack) == 0:
                    return False
                if p_stack.pop() == paired_par[s[i]]:
                    continue;
                else: 
                    return False
        
        if len(p_stack) != 0:
            return False
            
        return True

        