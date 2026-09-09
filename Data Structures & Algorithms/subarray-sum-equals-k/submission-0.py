class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_list = { 0 : 1 }
        prefix_sum = 0

        res = 0

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_list:
                res += prefix_list[(prefix_sum - k)]

            prefix_list[prefix_sum] = prefix_list.get(prefix_sum, 0) + 1

        return res
            
