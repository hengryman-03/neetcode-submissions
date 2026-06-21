class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights) - 1

        maxA = 0

        while i < len(heights) and j > 0:
            maxA = max(maxA, min(heights[i], heights[j])* (j-i))

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxA
        