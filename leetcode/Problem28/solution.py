#using kmp
def get_pi(s):
    pi = [0]
    j=0
    for i in range(1, len(s)):
        j=pi[i-1]
        while True:
            if s[i] == s[j]:
                pi.append(j+1)
                break
            else:
                if j == 0:
                    pi.append(0)
                    break
                j = pi[j-1]
    
    return pi

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        pi = get_pi(needle)
        
        i=0
        j=0
        while True:
            if j == len(needle):
                return i-j
            if i == len(haystack):
                return -1
                            
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = pi[j-1]