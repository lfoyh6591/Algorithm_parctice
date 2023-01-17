class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        check = [[0]*10 for i in range(27)]
        print(check)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    check[i][int(board[i][j])] += 1
                    check[j+9][int(board[i][j])] += 1
                    check[(j//3)+(i//3)*3+18][int(board[i][j])] += 1

        for i in range(27):
            for j in range(10):
                if check[i][j] > 1:
                    return False

        return True