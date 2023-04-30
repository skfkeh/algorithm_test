### BAEKJOON
# https://www.acmicpc.net/problem/1459
import math
x, y, w, s = map(int, input().split())

print(f"w*2:{w*2}, s*math.sqrt(2):{s*math.sqrt(2)}")

if w*2 >= s:  ## 대각선으로 가는게 이득일 때
    if w > s:
        if (x+y)%2 != 0:
            print("cc11") 
            across = max(x, y) * (s-1)
            move = abs(x-y)
        else:
            print("cc22")
            across = max(x, y) * s
            move = 0
    else:
        across = min(x, y) * s
        move = abs(x-y)*w
        print(f"acorss:{across}, move:{move}")
    print(move + across)
else:        ## 길따라 가는게 이득일 때
    print("bbbb")
    move = (x+y)*w
    print((x+y)*w)