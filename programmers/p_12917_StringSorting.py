### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    slist = list(s)
    slist.sort(reverse=True)
    slist = ('').join(slist)
    answer = slist
    return answer
