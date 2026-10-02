class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = set()

        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i,0) + 1
            if hash_map[i] > (len(nums)/3):
                res.add(i)
        
        return list(res)