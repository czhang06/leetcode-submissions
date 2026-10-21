class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        result = 1

        if len(s) == 0:
            return 0

        d = set()
        d.add(s[l])

        while r < len(s):
            if s[r] not in d:
                d.add(s[r])
                result = max(result, r - l + 1)
                r += 1
            else:
                d.remove(s[l])
                l += 1

        return result   