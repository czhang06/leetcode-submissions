class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(curr, remaining):
            result.append(curr)
            for i in range(len(remaining)):
                backtrack(curr + [remaining[i]], remaining[i + 1:])

        backtrack([], nums)
        return result  