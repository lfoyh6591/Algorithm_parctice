class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        if not nums:
            if lower==upper:
                return [str(lower)]
            else:
                return [str(lower)+"->"+str(upper)]
        l = []
        for num in nums:
            l.append((lower, num-1))
            lower = num+1
        
        l.append((nums[-1]+1, upper))

        ret = []
        for start, end in l:
            if start > end:
                continue
            if start == end:
                ret.append(str(start))
            else:
                ret.append(str(start)+"->"+str(end))
        
        return ret