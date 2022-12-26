def to_binary(n):
    l = []
    while n > 0:
        if n % 2 == 0:
            l.append(0)
        else:
            l.append(1)
        n = n//2
    return l

def binary_mul_cal(x, n):
    l = [x]
    for i in range(n):
        l.append(l[-1]**2)
    return l

def binary_div_cal(x, n):
    l = [1/x]
    for i in range(n):
        l.append(l[-1]**2)
    return l

class Solution:
    def myPow(self, x: float, n: int) -> float:
        binary = to_binary(abs(n))
        ans = 1.0

        if n > 0:
            cal = binary_mul_cal(x, len(binary))
        else:
            cal = binary_div_cal(x, len(binary))

        for i in range(len(binary)):
            if binary[i] == 1:
                ans*=cal[i]

        return ans