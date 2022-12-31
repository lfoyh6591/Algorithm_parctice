class Solution:
    def cut(self, pizza,prefix_sum, x, y, n, memo, mod):
        row = len(pizza)
        col = len(pizza[0])
        if n > ((row - x - 1) + (col - y - 1)):
            memo[n][x][y] = 0
            return 0

        if memo[n][x][y] != -1:
            return memo[n][x][y]

        if n == 0:
            if (prefix_sum[row][col] - prefix_sum[x][col] - prefix_sum[row][y] + prefix_sum[x][y]) > 0:
                memo[n][x][y] = 1
                return 1
            memo[n][x][y] = 0
            return 0

        ret = 0
        for i in range(x+1, row):
            if (prefix_sum[i][col] - prefix_sum[x][col] - prefix_sum[i][y] + prefix_sum[x][y]) != 0:
                if memo[n-1][i][y] == -1:
                    memo[n-1][i][y] = (self.cut(pizza, prefix_sum, i, y, n-1, memo, mod)%mod)
                ret += memo[n-1][i][y]
                ret %= mod

        for i in range(y+1, col):
            if (prefix_sum[row][i] - prefix_sum[x][i] - prefix_sum[row][y] + prefix_sum[x][y]) != 0:
                if memo[n-1][x][i] == -1:
                    memo[n-1][x][i] = (self.cut(pizza, prefix_sum, x, i, n-1, memo, mod)%mod)
                ret += memo[n-1][x][i]
                ret %= mod

        memo[n][x][y] = ret
        return ret


    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        row = len(pizza)
        col = len(pizza[0])
        prefix_sum = [[0] * (col+1) for i in range(row+1)]

        for i in range(row):
            pizza[i] = list(pizza[i])
        memo = [[[-1] * col for i in range(row)] for j in range(k)]
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + (1 if (pizza[i-1][j-1] == "A") else 0)
        
        return self.cut(pizza, prefix_sum, 0, 0, k-1, memo, mod)