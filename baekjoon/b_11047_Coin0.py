### Baekjoon
# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
klist = []
total = 0

for _ in range(n):
    tmp = int(input())
    klist.append(tmp)
klist.sort(reverse=True)

for i in klist:
    if i>k:
        continue
    total+=k//i
    k=k-(k//i)*i

print(total)
