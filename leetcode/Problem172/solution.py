class Solution:
    def trailingZeroes(self, n: int) -> int:
        l = []
        idx = 1
        while 5**idx <= n:
            l.append(5**idx)
            idx += 1

        ret = 0
        for i in range(len(l)):
            ret += (n//l[i])
        
        return ret