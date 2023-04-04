### BAEKJOON
# https://www.acmicpc.net/problem/13627
n, m = map(int, input().split())
who = input()

survived = who.split()
survived.sort()
dead = []

for i in range(1, n+1):
    if str(i) in survived:
        pass
    else:
        dead.append(i)

if len(dead) == 0:
    print("*")
else:
    for i in dead:
        print(i, end=" ")