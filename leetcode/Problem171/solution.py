class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = {}
        for i in range(26):
            dic[str(chr(i+65))] = i+1
        
        idx = 0
        ret = 0
        for c in columnTitle[::-1]:
            ret += dic[c]*(26**idx)
            idx += 1

        return ret