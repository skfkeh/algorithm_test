### BAEKJOON
# https://www.acmicpc.net/problem/2309
nlist = []
total = 0
for i in range(9):
    n = int(input())
    nlist.append(n)
total = sum(nlist)

a, b = 0, 0
chk = False
for i in range(9):
    ## i와 j를 하나씩 비교
    for j in range(i+1, 9):
        if total - nlist[i] - nlist[j] == 100:
            a, b = nlist[i], nlist[j]
            chk = True
            break
    ## 모두 할당 됐다면 break
    if chk == True:
        break
nlist.remove(a)
nlist.remove(b)
nlist.sort()

for i in nlist:
    print(i)