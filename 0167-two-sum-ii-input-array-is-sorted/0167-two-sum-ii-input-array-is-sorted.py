class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        curr = numbers[l] + numbers[r]

        while curr != target:
            if curr < target:
                l += 1
            if curr > target:
                r -= 1
            curr = numbers[l] + numbers[r]
        
        return [l + 1, r + 1]