class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        res = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            elif nums[i] < nums[j]:
                nums[i+1] = nums[j]
                res += 1
                i += 1
                j += 1
            
        return len(nums[:res])