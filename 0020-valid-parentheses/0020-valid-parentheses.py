class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}':'{', ']':'[', ')':'('}

        for i in range(len(s)):
            b = s[i]
            if b in brackets:
                if not stack or stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)
        
        if not stack:
            return True
        return False