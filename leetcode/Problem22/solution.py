class Solution:
    def rec(self, n, open_p, dic, lists):
        if n==0 : 
            return lists

        ret1 = []
        ret2 = []

        if (open_p == 0):
            dic["("] -= 1
            lists = [s+"(" for s in lists]
            open_p += 1
        
            if dic["("] > 0:
                dic["("] -= 1
                lists1 = [s+"(" for s in lists]
                ret1 = self.rec(n, open_p+1, dic, lists1)
                dic["("] += 1
                
            if dic[")"] > 0:
                dic[")"] -= 1
                lists2 = [s+")" for s in lists]
                ret2 = self.rec(n-1, open_p-1, dic, lists2)
                dic[")"] += 1
            dic["("] += 1
        else:
            if dic["("] > 0:
                dic["("] -= 1
                lists1 = [s+"(" for s in lists]
                ret1 = self.rec(n, open_p+1, dic, lists1)
                dic["("] += 1
                
            if dic[")"] > 0:
                dic[")"] -= 1
                lists2 = [s+")" for s in lists]
                ret2 = self.rec(n-1, open_p-1, dic, lists2)
                dic[")"] += 1

        return ret1 + ret2

    def generateParenthesis(self, n: int) -> list[str]:
        dic = {"(" : n, ")" : n}
        return self.rec(n, 0, dic, [""])