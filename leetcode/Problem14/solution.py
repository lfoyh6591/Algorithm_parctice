class Solution:
    def prefix_matching(self, s1, s2):
        ret = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                ret += s1[i]
            else:
                return ret
        
        return ret

    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            prefix = self.prefix_matching(prefix, s)
            if len(prefix) == 0:
                return ""
                
        return prefix