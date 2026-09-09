'''
Strategy:
1. Move r right until the window becomes valid
2. Once valid, move l right to make it smaller
3. Keep shrinking while it is still valid
4. Record the smallest valid window seen
5. When shrinking makes it invalid, expand r again


'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        required = {}
        curr_wind = {}

        for char in t:
            required[char] = required.get(char, 0) + 1

        need = len(required)
        have = 0

        l = 0
        res = [-1, -1]
        res_len = float("INF")

        for i in range(len(s)):
            char = s[i]

            curr_wind[char] = curr_wind.get(char, 0) + 1

            if char in required and curr_wind[char] == required[char]:
                have += 1

            while have == need:
                if i - l + 1 < res_len:
                    res = [l, i + 1]
                    res_len = i - l + 1
                
                rm_curr = s[l]
                curr_wind[rm_curr] -= 1

                if rm_curr in required and curr_wind[rm_curr] < required[rm_curr]:
                    have -= 1
                l += 1

        if res_len == float("INF"):
            return ""

        return s[res[0]:res[1]]
            


        



