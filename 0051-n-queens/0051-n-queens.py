class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = [0] * n
        diagl, diagr = ([0] * (n * 2 - 1)), ([0] * (n * 2 - 1))
        grid = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                result.append(["".join(row) for row in grid])
                return
            for c in range(n):
                if cols[c] or diagl[r - c + n - 1] or diagr[r + c]:
                    continue
                
                grid[r][c] = "Q"
                cols[c] = diagl[r - c + n - 1] = diagr[r + c] = 1
                backtrack(r + 1)
                grid[r][c] = "."
                cols[c] = diagl[r - c + n - 1] = diagr[r + c] = 0
        backtrack(0)
        return result