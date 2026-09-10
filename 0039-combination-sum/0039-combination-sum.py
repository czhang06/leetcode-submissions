class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []

        candidates.sort()

        def backtrack(arr, total, i):
            if total > target:
                return
            if total == target:
                result.append(arr[:])
                return
            for j in range(i, len(candidates)):
                num = candidates[j]
                arr.append(num)
                total += num
                backtrack(arr, total, j)
                arr.pop()
                total -= num

        backtrack([], 0, 0)

        return result            
                