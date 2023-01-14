class Solution:
    def comparison(self, l1, l2):
        for i in range(len(l1)):
            if l1[i] > l2[i]:
                return True
            elif l2[i] > l1[i]:
                return False
            
        return True

    def max_int(self) -> list:
        n = 2**30
        carry = 0
        l = []
        while n != 0:
            cal = (n%10) *2 + carry
            carry = cal // 10
            l.append(str(cal%10))
            n = n // 10
        return l[::-1]

    def reverse(self, x: int) -> int:
        sign = (x >= 0)
        x = abs(x)
        x_list = []
        if x == 0:
            return 0

        while x != 0:
            x_list.append(str(x%10))
            x = x // 10
        
        l = self.max_int()
        if sign:
            l[-1] = str(int(l[-1]) - 1)
        if len(x_list) < len(l):
            if sign:
                return int("".join((x_list)))
            else:
                return int("-"+"".join(x_list))
        elif len(x_list) > len(l):
            return 0
        else:
            if self.comparison(x_list, l):
                return 0
            else:
                if sign:
                    return int("".join(x_list))
                else:
                    return int("-"+"".join(x_list))