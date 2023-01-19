class Solution:
    def rec(self, idx, x, y, check, board, word):
        
        if idx == len(word):
            return True
        m = len(board)
        n = len(board[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x_m, y_m in moves:
            new_x = x+x_m
            new_y = y+y_m
            if (new_x < 0) or (new_x >= m) or (new_y < 0) or (new_y >= n):
                continue
            if check[new_x][new_y]:
                continue
            if board[new_x][new_y] == word[idx]:
                check[new_x][new_y] = True
                if self.rec(idx+1, new_x, new_y, check, board, word):
                    return True
                check[new_x][new_y] = False

        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        
        check = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    check[i][j] = True
                    if self.rec(1, i, j, check, board, word):
                        return True
                    check[i][j] = False                        
        
        return False