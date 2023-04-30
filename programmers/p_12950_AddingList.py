### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = [[x + y for x, y in zip(inlist1, inlist2)] for inlist1, inlist2 in zip(arr1, arr2)]
    return answer
