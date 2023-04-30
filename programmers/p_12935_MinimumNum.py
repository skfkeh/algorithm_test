### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    tmp = min(arr)
    arr.remove(tmp)
    answer = [-1] if len(arr) == 0 else arr
    return answer
