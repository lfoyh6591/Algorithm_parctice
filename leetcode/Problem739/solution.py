class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        res = [0]*length
        dic = {}
        for i in range(length-1):
            if temperatures[i] < temperatures[i+1]:
                res[i] = 1
                del_list = []
                for key in dic.keys():
                    if key < temperatures[i+1]:
                        del_list.append(key)
                        for index in dic[key]:
                            res[index] = i+1-index
                
                for key in del_list:
                    del dic[key]
                
                        
            else:
                if temperatures[i] in dic.keys():
                    dic[temperatures[i]] += [i]
                else:
                    dic[temperatures[i]] = [i]
                    
                
        return res