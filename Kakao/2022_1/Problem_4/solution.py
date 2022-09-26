import copy

def cal(n, ryan, apeach, state, ryan_score, apeach_score):
    score_diff = ryan_score - apeach_score
    if n == 0:
        # print("!", n, ryan, apeach, state, ryan_score, apeach_score)
        if score_diff > 0:
            return score_diff, copy.deepcopy(ryan)
        else:
            return score_diff, [-1]
    else:    
        if state == 10:
            # print("@", n, ryan, apeach, state, ryan_score, apeach_score)
            temp = ryan[10]
            ryan[10] = n
            score_diff, r = cal(0, ryan, apeach, state, ryan_score, apeach_score)
            ryan[10] = temp
            return score_diff, r

        else:
            if n > apeach[state]:
                temp = ryan[state]
                # print("#", n, ryan, apeach, state, ryan_score, apeach_score)
                diff1, r1 = cal(n, ryan, apeach, state+1, ryan_score, apeach_score)
                ryan[state] = apeach[state] + 1
                ryan_score += (10-state)
                if apeach[state] != 0:
                    apeach_score -= (10-state)
                diff2, r2 = cal(n-ryan[state], ryan, apeach, state+1, ryan_score, apeach_score)
                ryan[state] = temp
                if diff1 > diff2:
                    return diff1, r1
                elif diff2 > diff1:
                    return diff2, r2
                else:
                    if diff1 <= 0:
                        return diff1, [-1]
                    for i in range(0, 11):
                        if r1[10-i] > r2[10-i]:
                            return diff1, r1
                        elif r2[10-i] > r1[10-i]:
                            return diff2, r2
                        else:
                            continue

            else:
                # print("$", n, ryan, apeach, state, ryan_score, apeach_score)
                return cal(n, ryan, apeach, state+1, ryan_score, apeach_score)

def solution(n, info):
    ryan = [0 for i in range(11)]
    apeach_score = 0
    for i in range(11):
        if info[i] != 0:
            apeach_score += (10-i)
            
    diff, r = cal(n, ryan, info, 0, 0, apeach_score)
    # print(diff, r)
    return r