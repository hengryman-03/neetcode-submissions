class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return 
        
        move = k % len(nums)
        for i in range(move):
            temp = nums[0]
            nums[0] = nums[-1]
            j = 1
            while j < len(nums):
                nums[j], temp = temp, nums[j]
                j += 1

        


        