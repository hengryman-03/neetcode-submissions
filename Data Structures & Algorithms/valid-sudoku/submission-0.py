from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)   # rows[r]      -> digits seen in row r
        cols = defaultdict(set)   # cols[c]      -> digits seen in column c
        boxes = defaultdict(set)  # boxes[(r//3, c//3)] -> digits seen in that box

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # skip empty cells

                box = (r // 3, c // 3)

                # If the digit was already seen in this row, column, or box -> invalid
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True