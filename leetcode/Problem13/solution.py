class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        roman = list(s)
        state = [1]*len(roman)
        for i in range(0, len(roman)-1):
            if dic[roman[i]] < dic[roman[i+1]]:
                state[i] = -1

        ans = 0
        for i in range(len(roman)):
            ans += dic[roman[i]]*state[i]

        return ans