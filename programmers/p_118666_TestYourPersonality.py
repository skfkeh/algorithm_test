### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
def solution(survey, choices):
    answer = ''
    dicts = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        dicts[survey[i][0]] += 4 - choices[i]
    
    answer += 'R' if dicts['R'] >= dicts['T'] else 'T'
    answer += 'C' if dicts['C'] >= dicts['F'] else 'F'
    answer += 'J' if dicts['J'] >= dicts['M'] else 'M'
    answer += 'A' if dicts['A'] >= dicts['N'] else 'N'
    
    return answer
