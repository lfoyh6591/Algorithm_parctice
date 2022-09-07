import sys
class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        graph = [[] for i in range(n)]
        dists = [[sys.maxsize]*n for i in range(n)]
        
        for i in range(n):
            dists[i][i] = 0
            
        for edge in edges:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
            dists[edge[0]][edge[1]] = edge[2]
            dists[edge[1]][edge[0]] = edge[2]
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dists[i][j] = min(dists[i][j], dists[i][k]+dists[k][j])
        print(dists)
        minnum = (sys.maxsize, -1)
        for i, dist in enumerate(dists):
            num = 0
            for d in dist:
                if d <= distanceThreshold:
                    num += 1
            
            if minnum[0] >= num:
                minnum = (num, i)
                
        return minnum[1]