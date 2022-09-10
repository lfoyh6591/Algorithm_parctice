def split(s):
    left = 0
    right = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1
            
        if left == right:
            return s[:i+1], s[i+1:]
    
    return s, ""
    
def is_right(s):
    l = []
    for c in s:
        if c == '(':
            l.append(c)
        elif c == ')':
            if len(l) == 0:
                return False
            if l[-1] == '(':
                l.pop()
    
    return True if len(l) == 0 else False

def flip(s):
    ret = ''
    for c in s:
        if c == '(':
            ret += ')'
        else:
            ret += '('
    return ret
        
def recursion(p):
    answer = ''
    if p == '':
        return ''
    
    u, v = split(p)
    if is_right(u):
        answer += u
    else:
        return answer + '(' + recursion(v) + ')' +  flip(u[1:-1])

    return answer + recursion(v)
    
def solution(p):
    if is_right(p):
        return p
    
    return recursion(p)
