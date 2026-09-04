class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or s1 == "" or s2 == "":
            return False

        sorted_s1 = "".join(sorted(s1))
        

        ix = 0
        while len(s1) + ix < len(s2) + 1:
            curr = s2[ ix : len(s1) + ix]
            sorted_curr = "".join(sorted(curr))
            if sorted_curr == sorted_s1:
                return True 
            ix += 1
        
        return False