def cal_fee(fee, t):
    if t <= fee[0]:
        return fee[1]
    else:
        if ((t-fee[0]) % fee[2]) == 0:
            state = 0
        else:
            state = 1
        
        return fee[1] + (((t-fee[0]) // fee[2]) + state) * fee[3]
    
def to_minute(t):
    return int(t[:2])*60 + int(t[3:5])

def parsing(s):
    return to_minute(s), s[6:10], True if s[11:] == "IN" else False


def solution(fees, records):
    dic_intime = {}
    dic_totaltime = {}
    for record in records:
        minute, num, is_in = parsing(record)
        if is_in:
            dic_intime[num] = minute
        else:
            dic_totaltime[num] = dic_totaltime.get(num, 0) + (minute - dic_intime[num])
            del(dic_intime[num])
    
    m = to_minute("23:59")
    for num in dic_intime.keys():
        dic_totaltime[num] = dic_totaltime.get(num, 0) + (m - dic_intime[num])
    
    ret = []
    for i in sorted(dic_totaltime.keys()):
        ret.append(cal_fee(fees, dic_totaltime[i]))
    
    return ret