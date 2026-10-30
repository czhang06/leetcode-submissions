class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y, x = len(matrix), len(matrix[0])

        sy, sx = 0, x - 1

        while sy < y and sx > -1:
            curr = matrix[sy][sx]
            if curr == target:
                return True
            if curr < target:
                sy += 1
            if curr > target:
                sx -= 1
        
        return False
            