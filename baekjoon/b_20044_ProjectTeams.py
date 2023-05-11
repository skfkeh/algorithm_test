### baekjoon
# https://www.acmicpc.net/problem/20044
n = int(input())
slist = sorted(list(map(int, input().split())))

total = [0]*n

for i in range(n):
    total[i] += slist.pop()
    total[i] += slist.pop(0)
    
print(min(total))
