### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = 0
    dicts = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four'
            ,5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

    for i in dicts:
        s = s.replace(dicts[i], str(i))
        
    answer = int(s)
    return answer
