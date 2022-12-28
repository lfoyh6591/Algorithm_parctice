def kadane(s, a, b):
    state_a = False
    state_b = False

    max_v = 0
    cur_v = 0
    freq_a = 0
    freq_b = 0
    first_b = False

    for i in range(len(s)):
        if s[i] == a:
            freq_a += 1
            state_a = True
        elif s[i] == b:
            if first_b:
                first_b = False
                freq_b -= 1
            
            freq_b += 1
            state_b = True
        else:
            continue

        if state_a and state_b:
            if (freq_a - freq_b) < 0:
                if s[i] == a:
                    freq_a = 1
                    freq_b = 0
                    state_b = False
                if s[i] == b:
                    freq_b = 1
                    freq_a = 0
                    state_a = False
                    first_b = True
            else:
                if ((freq_a - freq_b) == 0) and (s[i] == a):
                    first_b = True
                cur_v = freq_a - freq_b
                if max_v < cur_v:
                    max_v = cur_v

    if state_b == False:
        return max(max_v, freq_a - 1)

    return max_v

class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        max_v = 0

        set_s = list(set(s))
        set_n = len((set_s))


        for i in range(set_n):
            for j in range(set_n):
                if i == j:
                    continue
                cur_v = kadane(s, set_s[i], set_s[j])
                if max_v < cur_v:
                    max_v = cur_v

        return max_v