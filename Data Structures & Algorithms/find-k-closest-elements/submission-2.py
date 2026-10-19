class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        curr = arr[:k]
        diff = x - curr[0]

        for ix in range(k, len(arr)):
            curr_diff = abs(x - arr[ix])
            print(curr_diff, diff)
            if curr_diff == diff and curr[0] < arr[ix]:
                break
            elif curr_diff < diff:
                print(ix-k+1, ix+1)
                curr = arr[ix-k+1: ix+1]
                diff = x - arr[ix-k+1]
        return curr
            
