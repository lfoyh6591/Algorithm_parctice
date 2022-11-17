class Solution:
    def longest_odd(self, s, k):
        ret = ""
        l = min(k, len(s)-k-1)
        for i in range(l):
            if s[k-i-1] == s[k+i+1]:
                ret += s[k+i+1]
            else:
                return ret[::-1]+s[k]+ret
            
        return ret[::-1]+s[k]+ret
    
    def longest_even(self, s, k):
        ret = ""
        l = min(k, len(s)-k-2)
        for i in range(l):
            if s[k-i-1] == s[k+i+2]:
                ret += s[k+i+2]
            else:
                return ret[::-1]+s[k:k+2]+ret
            
        return ret[::-1]+s[k:k+2]+ret
    
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        ret = ""
        for i in range(len(s)):
            pal = self.longest_odd(s,i)
            if len(pal) > max_length:
                max_length = len(pal)
                ret = pal
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                pal = self.longest_even(s, i)
                if len(pal) > max_length:
                    max_length = len(pal)
                    ret = pal
                    
        return ret
                