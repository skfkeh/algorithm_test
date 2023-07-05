### BaekJoon
# https://www.acmicpc.net/problem/2622
from math import ceil

n = int(input())
cnt = 0

## 1번째 풀이
for x in range(1, n):
    for y in range(x, n):
        z = n - x - y
        if y <= z and x + y > z:
            cnt += 1
            
## 2번째 풀이
for x in range(ceil(n/3), ceil(n/2)):
    for y in range(ceil((n-x)/2), x+1):
        cnt += 1

## 3번째 풀이
for x in range(ceil(n/3), ceil(n/2)):
    cnt += x - ceil((n-x)/2) + 1

    
## 4번째 풀이
for x in range((n+1)//3, (n+1)//2):
    cnt += x - (n-x)//2 + 1

## 5번째 풀이
for x in range((n+1)//3, (n+1)//2):
    cnt += (3*x - n + 2)//2

## 6번째 풀이
cnt = sum([(3*x-n+2)//2 for x in range((n+1)//3, (n+1)//2)])
    
print(cnt)
