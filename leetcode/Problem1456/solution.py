class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = 0
        end = k-1
        cnt = 0
        for i in range(0, k):
            if s[i] in vowels:
                cnt += 1

        max_cnt = cnt
        while end < len(s)-1:
            if s[start] in vowels:
                cnt -= 1
            start += 1
            end += 1
            if s[end] in vowels:
                cnt += 1
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt