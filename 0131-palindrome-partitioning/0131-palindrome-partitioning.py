class Solution:
    def partition(self, s: str) -> list[list[str]]:

        result = []
        
        def backtrack(start, curr):
            if start == len(s):
                result.append(curr[:])
                return
            for end in range(start, len(s)):
                piece = s[start:end + 1]
                if piece == piece[::-1]:
                    curr.append(piece)
                    backtrack(end + 1, curr)
                    curr.pop()
        backtrack(0, [])
        return result