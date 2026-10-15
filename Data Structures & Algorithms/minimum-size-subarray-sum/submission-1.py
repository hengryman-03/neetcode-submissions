class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 1

        curr_sum = nums[i]
        min_len = float("INF")

        while j < len(nums) + 1:
            if curr_sum >= target:
                min_len = min(j-i, min_len)
                curr_sum -= nums[i]
                i += 1
                print("minus: " + str(curr_sum))
                print("len: " + str(min_len))
                
            else:
                if j < len(nums):
                    curr_sum += nums[j]
                    print(curr_sum)
                j += 1
            
        return min_len if min_len != float("INF") else 0
            
