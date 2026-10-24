class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d1[s[i]] += 1
            d2[t[i]] += 1

        
        for c in d2:
            if d2[c] != d1[c]:
                return False
        return True