class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1

        result = min(height[r], height[l]) * (r - l)

        while l < r:
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
            result = max(result, min(height[r], height[l]) * (r - l))

        return result