class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res, sol = [],[]
        
        def backtrack(i):
            if i == n:
                res.append(sol[:]) # must be copy and not reference, since sol can keep changing
                return 
                
            # do not pick nums[i]
            backtrack(i+1)		
            
            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop() # pop the appended temporary solution
            

        backtrack(0)
        return res