class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            ix, jx = i + 1, len(nums) - 1

            while ix < jx:
                if nums[ix] + nums[jx] == target:
                    result.append([nums[i], nums[ix], nums[jx]])

                    
                    while ix < jx and nums[ix] == nums[ix + 1]:
                        ix += 1
                    while ix < jx and nums[jx] == nums[jx - 1]:
                        jx -= 1

                    ix += 1
                    jx -= 1

                elif nums[ix] + nums[jx] < target:
                    ix += 1
                elif nums[ix] + nums[jx] > target:
                    jx -= 1
                
        return result

                
