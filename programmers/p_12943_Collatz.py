### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    answer = 0
    while num != 1:
        if answer >= 500:
            answer = -1
            break
        answer += 1
        num = num//2 if num % 2 == 0 else num*3+1
    return answer
