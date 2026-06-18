class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        print(arr)

        for i in range(len(arr) - 1, -1 ,-1):
            if arr[i].isspace() == False and arr[i] != "":
                arr[i].strip()
                return len(arr[i])
        
        return 0
        