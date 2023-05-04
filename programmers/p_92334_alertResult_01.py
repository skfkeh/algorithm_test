### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    user_dicts = {l:[] for l in id_list}
    stop_dicts = {s:0 for s in id_list}
    stop_user = []
    
    report = list(set(report))
    
    for i in report:
        x, y = list(i.split())
        user_dicts[x].append(y)
    
    for i in user_dicts:
        for j in user_dicts[i]:
            stop_dicts[j] += 1
    
    for i in stop_dicts:
        if stop_dicts[i] >= k:
            stop_user.append(i)
    
    for i, l in zip(range(len(user_dicts)), user_dicts):
        for j in user_dicts[l]:
            if j in stop_user:
                answer[i]+=1
    
    return answer
