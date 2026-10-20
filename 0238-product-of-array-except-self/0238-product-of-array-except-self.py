class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ltr = [1]
        rtl = [1]

        for i in range(len(nums)):
            ltr.append(ltr[-1] * nums[i])
            rtl.append(rtl[-1] * nums[-(i + 1)])

        result = []
        for i in range(len(nums)):
            result.append(ltr[i] * rtl[-(i + 2)])
        return result
