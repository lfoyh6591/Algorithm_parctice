class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        dic = {}
        
        for t in time:
            dic[t%60] = dic.get(t%60, 0) + 1
        
        ret = 0
        for key, value in dic.items():
            if (key == 0) or (key == 30):
                ret += (value)*(value-1)//2
            elif key < 30:
                ret += (dic[key] * dic.get((60-key), 0))
            
        return ret