class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums = set(nums)
        nums = sorted(nums)

        print(nums)
        result = [nums[0]]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == result[-1] + 1:
                result.append(nums[i])
            else:
                count = max(count, len(result))
                result = [nums[i]]

        count = max(count, len(result))

        return count 


        

        