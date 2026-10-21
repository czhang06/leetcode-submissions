class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = result = 0

        last = {}
        

        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1
            last[c] = r
            result = max(result, r - l + 1)
        
        return result