class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        

        boxes = [set() for n in range(9)]
        rows = [set() for n in range(9)]
        cols = [set() for n in range(9)]

        for x in range(9):
            for y in range(9):
                p = board[x][y]
                if p == ".":
                    continue
                else:
                    box = (x // 3)*3 + y // 3
                    if p in boxes[box] or p in rows[x] or p in cols[y]:
                        return False
                    else:
                        boxes[box].add(p)
                        rows[x].add(p)
                        cols[y].add(p)
        
        return True
                    