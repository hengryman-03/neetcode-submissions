class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        i = 0
        right = len(nums) - 1

        while i <= right:

            if nums[i] == 0:
                # your code
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif nums[i] == 1:
                # your code
                i += 1
                
            else:  # nums[i] == 2
                # your code
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

        return nums