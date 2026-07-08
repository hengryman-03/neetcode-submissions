class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        max_length = 0
        left = 0

        placeholder = set()

        for i in range(len(s)):
            while s[i] in placeholder:
                placeholder.remove(s[left])
                left += 1
            placeholder.add(s[i])
            max_length = max(max_length, i - left + 1)

        return max_length


        



        