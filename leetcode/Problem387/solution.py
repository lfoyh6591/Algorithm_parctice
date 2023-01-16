class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, c in enumerate(s):
            if dic.get(c, -2) == -2:
                dic[c] = i
            else:
                dic[c] = -1

        ret = 100000
        for key, value in dic.items():
            if value != -1:
                ret = min(ret, value)
        
        if ret == 100000:
            return -1
        return ret