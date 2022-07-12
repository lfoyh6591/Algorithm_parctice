def max_time(head, tree, informTime):
    max_t = 0
    if informTime[head] == 0:
        return 0
    
    else:
        for i in range(len(tree[head])):
            t = max_time(tree[head][i], tree, informTime)
            if max_t < t:
                max_t = t
                
        return informTime[head] + max_t

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        tr = [-1]*n
        for i in range(n):
            if manager[i] == -1:
                continue
                
            if tr[manager[i]] == -1:
                tr[manager[i]] = [i]
            else:
                tr[manager[i]].append(i)
        
        return max_time(headID, tr, informTime)