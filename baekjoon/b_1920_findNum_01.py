### BAEKJOON
# https://www.acmicpc.net/problem/1920
n = input()
nlist = set(map(int, input().split()))
m = input()
mlist = list(map(int, input().split()))

for i in mlist:
    print(0) if i not in nlist else print(1)
