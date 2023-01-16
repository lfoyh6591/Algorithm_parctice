class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0) or (x == 1):
            return x

        start = 0
        end = x//2 + 1
        
        while end >= start:
            n = (start+end) // 2
            if (n**2 <= x) and ((n+1)**2 > x):
                return n

            if n**2 > x:
                end = n
            elif n**2 < x:
                start = n