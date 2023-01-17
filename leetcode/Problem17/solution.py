class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.dic = {"2" : ["a", "b", "c"], "3" : ["d", "e", "f"], "4" : ["g", "h", "i"], "5" : ["j", "k", "l"], "6" : ["m", "n", "o"], "7" : ["p", "q", "r", "s"], "8" : ["t", "u", "v"], "9" : ["w", "x", "y", "z"]}    

        if not digits:
            return []
            
        if len(digits) == 1:
            return self.dic[digits]
        
        letters = self.dic[digits[0]]
        ret = []
        for l in letters:
            ret += [l+c for c in self.letterCombinations(digits[1:])]
        
        return ret