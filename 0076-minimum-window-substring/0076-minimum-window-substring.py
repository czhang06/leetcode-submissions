class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        count = defaultdict(int)
        result = ""

        letters = set(t)
        complete = set()

        for i in range(len(t)):
            d[t[i]] += 1
        
        l = 0
        r = 0

        result = ""

        while True:
            count[s[r]] += 1
            if count[s[r]] >= d[s[r]] and s[r] in letters:
                complete.add(s[r])
            r += 1
            while l < len(s) and count[s[l]] > d[s[l]]:
                count[s[l]] -= 1
                l += 1
            if len(complete) == len(letters):
                if r - l < len(result) or result == "":
                    result = s[l:r]
            if r >= len(s):
                break
        return result

