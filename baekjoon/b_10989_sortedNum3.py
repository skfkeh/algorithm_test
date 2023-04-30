### baekjoon
# https://www.acmicpc.net/problem/10989
# list에서 sorted 처리하는 대신
# 10000 이하의 숫자 counting 하는 방식으로 전환
# 메모리 이슈로 sys.stdin.readline 선언필요
import sys
input = sys.stdin.readline
num = int(input())
arr = [0]*10000

for i in range(num):
    a = int(input())
    arr[a-1] += 1
    
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
