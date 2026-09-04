class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_of_key = {}

        for i in arr:
            if i not in count_of_key:
                count_of_key[i] = 1
            else:
                count_of_key[i] += 1
        
        counter = 1
        for i in arr: 
            if count_of_key[i] == 1:
                if counter == k:
                    return i
                counter += 1
        
        return ""