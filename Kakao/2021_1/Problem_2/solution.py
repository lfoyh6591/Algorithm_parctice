def combinations(order, num):
    if num == 1:
        return list(order)
    
    l = len(order)
    ret = []
    for i in range(l-num+1):
        l2 = combinations(order[i+1:], num-1)
        for j in l2:
            ret.append(order[i]+j)
    
    return ret

def solution(orders, course):
    patterns = []
    answer = []
    for num in course:
        s = set()
        mostset = []
        maxnum = 0        
        for order in orders:
            l = combinations("".join(sorted(order)), num)
            patterns.append(l)
            s = s | set(l)

        for meal in s:
            num = 0
            for pattern in patterns:
                if meal in pattern:
                    num += 1
            if num < 2:
                continue
                
            if num > maxnum:
                mostset = [meal]
                maxnum = num
            elif num == maxnum:
                mostset.append(meal)
            
        answer += mostset
    return sorted(answer)   
        