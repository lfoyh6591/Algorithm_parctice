class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ret = [[1]]
        for i in range(numRows-1):
            l = []
            cur = 0
            last = ret[-1]
            for j in last:
                l.append(cur + j)
                cur = j
            l.append(1)
            ret.append(l)

        return ret