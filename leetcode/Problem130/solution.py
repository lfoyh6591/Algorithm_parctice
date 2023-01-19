class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.check = [[False]*len(board[0]) for i in range(len(board))]
        m, n = len(board), len(board[0])
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if (not self.check[i][j]) and (board[i][j] == "O"):
                    l = [(i, j)]
                    q = [(i, j)]
                    state = 0
                    while q:
                        x, y = q.pop(0)
                        self.check[x][y] = True
                        for x_m, y_m in moves:
                            new_x = x+x_m
                            new_y = y+y_m
                            if (new_x < 0) or (new_x >= m) or (new_y < 0) or (new_y >= n):
                                state = 1
                                continue
                            if (board[new_x][new_y] == "O") and (not self.check[new_x][new_y]):
                                q.append((new_x, new_y))
                                l.append((new_x, new_y))
                                self.check[new_x][new_y] = True
                    if not state:
                        for x, y in l:
                            board[x][y] = "X"
        
        return