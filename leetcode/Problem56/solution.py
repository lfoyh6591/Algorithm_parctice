class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ret = []
        line = [0]*10003
        reserve = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            line[start+1] += 1
            line[end+1] -= 1
            if start == end:
                reserve.append(start)
        reserve = list(set(reserve))
        reserve.sort()
        start = 0
        for i, v in enumerate(line[1:]):
            line[i] += line[i-1]
            if line[i] != 0:
                if line[i-1] == 0:
                    start = i

            if line[i] == 0:
                if line[i-1] != 0:
                    while reserve and (reserve[0] <= (i-1)):
                        if reserve[0] < (start - 1):
                            ret.append([reserve[0], reserve[0]])
                        del reserve[0]

                    ret.append([start-1, i-1])
            
        for r in reserve:
            ret.append([r, r])
                    
        return ret