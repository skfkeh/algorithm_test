### baekjoon
# https://www.acmicpc.net/problem/10815
import sys
input = sys.stdin.readline
n = int(input())
nlist = set(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

for i in range(len(mlist)):
    print(1, end=' ') if mlist[i] in nlist else print(0, end=' ')
