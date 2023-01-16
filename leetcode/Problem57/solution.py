class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        starts = [i[0] for i in intervals]
        ends = [i[1] for i in intervals]

        state = 0
        prev = -1
        for i in range(len(starts)):
            if (newInterval[0] > prev) and (newInterval[0] <= starts[i]):
                starts.insert(i, newInterval[0])
                state = 1
                break
        if state == 0:
            starts.append(newInterval[0])
        
        prev = -1
        state = 0
        for i in range(len(ends)):
            if (newInterval[1] > prev) and (newInterval[1] <= ends[i]):
                ends.insert(i, newInterval[1])
                state = 1
                break

        if state == 0:
            ends.append(newInterval[1])

        cur = 0
        
        idx1 = 0
        idx2 = 0
        l = []
        ret = []
        print(starts)
        print(ends)
        while (idx1 < len(starts)) or (idx2 < len(ends)):
            if idx1 == len(starts):
                l.append(ends[-1])
                ret.append(l)
                break
            
            if starts[idx1] <= ends[idx2]:
                if cur == 0:
                    l.append(starts[idx1])
                cur += 1
                idx1 += 1
            else:
                if cur == 1:
                    l.append(ends[idx2])
                    ret.append(l)
                    l = []
                cur -= 1
                idx2 += 1

        return ret