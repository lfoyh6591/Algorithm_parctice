class Solution:
    def rec(self, n, length, lists):
        if n<0:
            return []

        if n == 0:
            if length == 0:
                return lists
            else:
                return []

        if length == 0:
            return []

        ret = []
        ret += self.rec(n-1, length-1, [[1]] if not lists else [l+[1] for l in lists])
        ret += self.rec(n-2, length-1, [[2]] if not lists else [l+[2] for l in lists])
        ret += self.rec(n-3, length-1, [[3]] if not lists else [l+[3] for l in lists])
        return ret

    def restoreIpAddresses(self, s: str) -> list[str]:
        lengths = self.rec(len(s), 4, [])
        memos = []
        for length in lengths:
            cur = []
            idx = 0
            for l in length:
                if s[idx] == "0":
                    if l != 1:
                        break
                
                if int(s[idx:idx+l]) > 255:
                    break
                cur.append(s[idx:idx+l])
                idx = idx+l
            memos.append(cur)
        ret = []
        for memo in memos:
            if len(memo) == 4:
                ret.append(".".join(memo))
        
        return ret