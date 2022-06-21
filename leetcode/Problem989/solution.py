class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        s_k = str(k)
        output = [0]*(max(len(num), len(s_k))+1)
        carry = 0
        num = num[::-1]
        for i in range(len(output)):
            if i >= len(s_k):
                temp_k = 0
            else:
                temp_k = int(s_k[-1-i])

            if i >= len(num):
                temp_n = 0
            else:
                temp_n = num[i]
                
            temp = (temp_k + temp_n + carry)
            output[i] = temp%10
            carry = temp//10
            
        if output[-1] == 0:
            output.pop()
            
        return output[::-1]