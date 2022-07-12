#using sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        dic, res, pl, sl = {}, [], len(p), len(s)
        
        if pl > sl:
            return []
        
        for c in p:
            dic[c] = dic.get(c, 0) + 1            
        
        for i in range(pl):
            dic[s[i]] = dic.get(s[i], 0) - 1
            
        if all(v == 0 for v in dic.values()):
            res.append(0)            

        for i in range(pl, sl):
            dic[s[i]] = dic.get(s[i], 0) - 1
            dic[s[i-pl]] = dic.get(s[i-pl], 0) + 1
        
            if all(v == 0 for v in dic.values()):
                res.append(i-pl+1)                        
                    
        return res