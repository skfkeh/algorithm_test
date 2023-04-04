### BAEKJOON
# https://www.acmicpc.net/problem/1026
n = int(input())
a = input()
b = input()

alist = a.split()
aalist = list(map(int, alist))
aalist.sort(reverse = True)

blist = b.split()
bblist = list(map(int, blist))
bblist.sort()

total = 0

for i in range(n):
    total += aalist[i]*bblist[i]
    
print(total)