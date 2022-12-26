class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        n = len(scores)
        l = []
        player = []
        
        for i in range(n):
            l.append((ages[i], scores[i]))
        l.sort()
        
        prefix = [0]*(n+1)

        for i in range(n):
            age, score = l[i]
            temp = 0
            for j in range(i):
                if (l[j][0] == age) or (l[j][1] <= score):
                    temp = max(temp, prefix[j+1])
            
            prefix[i+1] = temp+score

        return max(prefix)