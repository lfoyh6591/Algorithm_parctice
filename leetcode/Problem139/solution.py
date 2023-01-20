class Solution:
    def rec(self, s, wordDict):
        if not s:
            return True

        if self.memo[len(s)-1] != -1:
            return True if self.memo[len(s)-1] else False
        
        for word in wordDict:
            idx = s.find(word)
            
            if idx == 0:
                self.memo[len(s)-1] = 1 if self.rec(s[len(word):], wordDict) else 0
                if self.memo[len(s)-1]:
                    return True
        
        return False

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.memo = [-1]*len(s)
        return self.rec(s, wordDict)