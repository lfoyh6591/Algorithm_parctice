class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        gas += gas
        cost += cost
        diff = []
        
        for i in range(2*n):
            diff.append(gas[i] - cost[i])
        
        idx = 0
        for i in range(2*n):
            if diff[idx] >= 0:
                break
            idx += 1

        cal = 0
        cnt = 0
        while idx < 2*n:
            cal += diff[idx]
            idx += 1
            cnt += 1
            if cal < 0:
                cal = 0
                cnt = 0
            if cnt == n:
                return idx - n
        
        return -1