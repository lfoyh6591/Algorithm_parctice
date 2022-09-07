import sys
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n)]
        dist = [sys.maxsize for i in range(n)]
        heap = []
        for time in times:
            graph[time[0]-1].append((time[2], time[1]-1))

        heap.append((0, k-1))
        dist[k-1] = 0
        
        while heap:
            cost, here = heappop(heap)
            
            if dist[here] < cost:
                continue
            
            for newcost, there in graph[here]:
                newcost += cost
                if dist[there] > newcost:
                    dist[there] = newcost
                    heappush(heap, (newcost, there))
                
        ret = max(dist)
        if ret == sys.maxsize:
            return -1
        
        return ret