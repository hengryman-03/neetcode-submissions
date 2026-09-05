class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals = sorted(intervals, key=lambda x:x[0]) # sorting intervals using x[0]: start_i

        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = ans[-1]
            prev_end = prev[1]
            curr_start = intervals[i][0]
            if curr_start <= prev_end:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                ans.append(intervals[i])
        return ans



