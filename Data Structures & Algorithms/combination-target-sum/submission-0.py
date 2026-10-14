class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        res, curr = [], []

        def backtracking(i, val):
            if val == 0:
                res.append(curr[:])
                return

            if val < 0 or i == n:
                return

            # PICK nums[i]
            curr.append(nums[i])
            backtracking(i, val - nums[i])
            curr.pop()

            # SKIP nums[i]
            backtracking(i + 1, val)

        backtracking(0, target)
        return res