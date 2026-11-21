class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nxt = nums[i] - 1
                nums[i], nums[nxt] = nums[nxt], nums[i]
            
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

