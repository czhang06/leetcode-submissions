class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        y, x = len(matrix) - 1, len(matrix[0]) - 1

        l = 0
        r = x
        t = 0
        b = y
        while t <= b:
            my = (t + b) // 2

            if target > matrix[my][-1]:
                t = my + 1
            elif target < matrix[my][0]:
                b = my - 1
            else:
                break
        else:
            return False
        
        while l <= r:
            mx = (l + r) // 2

            if matrix[my][mx] == target:
                return True
            elif matrix[my][mx] < target:
                l = mx + 1
            else:
                r = mx - 1
        
        return False

        