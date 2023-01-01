import heapq
class Solution:
    def racecar(self, target: int) -> int:
        dic = {}
        p = {}
        cur = 1
        cnt = 1
        state = {}
        while cur < 10001:
            dic[cur] = cnt
            p[cur] = "A"*cnt
            cur += 2**cnt
            cnt += 1
        heap = []
        for k, v in dic.items():
            heapq.heappush(heap, (v, k, 1, p[k]))
        
        while heapq:
            value, key, cur_speed, pr = heapq.heappop(heap)
            if key == target:
                return value
            if cur_speed in state.get(key, []):
                continue
                
            l = state.get(key, [])
            l.append(cur_speed)
            state[key] = l

            if pr[-2:]!="RR":
                if cur_speed > 0:
                    heapq.heappush(heap, (value+1, key, -0.5, pr+"R"))
                elif cur_speed < 0:
                    heapq.heappush(heap, (value+1, key, 0.5, pr+"R"))

            for k, v in dic.items():
                if cur_speed == 0.5 :
                    heapq.heappush(heap, (value+v, key+k, 1, pr+p[k]))
                elif cur_speed == -0.5 :
                    heapq.heappush(heap, (value+v, key-k, -1, pr+p[k]))
        return 0