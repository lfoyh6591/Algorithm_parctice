def to_k(n, k):    
    ret = ""
    while n != 0:
        ret = str(n%k) + ret
        n //= k
    
    return ret
        
def is_prime(n):
    if n == 1:
        return False
    if (n == 2) or (n == 3):
        return True
    
    i = 2
    while True:
        if i**2 > n:
            return True
        if n%i == 0:
            return False
        i+=1

def solution(n, k):
    s = to_k(n, k)
    l = s.split("0")
    count = 0
    for i in l:
        if (len(i) > 0) and (is_prime(int(i))):
            count += 1
    
    return count