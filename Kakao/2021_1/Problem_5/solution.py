def to_second(time):
    return int(time[0:2])*3600 + int(time[3:5])*60 + int(time[6:])

def to_time(second):
    sec = second % 60
    minute = (second % 3600) // 60
    hour = second // 3600
    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    return hour + ':' + minute + ':' + sec

def solution(play_time, adv_time, logs):
    play_time = to_second(play_time)
    adv_time = to_second(adv_time)
    n = len(logs)
    boundary = []
    for log in logs:
        start = to_second(log[:8])
        end = to_second(log[9:])
        
        boundary.append((start, 1))
        boundary.append((end, 0))
    
    boundary = sorted(boundary)
    
    total = []
    overlap = 0
    current = 0
    for time, mark in boundary:
        total += [overlap] * (time - current)
        
        if mark == 1:
            overlap += 1
        else:
            overlap -= 1
        current = time
    
    total += [overlap] * (play_time - current)
    cal_time = 0
    for i in range(adv_time):
        cal_time += total[i]
    cal_time = [cal_time]
    
    for i in range(1, play_time - adv_time + 1):
        cal_time.append(cal_time[i-1] - total[i-1] + total[i-1+adv_time])
    
    max_time = 0
    ret = 0
    for i, time in enumerate(cal_time):
        if time > max_time:
            max_time = time
            ret = i
            
    return to_time(ret)