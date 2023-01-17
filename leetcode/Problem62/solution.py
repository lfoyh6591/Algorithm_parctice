class Solution:
    def rec(self, m, n):
        if self.memo[m][n] != -1:
            return self.memo[m][n]

        if (m == 0) and (n == 0):
            self.memo[0][0] = 0
            return 0
        if (m == 0) or (n == 0):
            self.memo[m][n] = 1
            return 1
        
        self.memo[m][n] = self.rec(m-1, n) + self.rec(m, n-1)
        return self.memo[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        if (m==1) and (n==1):
            return 1
        self.memo = [[-1]*n for i in range(m)]
        return self.rec(m-1, n-1)