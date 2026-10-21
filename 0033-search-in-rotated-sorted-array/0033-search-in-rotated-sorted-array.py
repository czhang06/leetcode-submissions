class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            else:
                if nums[m] > nums[-1]:
                    l = m + 1
                else:
                    r = m - 1
        
        r = l + len(nums) - 1
        nums.extend(nums)
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m % (len(nums)//2)
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
