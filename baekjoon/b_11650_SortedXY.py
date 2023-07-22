### BaekJoon
# https://www.acmicpc.net/problem/11650
n = int(input())
xlist, ylist = [], []
for i in range(n):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
    
for y, x in sorted(zip(ylist, xlist)):
    print(x, y)
