class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        l = result = maxf = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, count[ord(s[r]) - ord('A')])
            while r - l + 1 - maxf > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result
