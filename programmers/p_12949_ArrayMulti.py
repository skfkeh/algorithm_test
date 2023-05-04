### programmers
# https://school.programmers.co.kr/learn/courses/30/lessons/12949
import numpy as np
def solution(arr1, arr2):
    anum = np.array(arr1)
    bnum = np.array(arr2)

    ## 행렬곱 처리하기
    answer = anum.dot(bnum)
    
    ## numpy행렬을 list로 변경
    answer = answer.tolist()
    return answer
