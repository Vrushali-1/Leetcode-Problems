class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =[set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    if board[r][c] in rows[r]:
                        return False
                    rows[r].add(board[r][c])
                    if board[r][c] in columns[c]:
                        return False
                    columns[c].add(board[r][c])
                    if board[r][c] in boxes[(r//3) * 3 + (c//3)]:
                        return False
                    boxes[(r//3) * 3 + (c//3)].add(board[r][c])
        return True
