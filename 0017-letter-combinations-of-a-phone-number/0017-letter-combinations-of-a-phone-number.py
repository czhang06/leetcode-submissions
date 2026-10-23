class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        key = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",}

        result = []

        if len(digits) == 0:
            return result

        def backtrack(curr, i):
            if i == len(digits):
                result.append(curr[:])
                return
            for letter in key[digits[i]]:
                curr += letter
                backtrack(curr, i + 1)
                curr = curr[:-1]
        
        backtrack("", 0)
        return result