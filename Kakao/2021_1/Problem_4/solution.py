import sys
def solution(n, s, a, b, fares):
    # graph = [[] for i in range(n)]
    dists = [[sys.maxsize]*n for i in range(n)]
    fee = sys.maxsize
    
    for i in range(n):
        dists[i][i] = 0
    
    for fare in fares:
        # graph[fare[0]-1].append((fare[2], fare[1]-1))
        # graph[fare[1]-1].append((fare[2], fare[0]-1))
        dists[fare[0]-1][fare[1]-1] = fare[2]
        dists[fare[1]-1][fare[0]-1] = fare[2]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dists[i][j] = min(dists[i][j], dists[i][k]+dists[k][j])
                
    for k in range(n):
        fee = min(fee, dists[s-1][k] + dists[k][a-1] + dists[k][b-1])
    
    return fee