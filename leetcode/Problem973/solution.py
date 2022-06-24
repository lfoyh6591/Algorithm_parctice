def distance(x, y):
    return x*x + y*y

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        dic = {}
        for point in points:
            x = point[0]
            y = point[1]
            
            d = distance(x, y)
            if d in dic.keys():
                dic[d].append(point)
            else:
                dic[d] = [point]
                
        dic = dict(sorted(dic.items()))
        print(dic)
        ret = []
        
        for key in dic.keys():
            if len(ret) >= k:
                return ret
            ret += dic[key]
            
        return ret