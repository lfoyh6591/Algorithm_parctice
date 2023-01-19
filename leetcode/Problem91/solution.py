class Solution:
    def rec(self, s):
        if self.memo.get(s, -1) != -1:
            return self.memo[s]

        if len(s) == 0:
            return 0

        if s[0] == "0":
            return 0

        if len(s) == 1:
            self.memo[s] = 1
            return 1
        
        if len(s) == 2:
            if int(s) <= 26:
                if s[1] == "0":
                    self.memo[s] = 1
                else:
                    self.memo[s] = 2
                return self.memo[s]

        if int(s[:2]) <= 26:
            self.memo[s] = self.rec(s[1:]) + self.rec(s[2:])
        else:
            self.memo[s] = self.rec(s[1:])

        return self.memo[s]
        

    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.rec(s)