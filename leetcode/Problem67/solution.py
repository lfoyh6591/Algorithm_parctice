class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        
        carry = 0
        a = a[::-1]
        b = b[::-1]
        
        res_len = max(len(a), len(b))+1
        res = [0]*res_len
        
        for i in range(res_len):
            if len(a) <= i:
                bi_a = 0
            else:
                bi_a = int(a[i])
            if len(b) <= i:
                bi_b = 0
            else:
                bi_b = int(b[i])
                
            s = carry + bi_a + bi_b
            carry = s//2
            res[i] = s%2
            
        ret = ""
        state = 0
        for i in range(res_len-1, -1, -1):
            if state == 0:
                if res[i] == 0:
                    continue
                elif res[i] == 1:
                    state = 1
            
            ret = ret + str(res[i])
            
        return ret