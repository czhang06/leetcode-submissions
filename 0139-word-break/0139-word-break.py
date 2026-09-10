class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                if len(word) + i > len(s):
                    continue
                correct = True
                for n in range(len(word)):
                    if word[n] != s[i + n]:
                        correct = False
                        break
                if correct:
                    dp[i + len(word)] = True
        return dp[len(s)]
                