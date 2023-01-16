import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p = re.compile('[a-z0-9]')
        l = p.findall(s)
        
        start = 0
        end = len(l) - 1
        while end > start:
            if l[end] != l[start]:
                return False
            end -= 1
            start += 1
        
        return True