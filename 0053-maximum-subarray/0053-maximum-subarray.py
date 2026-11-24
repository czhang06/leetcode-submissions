class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        result = nums[0]
        curr = 0

        for r in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[r]
            result = max(result, curr)
        return result
       
        