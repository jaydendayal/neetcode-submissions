class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(cells):
            digits = [c for c in cells if c != '.']
            return len(digits) != len(set(digits))
        for row in board:
                if has_duplicates(row):
                    return False
        for col in zip(*board):
                if has_duplicates(col):
                    return False
        for bRow in range (0,9,3):
            for bCol in range(0,9,3):
                box = []
                for r in range(bRow, bRow + 3):
                    for c in range(bCol, bCol +3):
                        box.append(board[r][c])
                if has_duplicates(box):
                    return False
        return True