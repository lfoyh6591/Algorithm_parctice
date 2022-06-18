def find_div(n):
    l = []
    for i in range(1, (n+1)//2+1):
        if n%i == 0:
            l.append(i)
            l.append(n//i)
    
    l.remove(n)
    return l
            
def is_pattern(s, p, n):
    if s == p*n:
        return True
    else:
        return False
    
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        divisor = find_div(len(s))
                
        for d in divisor:
            if is_pattern(s, s[0:d], len(s)//d) == True:
                return True
            
        return False
            
            