class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
            if total > target:
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return result