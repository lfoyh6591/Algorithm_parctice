memo = [-1]*46
class Solution:
    def climbStairs(self, n: int) -> int:
        if memo[n] != -1:
            return memo[n]

        if n == 0:
            memo[0] = 0
            return 0
        if n == 1:
            memo[1] = 1
            return 1
        if n == 2:
            memo[2] = 2
            return 2

        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]