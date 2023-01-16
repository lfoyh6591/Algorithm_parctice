class Solution:
    def compare(self, l1, l2):
        if len(l1) > len(l2):
            return True
        elif len(l2) > len(l1):
            return False

        for i in range(len(l1)):
            if l1[i] > l2[i]:
                return True
            elif l2[i] > l1[i]:
                return False

        return True

    def max_int(self, sign):
        n = 2**31
        l = []
        while n != 0:
            l.append(n%10)
            n//=10

        if sign == 0:
            l[0] = l[0] - 1

        return l[::-1]

    def myAtoi(self, s: str) -> int:
        l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        s = s.strip()
        if len(s) == 0:
            return 0

        sign = 1 if s[0] == "-" else 0
        if (s[0] == "-") or (s[0] == "+"):
            st = 1
        else:
            st = 0

        start = st
        for i, c in enumerate(s[st:]):
            if c == "0":
                start = st+i+1
            else:
                break
        x = []
        state = True
        for c in s[start:]:
            if c not in l:
                break
            x.append(int(c))
            state = False
        if state:
            return 0

        max_x = self.max_int(sign)
        if self.compare(x, max_x):
            x = max_x
        ret = 0
        for idx, i in enumerate(x[::-1]):
            ret += i*(10**idx)

        if sign == 0:
            return ret
        else:
            return 0-ret