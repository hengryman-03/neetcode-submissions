class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)

        res, sol = [], []

        def backtracking(ix, val):
            if val == 0:
                res.append(sol[:])
                return 

            if val < 0 or ix == len(candidates):
                return 

            sol.append(candidates[ix])
            backtracking(ix+1, val-candidates[ix])
            sol.pop()

            next_ix = ix + 1
            while next_ix < len(candidates) and candidates[ix] == candidates[next_ix]:
                next_ix += 1
            
            backtracking(next_ix, val)
        
        backtracking(0, target)
        return res
            
