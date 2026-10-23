class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        result = False
        def bt(y, x, i):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= w or y >= h or i >= len(word) or board[y][x] != word[i] or (y, x) in used:
                return False
            used.add((y, x))
            for a, b in directions:
                if bt(y + a, x + b, i + 1):
                    used.remove((y, x))
                    return True
            used.remove((y, x))
        used = set()
        for y in range(h):
            for x in range(w):
                if bt(y, x, 0):
                    return True
        return False
                