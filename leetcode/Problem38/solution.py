class Solution:
    def countAndSay(self, n: int) -> str:
        dic = {1: 1}
        if n == 1:
            return "1"
        s = "1"
        for i in range(n-1):
            new_s = ""
            cur = s[0]
            cnt = 0
            for j in range(len(s)):
                if s[j] == cur:
                    cnt += 1
                else:
                    new_s += str(cnt) + str(cur)
                    cur = s[j]
                    cnt = 1
            
            if cnt != 0:
                new_s += str(cnt) + str(cur)

            s = new_s
        return s