class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        
        for s in strs:
            key = "".join(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        
        print(dic)
        
        return dic.values()                        