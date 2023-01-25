class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        bit = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]%10 == 0:
                    cnt = 0
                    for n_x, n_y in neighbors:
                        if ((n_x+i) < 0) or ((n_x+i)>=m) or ((n_y+j) < 0) or ((n_y+j) >= n):
                            continue
                        if board[n_x+i][n_y+j]%10:
                            cnt += 1
                    if cnt == 3:
                        board[i][j] = 10
                else:
                    cnt = 0
                    for n_x, n_y in neighbors:
                        if ((n_x+i) < 0) or ((n_x+i)>=m) or ((n_y+j) < 0) or ((n_y+j) >= n):
                            continue
                        if board[n_x+i][n_y+j]%10:
                            cnt += 1
                    if (cnt == 2) or (cnt == 3):
                        board[i][j] = 11

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]//10