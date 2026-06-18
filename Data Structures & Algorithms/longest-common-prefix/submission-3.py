class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word = strs[0]

        while len(word) > 0:
            for ix, i in enumerate(strs):
                if i.startswith(word) and i != "":
                    if ix == len(strs) -1:
                        return word
                else:
                    word = word[:len(word) - 1]
                    break
        
        return ""