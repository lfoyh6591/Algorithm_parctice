class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        check = [[False]*n for i in range(n)]
        check[0][0] = True
        lists = [[[s[0]]]]
        for i in range(1, n):
            check[i][i] = True
            l = []
            for r in lists[-1]:
                l.append(r + [s[i]])
            for j in range(0, i):
                if s[i] == s[j]:
                    if i-j == 1:
                        check[j][i] = True
                        if j>0:
                            for r in lists[j-1]:
                                l.append(r + [s[j:i+1]])
                        else:
                            l.append([s[0:2]])
                    else:
                        if check[j+1][i-1]:
                            check[j][i] = True
                            if j > 0:
                                for r in lists[j-1]:
                                    l.append(r + [s[j:i+1]])
                            if j == 0:
                                l.append([s[:i+1]])
            lists.append(l)

        return lists[-1]