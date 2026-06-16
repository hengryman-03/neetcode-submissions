class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = 1
            else:
                mapping[nums[i]] += 1
        sorted_mapping = sorted(mapping.items(), key=lambda x: x[1], reverse=True)


        result = []
        for i in range(k):
            result.append(sorted_mapping[i][0])

        return result