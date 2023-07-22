### Baekjoon
# https://www.acmicpc.net/problem/1085
x, y, w, h = map(int, input().split())
## 6 2 10 3 -> w-x:4, h-y:1
if w-x>h-y:
    if h-y>x: print(y) if x>y else print(x)   # y와 경계 사이가 x까지보다 멀때
    elif h-y>y: print(y) if x>y else print(x) # y와 경계 사이가 y까지보다 멀때
    else: print(h-y)
else:
    if w-x>x: print(y) if x>y else print(x)   # x와 경계 사이가 x까지보다 멀때
    elif w-x>y: print(y) if x>y else print(x) # x와 경계 사이가 y까지보다 멀때
    else: print(w-x)
