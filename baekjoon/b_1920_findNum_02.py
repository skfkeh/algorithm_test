### BAEKJOON
# https://www.acmicpc.net/problem/1920
n = input()
nlist = list(map(int, input().split()))
m = input()
mlist = list(map(int, input().split()))
nlist.sort()

for i in mlist:
    lt, rt = 0, int(n)-1
    Flag = False
    
    while lt <= rt:
        mid = (lt+rt)//2
        if i == nlist[mid]:
            Flag = True
            print(1)
            break
        elif i > nlist[mid]:
            lt = mid+1
        else:
            rt = mid-1
    if not Flag:
        print(0)
