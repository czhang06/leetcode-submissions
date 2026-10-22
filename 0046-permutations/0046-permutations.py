class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(used, curr):
            if len(curr) == len(nums):
                result.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    curr.append(nums[i])
                    used.add(nums[i])
                    backtrack(used, curr)
                    n = curr.pop()
                    used.remove(n)
        
        backtrack(set(), [])
        return result