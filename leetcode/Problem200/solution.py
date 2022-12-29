class Solution:
    def check_island(self, x, y, grid, state):
        if state[x][y] or grid[x][y] == "0":
            return 0

        if grid[x][y] == "1":
            state[x][y] = True

        d_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in d_list:
            new_x = x + d[0]
            new_y = y + d[1]
            if (new_x < 0) or (new_x >= len(grid)) or (new_y < 0) or (new_y >= len(grid[0])):
                continue
            self.check_island(new_x, new_y, grid, state)

        return 1


    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        state = [[False] * n for i in range(m)]
        island_num = 0

        for i in range(m):
            for j in range(n):
                if state[i][j] or (grid[i][j] == "0"):
                    continue
                island_num += self.check_island(i, j, grid, state)  

        return island_num  