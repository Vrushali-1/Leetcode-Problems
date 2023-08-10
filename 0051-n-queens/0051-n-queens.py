class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def createBoard(board):
            temp = []
            for i in range(n):
                temp.append("".join(board[i]))
            answer.append(temp)
        
        def backtrack(row,cols,diagonals,anti_diagonals,board):
            if row == n:
                createBoard(board)
                return
            
            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                board[row][col] = "Q"
                backtrack(row + 1,cols,diagonals,anti_diagonals,board)
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
                board[row][col] = "."
        
        answer = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0,set(),set(),set(),empty_board)
        return answer
