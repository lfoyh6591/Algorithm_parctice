class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powerof2 = []
        dic = {}
        for i in range(31):
            powerof2.append(2**i)

        for i in range(31):
            s = str(powerof2[i])
            l = ""
            for i in range(10):
                l += str(i)
                l += str(s.count(str(i)))
            
            occ = dic.get(len(s), [])
            occ.append(l)
            dic[len(s)] = occ

        n = str(n)
        l = ""
        for i in range(10):
            l += str(i)
            l += str(n.count(str(i)))
        
        occ = dic[len(str(n))]
        if l in occ:
            return True
        else:
            return False