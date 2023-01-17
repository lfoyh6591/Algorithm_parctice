class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num0 = s.count("0")
        num1 = s.count("1")
        cur1 = 0
        cur0 = 0
        min_flip = 100000
        for i, c in enumerate(s):
            if c == "1":
                min_flip = min(min_flip, cur1 + num0 - cur0)
                cur1 += 1
                if cur1 == num1:
                    min_flip = min(min_flip, num1)
            else:
                cur0 += 1
        
        return min_flip