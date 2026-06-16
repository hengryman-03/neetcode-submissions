class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t): 
            return False
        
        count = 0
        dups = set()
        for i in range(len(t)):
            curr = t[i]
            if curr == s[count] and s[count] not in dups:
                count += 1
            if count == len(s):
                return True
        return False