class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'{', '[', '('}
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                b = stack.pop()
                if b == "{" and bracket != "}":
                    return False
                elif b == "(" and bracket != ")":
                    return False
                elif b == "[" and bracket != "]":
                    return False
        
        if not stack:
            return True
        else:
            return False