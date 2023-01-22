class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        p = numerator // denominator
        q = numerator % denominator 
        dic = {}

        if not q:
            return str(p)

        if p < 0:
            q = denominator - q
            ret = "-" + str(abs(p)-1) + "."
        else:
            ret = str(p) + "."        
        
        idx = len(ret)
        while True:
            if not q:
                return ret
            if dic.get(q, -1) != -1:
                ret = ret[:dic[q]] + "(" + ret[dic[q]:] + ")"
                return ret
            dic[q] = idx
            q *= 10
            ret += str(q//denominator)
            q %= denominator
            idx += 1

        return ret
