def prepare_bylength(queries):
    dic = {}
    for query in queries:
        l = len(query)
        dic[l] = dic.get(l, []) + [query]
        
    return dic
    
def extract(word, isstart):
    if isstart == 1:
        for i in range(len(word)):
            if word[i] != '?':
                return word[i:]
    else:
        for i in range(len(word)):
            if word[i] == '?':
                return word[:i]

def compare(word, keyword, isstart):
    l = len(keyword)
    if isstart == 1:
        if word.endswith(keyword):
            return True
        else:
            return False
    
    elif isstart == 0:
        if word.startswith(keyword):
            return True
        else:
            return False

def solution(words, queries):
    answer = []
    words = prepare_bylength(words)
    start_dic = {}
    end_dic = {}
    for l in words.keys():
        start_dic[l] = {}
        end_dic[l] = {}

    for query in queries:
        l = len(query)
        if query[0] == '?':
            if query[-1] == '?':
                answer.append(len(words.get(l, [])))
                continue
            else:
                endwith = extract(query, 1)
                count = end_dic.get(l, {}).get(endwith, 0)
                
                if count != 0:
                    answer.append(count)
                    continue
                    
                for word in words.get(l, []):
                    if compare(word, endwith, 1):
                        count += 1
                end_dic[l] = end_dic.get(l, {})
                end_dic[l][endwith] = count
                answer.append(count)
                
        elif query[-1] == '?':
            startwith = extract(query, 0)
            count = start_dic.get(l, {}).get(startwith, 0)
                
            if count != 0:
                answer.append(count)
                continue

            for word in words.get(l, []):
                if compare(word, startwith, 0):
                    count += 1
            start_dic[l] = start_dic.get(l, {})
            start_dic[l][startwith] = count
            answer.append(count)
            
    return answer
            