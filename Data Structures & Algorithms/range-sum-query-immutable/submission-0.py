class NumArray:

    def __init__(self, nums: List[int]):
        res =[0] * (len(nums) +1)

        for i in range(len(nums)):
            res[i+1] = res[i] + nums[i]
        self.nums = res

        

        

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)