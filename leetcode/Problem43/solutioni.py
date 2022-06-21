def add_str(num1, num2):
    length = max(len(num1), len(num2))
    res = ""
    carry = 0
    for i in range(length):
        a = int(num1[-1-i]) if len(num1)>i else 0
        b = int(num2[-1-i]) if len(num2)>i else 0
        sum = a + b + carry
        res = str(sum%10) + res
        carry = 1 if sum>9 else 0

    if carry == 1:
        res = "1" + res
    return res

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dp = [-1] * 10
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = "0"
        for i in range(len(num1)):
            a = int(num1[-1-i])
            
            if dp[a] != -1:
                res = add_str(res, dp[a] + "0"*i)
            else:
                mul = "0"
                for j in range(len(num2)):
                    temp = str(int(a) * int(num2[-1-j])) + "0"*j
                    mul = add_str(mul, temp)
                dp[a] = mul
                res = add_str(res, dp[a] + "0"*i)
                
        return res