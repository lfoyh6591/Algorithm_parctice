class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n >= 1) and (1162261467 % n == 0)