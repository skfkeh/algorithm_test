### baekjoon
# https://www.acmicpc.net/problem/1181
def Sorting(li):
    li2 = sorted(li, key=len)
    return li2

n = int(input())
txtlist = []

for i in range(n):
    txtlist.append(input())
    
txtlist1 = Sorting(sorted(list(set(txtlist))))
for i in txtlist1:
    print(i)
