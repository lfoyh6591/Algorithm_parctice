class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        count = [True] * n
        count[0] = False
        count[1] = False
        
        for i in range(2, int(n**(1/2)) + 1):
            if count[i]:
                for j in range(i*i, n, i):
                    count[j] = False

        return sum(count)